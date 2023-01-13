import uuid
import clickhouse_connect
from copy import deepcopy
from concurrent.futures import ThreadPoolExecutor, as_completed


def make_date(index, sub_target, random_data):
    target_data = []
    while True:
        if len(target_data) >= sub_target:
            break
        random_data[0] = str(uuid.uuid1()).upper().replace("-", "") + str(uuid.uuid1()).upper().replace("-", "")
        target_data.append(deepcopy(random_data))
        print(f"\r{index + 1}号线程正在努力创造数据了，进度：{(len(target_data) / sub_target) * 100}%， 客官别着急哦...",
              end="\n", flush=True)
    client = clickhouse_connect.get_client(host='172.20.8.110', port=32003, username='default', password='ck@12345')
    client.insert(f"{data_name}.{table}", target_data)
    client.close()
    return index, target_data


def run():
    client = clickhouse_connect.get_client(host='172.20.8.110', port=32003, username='default', password='ck@12345')
    count = client.command(f"select count(*) from {data_name}.{table};")
    need_num = target - count
    print(f"目标是{target}条，当前拥有{count}条数据，与目标相差{need_num}条")
    if need_num <= 0:
        print(f"不需要增加，已退出")
        return
    thread_num = 10000
    total_thread = need_num // thread_num
    last_num = need_num % thread_num
    task_list = []
    executor = ThreadPoolExecutor(max_workers=10)
    for index in range(0, total_thread):
        random_data = client.command(f"select * from {data_name}.{table} order by rand() limit 1;")
        task_list.append(executor.submit(lambda cxp: make_date(*cxp), (index, thread_num, random_data)))
    if last_num:
        random_data = client.command(f"select * from {data_name}.{table} order by rand() limit 1;")
        task_list.append(executor.submit(lambda cxp: make_date(*cxp), (total_thread, last_num, random_data)))
    for future in as_completed(task_list):
        index, target_data = future.result()
        count += len(target_data)
        print(f"\033[1;31m{index}号线程已经完成, 当前有{count}条数据，进度{count / target * 100}%\033[0m")
    print("所有任务已经添加完成！！！！！开心吧")


if __name__ == '__main__':
    data_name = "p_6391260117622329344"
    table = "d_6402658882224656384"
    target = 8010000
    run()
