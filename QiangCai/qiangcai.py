import time

import uiautomator2 as u2


# 连接手机
def connect_phone():
    u2.connect()
    d = u2.connect("RFCN309ABWX")
    if not d.service("uiautomator").running():
        # 启动uiautomator服务
        print("start uiautomator")
        d.service("uiautomator").start()
        time.sleep(2)

    if not d.agent_alive:
        print("agent_alive is false")
        u2.connect()
        d = u2.connect("RFCN309ABWX")
    return d


def run():
    d = connect_phone()
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
            print("确认支付")
            d(resourceId="btn-line").click()
            break
        print("本次花费时间:", time.time() - start)
        print("总共花费时间:", (time.time() - time_start) / 60, "分钟，第", count, "次")
        count += 1
    try:
        if d.wait_activity("com.meituan.retail.c.android.newhome.newmain.NewMainActivity", timeout=10):
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
                    print("确认支付")
                    d(resourceId="btn-line").click()
                    break
                print("本次花费时间:", time.time() - start)
                print("总共花费时间:", (time.time() - time_start) / 60, "分钟，第", count, "次")
                count += 1
    except Exception as e:
        if d.wait_activity("com.meituan.retail.c.android.newhome.newmain.NewMainActivity", timeout=10):
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
                    print("确认支付")
                    d(resourceId="btn-line").click()
                    break
                print("本次花费时间:", time.time() - start)
                print("总共花费时间:", (time.time() - time_start) / 60, "分钟，第", count, "次")
                count += 1


if __name__ == '__main__':
    run()

# d.app_stop("com.ss.android.ugc.aweme")
# print("stop app")
