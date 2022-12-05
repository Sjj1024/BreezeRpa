import uuid
import clickhouse_connect
from copy import deepcopy
from concurrent.futures import ThreadPoolExecutor, as_completed


def make_date(index, sub_target, random_data):
    print(f"{index + 1}号线程目标任务{sub_target}")
    target_data = []
    while True:
        if len(target_data) >= sub_target:
            break
        random_data[0] = str(uuid.uuid1()).upper().replace("-", "") + str(uuid.uuid1()).upper().replace("-", "")
        target_data.append(deepcopy(random_data))
        print(f"\r{index + 1}号线程正在努力创造数据了，进度：{(len(target_data) / sub_target) * 100}%， 客官别着急哦...",
              end="", flush=True)
    return index, target_data


def run():
    count = client.command(f"select count(*) from {data_name}.{table};")
    need_num = target - count
    print(f"目标是{target}条，当前拥有{count}条数据，与目标相差{need_num}条")
    thread_num = 3000
    total_thread = need_num // thread_num
    last_num = need_num % thread_num
    task_list = []
    for index in range(0, total_thread):
        random_data = client.command(f"select * from {data_name}.{table} order by rand() limit 1;")
        task_list.append(executor.submit(lambda cxp: make_date(*cxp), (index, thread_num, random_data)))
    if last_num:
        random_data = client.command(f"select * from {data_name}.{table} order by rand() limit 1;")
        task_list.append(executor.submit(lambda cxp: make_date(*cxp), (total_thread, last_num, random_data)))
    for future in as_completed(task_list):
        index, target_data = future.result()
        print(f"{index}任务已经完成, 开始插入数据....")
        client.insert(f"{data_name}.{table}", target_data)
        count = client.command(f"select count(*) from {data_name}.{table};")
        print(f"\n\033[1;31m{index}任务已经完成, 当前有{count}条数据，进度{count / target * 100}%...\033[0m")
    print("所有任务已经添加完成！！！！！开心吧")


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=1)
    client = clickhouse_connect.get_client(host='172.20.8.110', port=32003, username='default', password='ck@12345')
    data_name = "p_6391260117622329344"
    table = "d_6398812264584974336"
    target = 10710000
    run()