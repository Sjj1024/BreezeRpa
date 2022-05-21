import time

import uiautomator2 as u2

# 连接手机
def connect_phone(device_name):
    d = u2.connect(device_name)
    if not d.uiautomator.start():
        # 启动uiautomator服务
        print("start uiautomator")
        d.uiautomator.start()
        time.sleep(2)
    return d

if __name__ == '__main__':
    device_name = "RFCN309ABWX"
    d = connect_phone(device_name)
    if d(textContains="全选").exists:
        print("全选")
        d(textContains="全选").click()


