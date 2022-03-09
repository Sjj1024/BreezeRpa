import json
import jwt
from config import *
import requests


def decode_id_token(encoded_jwt):
  """
  解析id_token
  """
  res = jwt.decode(encoded_jwt, publick_key, algorithms='HS256', options={"verify_signature": False})
  print(f"解析出来的UserInfo:{res}")
  return res


class CollectorClient:
  __instance = None

  def __init__(self):
    self.url = collector_url
    self.token = self.get_token(collector_username, collector_password)
    self.header = {
      'authorization': self.token,
      'content-type': 'application/json',
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }

  def __new__(cls, *args, **kwargs):
    if CollectorClient.__instance is None:
      CollectorClient.__instance = object.__new__(cls)
    return CollectorClient.__instance

  def get_token(self, username, password):
    """
    获取用户Token
    """
    url = f"{self.url}/login/password"
    payload = {
      "username": username,
      "password": password,
      "create": False
    }
    headers = {
      'content-type': 'application/json;charset=UTF-8',
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload)).json()
    access_token = response.get("result").get("access_token")
    return access_token

  def query_user_token(self, user_info):
    """
    查询用户是否存在，并返回token
    """
    user_id = user_info.get("ouId")
    url = f"{self.url}/data/query/{template_uuid}"
    payload = json.dumps({
      "q": f'string @ "{user_id}"'
    })
    response = requests.request("POST", url, headers=self.header, data=payload).json()
    result = response.get("result")
    if len(result):
      username = result[0].get("extra").get("用户名")
      password = result[0].get("extra").get("密码")
      return self.get_token(username, password)
    else:
      self.add_user(user_info)
      return self.get_token(collector_username, collector_password)

  def add_user(self, user):
    user_id = user.get("ouId")
    url = f"{self.url}/data/{template_uuid}"
    payload = {
      "extra": {
        "用户名": "jiangjiang",
        "密码": "123Jiang",
        "ouId": user_id,
        "第三方信息": json.dumps(user)
      }
    }
    response = requests.request("POST", url, headers=self.header, data=json.dumps(payload)).json()
    print(response)


collector_client = CollectorClient()

if __name__ == '__main__':
  collector_client = CollectorClient()
  collector_client2 = CollectorClient()
  print(id(collector_client))
  print(id(collector_client2))
  user_info = {"ouId": "2320189280760993651"}
  collector_client.query_user_token(user_info)
