import requests
import time
import hashlib
from urllib.parse import urlencode,unquote
'''
扫码支付（主扫）
'''
key = 'YiQtLvcisq1Fjzo5'         # 填写通信密钥
mchid = '1593541201'       # 特写商户号

time = str(int(time.time()))
order = {
    'body'         : 'test',  # 订单标题
    'out_trade_no' : time,    # 订单号
    'total_fee'    : 120,     # 金额,单位:分
    'mchid' : mchid
}

# 构造签名函数
def sign(attributes):
    attributes_new = {k: attributes[k] for k in sorted(attributes.keys())}
    return hashlib.md5((unquote(urlencode(attributes_new))+'&key='+key)
        .encode(encoding='utf-8')).hexdigest().upper()

order['sign'] = sign(order)
request_url = "https://payjs.cn/api/mweb"
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=order,headers=headers)
if response:
    print(response.json())