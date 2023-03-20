import random
import uuid
import pandas as pd
import numpy as np
import clickhouse_connect
from copy import deepcopy
from concurrent.futures import ThreadPoolExecutor, as_completed


def make_date(index, start_num, sub_target, random_data):
    target_data = []
    index_num = start_num + (index * sub_target)
    while True:
        if len(target_data) >= sub_target:
            break
        index_num += 1
        # 创造ID列，是否加密
        if use_uuid:
            random_data[0] = str(uuid.uuid1()).upper().replace("-", "") + str(uuid.uuid1()).upper().replace("-", "")
        else:
            random_data[0] = str(index_num)
        # 创建X列：范围-100, 1000000
        if len(random_data) > 1:
            # 使用历史数据
            print("使用库中数据，不自己造数据了")
        else:
            # 自己造数据:根据多少列来自己创造
            print("自己造数据")
            for col in range(1, column + 1):
                random_data[col] = random.randint(-100, 1000000)
        target_data.append(deepcopy(random_data))
    client = clickhouse_connect.get_client(host=host, port=port, username=username, password=password)
    client.insert(f"{data_name}.{table}", target_data)
    client.close()
    return index, target_data


def creat_mock_data():
    print("使用代码自己创建随机数据mock...")


def creat_copy_data(client, need_num, count, current_count):
    print("数据库中已经存在数据，就从已存在数据中随机copy...")
    thread_num = 10000
    total_thread = need_num // thread_num
    last_num = need_num % thread_num
    task_list = []
    executor = ThreadPoolExecutor(max_workers=50)
    print(f"所有子线程都在努力创造数据了，total_thread: {total_thread}，last_num: {last_num}")
    for index in range(0, total_thread):
        # 是使用库中的还是使用随机的
        if use_mock:
            random_data = []
        else:
            random_data = client.command(f"select * from {data_name}.{table} order by rand() limit 1;")
        task_list.append(executor.submit(lambda cxp: make_date(*cxp), (index, count, thread_num, random_data)))
    if last_num:
        # 是使用库中的还是使用随机的
        if use_mock:
            random_data = []
        else:
            random_data = client.command(f"select * from {data_name}.{table} order by rand() limit 1;")
        start_num = count + thread_num * total_thread
        task_list.append(executor.submit(lambda cxp: make_date(*cxp), (0, start_num, last_num, random_data)))
    for future in as_completed(task_list):
        index, target_data = future.result()
        current_count += len(target_data)
        print(f"\033[1;31m{index}号线程已经完成, 进度{current_count / target * 100}%\033[0m", end="\n", flush=True)
    count = client.command(f"select count() from {data_name}.{table};")
    distinct_count = client.command(f"select count(DISTINCT id) from {data_name}.{table};")
    print(f"所有任务已经添加完成！总数据有{count}条，去重后有{distinct_count}条，重复数据{count - distinct_count}条")


def creat_template_csv():
    print("创建模板csv文件，用于在项目中上传后，和ck数据库关联")
    # guest 创建多少列并加入y列
    host_column = {}
    guest_column = {"y": [1]}
    for i in range(1, column + 1):
        host_column[f"x{i}"] = [1]
        guest_column[f"x{i}"] = [1]
    df_host = pd.DataFrame(host_column)
    df_host.to_csv(f'host_{column}col_template.csv', index_label="id")
    df_guest = pd.DataFrame(guest_column)
    df_guest.to_csv(f'guest_{column}col_template.csv', index_label="id")
    print("csv模板已经生成，里面会存在1条测试数据，不用管，后面生成数据的时候会先清理掉。\n"
          "请在添加数据集管理里面上传此模板，上传完成后，在数据库中的dataset表中找到项目id和数据集id。\n"
          "然后到ck数据库中执行下面的sql检测是否成功：确认成功后即可开始创造数据")
    print(f"""-- 先从mysql的dateset表中找到项目id和id，然后替换为p_项目id.d_数据集id
SELECT * FROM p_项目ID.d_数据集id;
-- 去重的SQL
select count(distinct(id)) from p_项目ID.d_数据集id;
-- 统计总得数量
select count(id) from p_项目ID.d_数据集id;
-- 清空表数据或者删除某条数据
alter table p_6540819793207889920.d_6542157498671960064 delete where id != '';
""")


def start_run():
    confirm = input(f"确定要向表{table}中创造数据么？不要弄错表了哦，确认无误后回车即可开始！")
    client = clickhouse_connect.get_client(host=host, port=port, username=username, password=password)
    count = client.command(f"select count() from {data_name}.{table};")
    # 判断数据表中的数据是否是1条
    if count == 1:
        # 清空表内容
        client.command(f"alter table {data_name}.{table} delete where id != '';")
    # 区分是guest还是host：guest添加y host不用
    if role == "guest":
        print(f"是guest用户，需要添加y列")
    else:
        print("是host，不用添加y列")
    # 区分id用不用加密，是否需要有序

    # 创建数据，普通数据范围-100, 1000000，y列数据范围：0，1

    # 创建完成之后，检查数据数据是否正确

    current_count = client.command(f"select count(DISTINCT id) from {data_name}.{table};")
    need_num = target - current_count
    print(f"目标是{target}条，当前拥有{count}条数据，去重后有{current_count}条数据，与目标相差{need_num}条")
    if need_num <= 0:
        print(f"不需要增加，已退出")
        return
    # 判断是自己代码mock还是copy已有数据
    if use_mock:
        creat_mock_data()
    else:
        creat_copy_data(client, need_num, count, current_count)


# 薛蕾 1-13 16:56:31
# C端参与方：
# 薛蕾 1-13 16:56:40
# data_name = "p_6481060737912410112"
# table = "d_6481062251838050304"

# 薛蕾 1-13 16:57:35
# A端发起方：
# 薛蕾 1-13 16:57:38
# data_name = "p_6481060737912410112"
# table = "d_6481061340080246784"


if __name__ == '__main__':
    # 数据库配置：ip port user passwd
    host = "172.20.8.110"
    # port = 31003
    port = 31003
    username = "default"
    password = "ck@12345"
    # 要向哪个库的哪个表里面创建数据
    data_name = "p_6540819793207889920"
    table = "d_6542157498671960064"
    # 目标数据：多少列，仅在创建模板的时候有用
    column = 10
    # 目标数据：多少条，仅在创建数据的时候有用
    target = 50 * 10000
    # 是否对ID加密
    use_uuid = True
    # ID列是否有序
    order_id = True
    # 是 guest 还是 host
    role = "guest"
    # 自己代码创建还是copy已有的数据: True mock, False copy
    use_mock = True
    # 创建模板csv文件
    # creat_template_csv()
    # 插入数据
    start_run()
