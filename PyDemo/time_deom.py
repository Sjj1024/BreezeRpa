import time


def timestamp_to_time():
  t = time.time()
  print(f"得到的时间戳是:{int(t)}, 原始数据是:{t}")
  print("时间戳转时间")
  timeStamp = 1640595861
  timeArray = time.localtime(timeStamp)
  otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
  print(otherStyleTime)


if __name__ == '__main__':
  timestamp_to_time()
