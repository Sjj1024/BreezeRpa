import hashlib
import time
import uuid


class AuthApi:
  environment = None
  url = None
  token = None
  client_key= ''
  client_secret=''

  @staticmethod
  def setEnvironment(environment, token=None):
    AuthApi.environment = environment

    if environment == "production":
      AuthApi.url = "https://survey.maicedata.com/public/api"
      AuthApi.client_key = ""
      AuthApi.client_secret = ""

    elif environment == "staging":
      AuthApi.url = "https://survey.idatatlas.com/public/api"
      AuthApi.client_key = ""
      AuthApi.client_secret = ""

    elif environment == "yajule_test":
      AuthApi.url = "https://abctest.agile.com.cn/public/api"
      AuthApi.client_key = "b853be07-2447-4a85-be2b-5d2343c3de71"
      AuthApi.client_secret = "6e47a21979194aea8f793bd151ce3478"
    else:
      raise Exception("环境设置错误")

    if token is not None:
      AuthApi.token = token
      AuthApi.url = AuthApi.url.replace("/public", "")

    if token is None and (AuthApi.client_key is None or AuthApi.client_secret is None):
      raise Exception("请设置token 或者 client_key, client_secret")

  @staticmethod
  def getAuthorization():
    nonce = uuid.uuid1().__str__().replace("-", "")
    ts = int(time.time())
    rawStr = AuthApi.client_key + AuthApi.client_secret + str(ts) + nonce
    token = hashlib.md5(rawStr.encode("utf-8")).hexdigest()
    print(f"token:{token}")
    authorization = "key=%s&nonce=%s&ts=%s&token=%s" % (AuthApi.client_key, nonce, str(ts), token)
    return authorization

  @staticmethod
  def prepareAuthorization():
    headers = dict()
    headers['Content-Type'] = 'application/json;charset=UTF-8'
    if AuthApi.token is not None:
      headers['authorization'] = AuthApi.token
    else:
      headers['authorization'] = AuthApi.getAuthorization()
    return headers


if __name__ == '__main__':
  AuthApi.setEnvironment('yajule_test')
  print(AuthApi.prepareAuthorization())
