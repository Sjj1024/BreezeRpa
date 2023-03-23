from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
# 企业微信提醒点外卖打卡等
import datetime
import requests
import json


def work_on_remind(url, payload):
    # 提醒上班打卡
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def pay_lunch_remind(url, payload):
    # 提醒点外卖
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def work_off_remind(url, payload):
    # 提醒下班打卡
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def run(wx_url):
    current_hour = datetime.datetime.now().hour
    current_minute = datetime.datetime.now().minute
    current_second = datetime.datetime.now().second
    current_time = f"{current_hour}点{current_minute}分{current_second}秒"
    dayOfWeek = datetime.datetime.now().weekday() + 1
    print(f"今天是星期{dayOfWeek}, 当前时间是：{current_time}")
    if dayOfWeek == 6 or dayOfWeek == 7:
        print(f"今天是周六周日，不用发送签到内容")
        return
    if (current_hour == 9) and (50 <= current_minute <= 59):
        content = f"上班打卡了，亲爱的宝子们~，需要艾特的话给我发手机号，当前时间:{current_time}"
        payload = json.dumps({
            "msgtype": "text",
            "text": {
                "content": content,
                "mentioned_mobile_list": mentioned_mobile_list
            }
        })
        work_on_remind(wx_url, payload)
    elif (current_hour == 11) and (0 <= current_minute < 10):
        content = f"快点外卖吧，吃的胖胖的才有劲干活啊，亲爱的宝~, 需要艾特的话给我发手机号， 当前时间:{current_time}"
        payload = json.dumps({
            "msgtype": "text",
            "text": {
                "content": content,
                "mentioned_mobile_list": mentioned_mobile_list
            }
        })
        pay_lunch_remind(wx_url, payload)
    elif (current_hour == 19) and (0 <= current_minute < 10):
        content = f"别干了，快下班打卡吧！总是忘记打卡的人，是不是你？！！！,需要艾特的话给我发手机号，当前时间:{current_time}"
        payload = json.dumps({
            "msgtype": "text",
            "text": {
                "content": content,
                "mentioned_mobile_list": mentioned_mobile_list
            }
        })
        work_off_remind(wx_url, payload)
    else:
        print("不用发送打卡内容")


if __name__ == '__main__':
    """
    ps -aux | grep python
    nohup python3 -u qiwei_remind.py > zet_remind.log 2>&1 &
    """
    scheduler = BlockingScheduler()
    # 企业微信机器人接口地址
    mentioned_mobile_list = ["15670339118", "17621631021", "15071018589"]
    wx_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=89c9eedd-31db-4e36-bbb3-6176ed9b4395"
    corn_tab = "*/10 * * * *"
    scheduler.add_job(run, CronTrigger.from_crontab(corn_tab), args=(wx_url,))
    print(f"定时任务启动了：定时提醒签到内容")
    scheduler.start()
