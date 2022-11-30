# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
import time
import hashlib
from urllib.parse import urlencode,unquote
import qrcode
'''
收银台支付
'''
mchid = '1593541201'        # PAYJS 商户号
key   = 'YiQtLvcisq1Fjzo5'        # 通信密钥

# 构造订单参数
time = str(int(time.time()))


# 1024小神支付使用的就是这种方式，然后将url生成二维码，即可支付
# 默认微信支付，如果是支付宝需要添加："type":"alipay"
order = {
    'mchid'        : mchid,
    'body'         : '我是一个测试订单标题',       # 订单标题
    'total_fee'    : 110,                          # 金额,单位:分
    'out_trade_no' : 'payjs_jspay_demo_'+time,   # 订单号
    "auto":1,
    "hide":1,
    "type":"alipay"
}



# 构造签名函数
def sign(attributes,key):
    attributes_list = list(attributes)
    for a in attributes_list:
        if attributes[a]=='':
            attributes.pop(a)
    attributes_new = {k: attributes[k] for k in sorted(attributes.keys())}
    return hashlib.md5((unquote(urlencode(attributes_new))+'&key='+key)
        .encode(encoding='utf-8')).hexdigest().upper()

# 添加数据签名
order['sign'] = sign(order,key)

# 浏览器跳转到收银台
url = 'https://payjs.cn/api/cashier?'+str(urlencode(order))
# web.open(url,new=0,autoraise=True)
print(url)

qr = qrcode.QRCode()  # 事实上里面的参数我们可以都不指定，默认会选择一个比较合适的参数

# 调用add_data，指定url。
qr.add_data(url)
# 生成二维码图像，颜色为蓝色，背景色为粉色
img = qr.make_image(fill_color='black', back_color='white')
# 显示图像，这个会打开一个临时文件
img.show()
# 此外，我们还可以保存到硬盘上
img.save("1.png")