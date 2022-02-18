import datetime
import time
import pandas as pd


def timestamp_to_time():
  t = time.time()
  print(f"得到的时间戳是:{int(t)}, 原始数据是:{t}")
  print("时间戳转时间")
  timeStamp = 1640595861
  timeArray = time.localtime(timeStamp)
  otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
  print(otherStyleTime)


def get_last_time():
  today = datetime.date.today()
  last_day_of_last_month = datetime.date(today.year, today.month, 1) - datetime.timedelta(1)
  first_day_of_last_month = datetime.date(last_day_of_last_month.year,
                                          last_day_of_last_month.month, 1)
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


if __name__ == '__main__':
  # timestamp_to_time()
  # get_last_time()
  start_run()
