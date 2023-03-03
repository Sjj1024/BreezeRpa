import datetime
import time
import pandas as pd


def timestamp_to_time():
    t = time.time()
    print(f"得到的时间戳是:{int(t)}, 原始数据是:{t}")
    timeStamp = 1640595861
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime)


def get_last_time():
    today = datetime.date.today()
    last_day_of_last_month = datetime.date(today.year, today.month, 1) - datetime.timedelta(1)
    first_day_of_last_month = datetime.date(last_day_of_last_month.year,
                                            last_day_of_last_month.month, 1)
    # 加一秒
    today_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    today_second = datetime.datetime.strptime(today_str, "%Y-%m-%d %H:%M:%S")
    last_second = today_second + datetime.timedelta(seconds=1)
    last_day = last_day_of_last_month.day
    first_day = first_day_of_last_month.day
    five_day_after = first_day_of_last_month + datetime.timedelta(5)
    if last_day_of_last_month < first_day_of_last_month:
        print("下载数据")
        first_day_of_last_month, five_day_after = five_day_after, five_day_after + datetime.timedelta(5)
        first_day += 5
    return first_day_of_last_month, last_day_of_last_month


def start_run():
    today = datetime.date.today()
    last_day_of_last_month = datetime.date(today.year, today.month, 1) - datetime.timedelta(1)
    start_date = datetime.date(last_day_of_last_month.year,
                               last_day_of_last_month.month, 1)
    result_data = pd.DataFrame()
    while True:
        eight_day_after = start_date + datetime.timedelta(8)
        if eight_day_after > last_day_of_last_month:
            data = pd.DataFrame({
                '电梯编号': ['a', 'b', 'c', 'd', 'e'],
                'key2': ['one', 'two', 'one', 'two', 'three'],
                '本月实缴金额': [2, 2, 2, 2, 2],
                'data2': [5, 5, 5, 10, 5],
                'data3': [5.01, 5.01, 5.01, 10.23, 5.01]
            })
            result_data = result_data.append(data)
            break
        data = pd.DataFrame({
            '电梯编号': ['a', 'b', 'c', 'd', 'e'],
            'key2': ['one', 'two', 'one', 'two', 'three'],
            '本月实缴金额': [2, 2, 2, 2, 2],
            'data2': [5, 5, 5, 10, 5],
            'data3': [5.01, 5.01, 5.01, 10.23, 5.01]
        })
        result_data = result_data.append(data)
        start_date = eight_day_after
    print(f"得到的结果是:\n{result_data}")


def list_err():
    list_e = [
        [314583, '2022-02-24 10:34:48', '0', '5', '璞吉(上海)医疗科技有限公司', '0', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', '0',
         '0', '0', '91310117MA1J2J1054', '嘉发大厦', '嘉发大厦', '0', '0', '0', '0', '0', '0',
         "[{'楼宇': '嘉发大厦', '楼层': '5', '楼宇名称二级': '嘉发大厦'}]"],
        [314584, '2022-02-24 10:34:48', '0', '5', '上海黄章林品牌策划工作室', '0', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', '0',
         '0', '0', '310117003208313', '嘉发大厦', '嘉发大厦', '0', '0', '0', '0', '0', '0',
         "[{'楼宇': '嘉发大厦', '楼层': '5', '楼宇名称二级': '嘉发大厦'}]"],
        [314585, '2022-02-24 10:34:48', '0', '1,1', '上海云聚程国际旅行社有限公司', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', '0', '0',
         '0', '0', '91310106MA1FYLTG0L', '嘉发大厦', '嘉发大厦', '0', '0', '0', '0', '0', '0',
         "[{'楼宇': '嘉发大厦', '楼层': '1', '楼宇名称二级': '嘉发大厦'}, {'楼宇': '嘉发大厦', '楼层': '1', '楼宇名称二级': '嘉发大厦'}]"],
        [314586, '2022-02-24 10:34:48', '0', '1,1', '上海市静安区秦鹏私立口腔诊所', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', '0', '0',
         '0', '0', '92310106MA1KE7053C', '嘉发大厦', '嘉发大厦', '0', '0', '0', '0', '0', '0',
         "[{'楼宇': '嘉发大厦', '楼层': '1', '楼宇名称二级': '嘉发大厦'}, {'楼宇': '嘉发大厦', '楼层': '1', '楼宇名称二级': '嘉发大厦'}]"],
        [314587, '2022-02-24 10:34:48', '0', '10',
         '北京冲浪科技有限公司                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ',
         '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '91110108MA00EQAT57', '嘉发大厦', '嘉发大厦',
         '0', '0',
         '0', '0', '0', '0', "[{'楼宇': '嘉发大厦', '楼层': '10', '楼宇名称二级': '嘉发大厦'}]"]]
    if "91110108MA00EQAT57" in str(list_e):
        print("在")
    str_1 = "1"
    int_1 = [1, 3]
    if isinstance(int_1, (list, str)):
        print("类型正确")


def get_time_str():
    import datetime
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':
    # timestamp_to_time()
    get_last_time()
    # start_run()
    # list_err()
    # get_time_str()
