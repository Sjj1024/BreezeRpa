import datetime
import requests
import json


def work_off_remind(url, content):
    # 提醒下班打卡
    payload = json.dumps({
        "msgtype": "text",
        "text": {
            "content": content,
            # "mentioned_list": [
            #     "songjiangjiang"
            # ],
            "mentioned_mobile_list": ["15670339118"]
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


if __name__ == '__main__':
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=89c9eedd-31db-4e36-bbb3-6176ed9b4395"
    content = "测试消息"
    work_off_remind(url, content)
