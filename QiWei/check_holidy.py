import datetime
from chinese_calendar import is_workday, is_holiday, is_in_lieu

time2 = datetime.datetime.now()
if is_workday(time2):
    print("今天是工作日")
if is_in_lieu(time2):
    print("今天是调休日")
if is_holiday(time2):
    print("今天是休息日")
