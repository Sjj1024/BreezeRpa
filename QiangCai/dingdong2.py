import os
import time

import uiautomator2 as u2


# from playsound import playsound

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


def ti_xing():
    os.system('say "抢到菜了，快来看"')


# 时间判断
def is_five_o_clock():
    return time.strftime('%H:%M') >= '05:59'


# 获取当前的时间
def get_current_hour(d):
    info = d.xpath('//*[@resource-id="com.yaya.zone:id/rv_selected_hour"]').get(timeout=1).info
    return info.get("childCount", 0)


def run(device_name):
    d = connect_phone(device_name)
    count = 1
    time_start = time.time()
    # 此处填设备编号
    while True:
        start = time.time()
        if d(textContains="结算(").exists:
            print("点击结算")
            d(textContains="结算(").click()

        if d(text="我知道了").exists:
            print("点击我知道了")
            d(text="我知道了").click()

        # if d(text="返回购物车").exists:
        #     print("点击返回购物车")
        #     d(text="返回购物车").click()

        if d(text="重新加载").exists:
            print("点击重新加载")
            d(text="重新加载").click()

        if d(text="立即支付").exists:
            print("点击立即支付")
            d(text="立即支付").click()

        hour_count = get_current_hour(d)
        for i in range(hour_count):
            info = d.xpath(
                '//*[@resource-id="com.yaya.zone:id/rv_selected_hour"]'
                '/android.view.ViewGroup[%s]' % str(i + 1)).get(timeout=1).info
            if info.get("enabled", "") != "false":
                print("TMD 有运力了")
                d.xpath(
                    '//*[@resource-id="com.yaya.zone:id/rv_selected_hour"]'
                    '/android.view.ViewGroup[%s]' % str(i + 1)).click_exists(timeout=1)
                print("点击了第" + str(i + 1) + "个")
                ti_xing()
                if d(text="立即支付").exists:
                    print("点击立即支付")
                    d(text="立即支付").click()
            if i == hour_count - 1:
                print("没有运力了")
                d.xpath('//*[@resource-id="com.yaya.zone:id/'
                        'iv_dialog_select_time_close"]').click_exists(timeout=1)
                d.xpath('//*[@resource-id="com.yaya.zone:id/'
                        'iv_order_back"]').click_exists(timeout=1)

        if d(text="下单失败").exists:
            print("下单失败")
            if d(text="返回购物车").exists:
                print("点击返回购物车")
                d(text="返回购物车").click()

        if d(text="确认交易").exists:
            print("点击确认交易")
            d(text="确认交易").click()
            ti_xing()

        if d(text="确认并支付").exists:
            print("点击确认并支付")
            d(text="确认并支付").click()

        if d(resourceId="btn-line").exists:
            print("确认支付")
            d(resourceId="btn-line").click()
            ti_xing()

        print("本次花费时间:", time.time() - start)
        print("总共花费时间:", (time.time() - time_start) / 60, "分钟，第", count, "次")
        count += 1


if __name__ == '__main__':
    # 此处填设备编号
    device_name = "RFCN309ABWX"
    run(device_name)
