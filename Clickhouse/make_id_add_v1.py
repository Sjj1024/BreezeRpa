import uuid
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
        if use_uuid:
            random_data[0] = str(uuid.uuid1()).upper().replace("-", "") + str(uuid.uuid1()).upper().replace("-", "")
        else:
            random_data[0] = str(index_num)
        target_data.append(deepcopy(random_data))
    client = clickhouse_connect.get_client(host=host, port=port, username=username, password=password)
    client.insert(f"{data_name}.{table}", target_data)
    client.close()
    return index, target_data


def run():
    client = clickhouse_connect.get_client(host=host, port=port, username=username, password=password)
    count = client.command(f"select count() from {data_name}.{table};")
    current_count = client.command(f"select count(DISTINCT id) from {data_name}.{table};")
    need_num = target - current_count
    print(f"目标是{target}条，当前拥有{count}条数据，去重后有{current_count}条数据，与目标相差{need_num}条")
    if need_num <= 0:
        print(f"不需要增加，已退出")
        return
    thread_num = 10000
    total_thread = need_num // thread_num
    last_num = need_num % thread_num
    task_list = []
    executor = ThreadPoolExecutor(max_workers=50)
    print(f"所有子线程都在努力创造数据了，total_thread: {total_thread}，last_num: {last_num}")
    for index in range(0, total_thread):
        random_data = client.command(f"select * from {data_name}.{table} order by rand() limit 1;")
        task_list.append(executor.submit(lambda cxp: make_date(*cxp), (index, count, thread_num, random_data)))
    if last_num:
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
    host = "172.20.58.37"
    # port = 31003
    port = 32003
    username = "default"
    password = "ck@12345"
    data_name = "p_6481060737912410112"
    table = "d_6482427017089257472"
    target = 50 * 10000
    # 是否对ID加密
    use_uuid = True
    run()
