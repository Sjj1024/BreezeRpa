# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
import requests
import time
import hashlib
from urllib.parse import urlencode,unquote
'''
扫码支付（主扫）
'''
mchid = '1593541201'        # PAYJS 商户号
key   = 'YiQtLvcisq1Fjzo5'        # 通信密钥

time = str(int(time.time()))
# 默认微信支付，如果是支付宝需要添加："type":"alipay"

order = {
    'body'         : 'test',  # 订单标题
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