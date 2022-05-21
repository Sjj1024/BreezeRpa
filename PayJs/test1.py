from payjs import PayJS # 也可根据个人习惯选择使用 Payjs/PAYJS/payjs
from payjs import PayJSNotify # 也可根据个人习惯选择使用 PayjsNotify/PAYJSNotify

MCHID = '1593541201'
KEY = 'YiQtLvcisq1Fjzo5'

# 初始化
p = PayJS(MCHID, KEY)

CALLBACK_URL = ""
# 扫码支付
OUT_TRADE_NO = '2017TEST' # 外部订单号（自己的支付系统的订单号，请保证唯一）
TOTAL_FEE = 10 # 支付金额，单位为分，金额最低 0.01 元最多 10000 元
BODY = '测试支付' # 订单标题
NOTIFY_URL = 'https://pay.singee.site/empty/' # Notify 网址
ATTACH = 'info' # Notify 内容
r = p.QRPay(out_trade_no=OUT_TRADE_NO, total_fee=TOTAL_FEE, body=BODY, notify_url=NOTIFY_URL, attach=ATTACH)
if r:
    print(r.code_url)         # 二维码地址（weixin:// 开头，请使用此地址构建二维码）
    print(r.qrcode)           # 二维码地址（https:// 开头，为二维码图片的地址）
    print(r.payjs_order_id)   # 订单号（PAYJS 的）
else:
    print(r.STATUS_CODE)      # HTTP 请求状态码
    print(r.ERROR_NO)         # 错误码
    print(r.error_msg)        # 错误信息
    print(r)

# 构造收银台支付网址（仅构造链接，请使用浏览器 302 到这个网址，无法预检查调用是否成功）
c = p.get_cashier_url(out_trade_no=OUT_TRADE_NO, total_fee=TOTAL_FEE, body=BODY, callback_url=CALLBACK_URL, notify_url=NOTIFY_URL, attach=ATTACH)
print(c)

# JSApi 支付
OPENID = '这里填写支付用户的 OpenID' # 支付用户在 PayJS 端的 OpenID，可通过 get_openid 获取
j = p.JSApiPay(out_trade_no=OUT_TRADE_NO, total_fee=TOTAL_FEE, openid=OPENID, body=BODY, notify_url=NOTIFY_URL, attach=ATTACH)
if j:
    print(j.jsapi)   # 用于发起支付的支付参数
else:
    print(j.STATUS_CODE)      # HTTP 请求状态码
    print(j.ERROR_NO)         # 错误码
    print(j.error_msg)        # 错误信息
    print(j)

# 刷卡支付
AUTH_CODE = '这里填写用户侧 18 位数字' # 用户的支付条码或二维码所对应的数字
m = p.MicroPay(out_trade_no=OUT_TRADE_NO, total_fee=TOTAL_FEE, auth_code=AUTH_CODE, body=BODY)
print(m)

# 订单查询
s = p.check_status(payjs_order_id=r.payjs_order_id)
if s:
    print(s.paid)            # 是否已支付
else:
    print(s.error_msg)       # 错误信息
    print(s)

# 订单关闭
t = p.close(r.payjs_order_id)
if t:
    print('Success')
else:
    print('Error')
    print(t.return_msg)

# 订单退款
t = p.refund(r.payjs_order_id)
if t:
    print('Success')
else:
    print('Error')
    print(t.return_msg)

# 获取用户 OpenId
o = p.get_openid(callback_url=CALLBACK_URL)
print(o)

# 回调验证
n = PayJSNotify(KEY, '回调内容（str 或 dict）')
print(n)