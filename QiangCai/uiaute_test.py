import uiautomator2 as u2

# 第2种连接手机的USB进行连接(安卓模拟器和真机都可以）必须开启USB调试模式
# CSQBL5000123456为手机序列号，`adb devices`查看
d = u2.connect_usb("RFCN309ABWX")
print(d.info)
# d = u2.connect_usb("b8c282ac")

# usb链接
# d = u2.connect_usb("emulator-5554")
# print(d.info)

# wifi链接:
# d = u2.connect_adb_wifi("192.168.31.197")
# print(d.info)

# d = u2.connect_wifi("192.168.31.197")
# print(d.info)

# U2控制移动设备
# 第1种通过手机WIFI来进行连接,参数为手机WIFI的IP地址（u2版本2.15.0几乎没有成功过）
# d = u2.connect_wifi("192.168.31.194")
# print(d.info)

# 第2种连接手机的USB进行连接(安卓模拟器和真机都可以）必须开启USB调试模式
# CSQBL5000123456为手机序列号，`adb devices`查看
# d = u2.connect_usb("CSQBL5000123456")
# print(d.info)

# 第3种 adb tcpip模式
# 开启了tcpip连接：adb tcpip 5555
# d = u2.connect_adb_wifi("127.0.0.1:7555")
# print(d.info)