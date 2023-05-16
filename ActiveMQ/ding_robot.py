import json
import time
import requests


class DingRobot(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(DingRobot)
        return cls.__instance

    def __init__(self):
        self.url = "https://oapi.dingtalk.com/robot/send?access_token=你的token"
        self.header = {
            "Content-Type": "application/json"
        }

    def send_msg(self, msg):
        time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        content = f"地震波消息:{msg}, 时间:{time_str}"
        data = {"msgtype": "text", "text": {"content": content}}
        try:
            res = requests.post(self.url, headers=self.header, data=json.dumps(data)).json()
            if res.get("errcode") == 0:
                print("地震波机器人发送消息成功! ")
            print(res)
        except Exception as e:
            print(f"dingding消息发送失败:{e}")


if __name__ == '__main__':
    ding = DingRobot()
    ding.send_msg("注意注意，地震波报警了")
