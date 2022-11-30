# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
import requests
import time
import hashlib
from urllib.parse import urlencode,unquote
import qrcode

'''
扫码支付（主扫）这个会有微信收款语音提醒
'''
mchid = '1593541201'        # PAYJS 商户号
key   = 'YiQtLvcisq1Fjzo5'        # 通信密钥

time = str(int(time.time()))
# 默认微信支付，如果是支付宝需要添加："type":"alipay"

order = {
    'body'         : 'payjs收款测试',  # 订单标题
    'out_trade_no' : time,    # 订单号
    'total_fee'    : 100,     # 金额,单位:分
    'mchid' : mchid,
    # "type":"alipay"
}

# 构造签名函数
def sign(attributes):
    attributes_new = {k: attributes[k] for k in sorted(attributes.keys())}
    return hashlib.md5((unquote(urlencode(attributes_new))+'&key='+key)
        .encode(encoding='utf-8')).hexdigest().upper()

order['sign'] = sign(order)
request_url = "https://payjs.cn/api/native"
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=order,headers=headers)
if response:
    print(response.json())
    qrcodeUrl = response.json()["code_url"]
    print(qrcodeUrl)
    qr = qrcode.QRCode()  # 事实上里面的参数我们可以都不指定，默认会选择一个比较合适的参数

    # 调用add_data，指定url。
    qr.add_data(qrcodeUrl)
    # 生成二维码图像，颜色为蓝色，背景色为粉色
    img = qr.make_image(fill_color='black', back_color='white')
    # 显示图像，这个会打开一个临时文件
    img.show()
    # 此外，我们还可以保存到硬盘上
    img.save("1.png")