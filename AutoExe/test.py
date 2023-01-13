from clicknium import clicknium as cc, locator
import subprocess
import time


def main():
    process = subprocess.Popen(r"E:\\v2rayn\\v2rayN.exe")
    time.sleep(10)
    cc.find_element(locator.v2rayn.menuitem_订阅).click()
    cc.find_element(locator.v2rayn.menuitem_更新订阅不通过代理).click()


if __name__ == "__main__":
    main()
