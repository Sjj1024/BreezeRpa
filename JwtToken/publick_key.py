import json

import jwt
from jwt.algorithms import RSAAlgorithm
from jwt.utils import force_bytes


def get_user_ifon(id_token):
  try:
    algo = RSAAlgorithm(RSAAlgorithm.SHA256)
    pem_key = open("/Users/metrodata/Desktop/PyProject/BreezeRpa/JwtToken/publick_key.txt", 'r')
    public_key = algo.prepare_key(pem_key.read())
    token_info = jwt.decode(force_bytes(id_token), key=public_key, verify=True)
    user_info = json.loads(json.dumps(token_info))
    print(user_info)
    username = user_info['sub']
    print(username)
    # 3.判断用户名是否在自己系统存在
    # 4.如果用户存在, 则登录成功，创建业务系统自己的会话，返回登录成功后的页面，略
    # 5.如果参数中有target_url，那么返回此指定url页面
    # 6.否则返回系统默认操作页面
    # 7. 如果用户不存在, 返回登录失败页面, 提示用户不存在
  except Exception as e:
    print(e)


if __name__ == '__main__':
  encoded_jwt = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjU5OTUxOTE3NTQyMDI1MTg1MTEifQ.eyJlbWFpbCI6IjEzMjM0MjFAcXEuY29tIiwibmFtZSI6Im1haWNlIiwibW9iaWxlIjpudWxsLCJleHRlcm5hbElkIjoiODk2OTM3MDYzMjU0MTE2MjEzIiwidWRBY2NvdW50VXVpZCI6ImQ4Nzc1NDBhN2E3N2Y0NzI5NmVjZmY5OTA3OTQzNzQ0U2tOYnhVTEptNXkiLCJvdUlkIjoiMjMyMDE4OTI4MDc2MDk5MzY1MSIsIm91TmFtZSI6IumVv-S4ieinkiIsIm9wZW5JZCI6bnVsbCwiaWRwVXNlcm5hbWUiOiJtYWljZSIsInVzZXJuYW1lIjoibWFpY2UiLCJhcHBsaWNhdGlvbk5hbWUiOiLmmbrog73pgInlnYBf6KeE5YiS566h55CGIiwiZW50ZXJwcmlzZUlkIjoiaWRhYXMiLCJpbnN0YW5jZUlkIjoiaWRhYXMiLCJhbGl5dW5Eb21haW4iOiIiLCJleHRlbmRGaWVsZHMiOnsidGhlbWVDb2xvciI6ImdyZWVuIiwiYXBwTmFtZSI6IuaZuuiDvemAieWdgF_op4TliJLnrqHnkIYifSwiZXhwIjoxNjQ2MTI0Mjc2LCJqdGkiOiIwZ3RmV3pxTHVvckc1M09jVUtZTkhBIiwiaWF0IjoxNjQ2MTIzNjc2LCJuYmYiOjE2NDYxMjM2MTYsInN1YiI6Im1haWNlIiwiaXNzIjoiaHR0cDovLzEwLjkwLjUuOTAvIiwiYXVkIjoiaWRhYXNwbHVnaW5fand0MTQifQ.CddyMl_q9eK1Mfid-gYilJ43D-wMcyNW3GliTZh6JrFKFn8pHsVwnsYxDFlk93vcp7tK3_HyGCSV99AfF8LKj9q1VE3B83q9fcTK8pyc67EJJDonRRuYXbx82_34V5N3UhZBHAxhrIwmO943GeHuobBumXSfTtKhiX-VJ1taPQDMJvMDGbe-wCHJws18NZypjFYccoZjvc-Biy8z7y-ST0dit_TiwGDSNvDd5I1hSxGtcfUtkUIRuaO6xRZ6KC_PTvD_J5-jmHOjpLjp99rIHpS3FLhHmDKHPzDDiAgHUrel1hp6ZMmldWA27HjuUNZs8gVngZJXJ92sKY3d0btRDQ"
  get_user_ifon(encoded_jwt)
