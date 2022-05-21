import os
import time
import uiautomator2 as u2


# 连接手机
def connect_phone(device_name):
    d = u2.connect(device_name)
    if not d.service("uiautomator").running():
        # 启动uiautomator服务
        print("start uiautomator")
        d.service("uiautomator").start()
        time.sleep(2)

    if not d.agent_alive:
        print("agent_alive is false")
        u2.connect()
        d = u2.connect(device_name)
    return d


def qiang_cai(device_name):
    d = connect_phone(device_name)
    d.app_start("com.sankuai.meituan")
    count = 1
    time_start = time.time()
    while True:
        start = time.time()
        if d(textContains="结算(").exists:
            print("点击结算")
            d(textContains="结算(").click()

        if d(text="我知道了").exists:
            print("点击我知道了")
            d(text="我知道了").click()

        if d(text="返回购物车").exists:
            print("点击返回购物车")
            d(text="返回购物车").click()

        if d(text="立即支付").exists:
            print("点击立即支付")
            d(text="立即支付").click()

        if d(text="确认并支付").exists:
            print("点击确认并支付")
            d(text="确认并支付").click()

        if d(resourceId="btn-line").exists:
            os.system('say "抢到菜了，快来看"')
            print("确认支付")
            d(resourceId="btn-line").click()
            # mac系统使用语音提示：说抢到菜了，windows请屏蔽
            # os.system('say "抢到菜了，快来看"')
            break
        print("本次花费时间:", time.time() - start)
        print("总共花费时间:", (time.time() - time_start) / 60, "分钟，第", count, "次")
        count += 1


def run(device_name):
    while True:
        try:
            qiang_cai(device_name)
        except Exception as e:
            print(e)
            os.system('say "有异常，尝试重新启动"')
            time.sleep(10)


if __name__ == '__main__':
    # device_name = "emulator-5554"
    device_name = "RFCN309ABWX"
    # device_name = "b8c282ac"
    run(device_name)
