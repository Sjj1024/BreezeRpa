## 2.解析令牌
# 通过JWT解密库，使用公钥对传入的 id_token 进行解密。将公钥以字符串的形式从文件中读取出来，并作为key进行解密：
# // 引入用到的包文件
import json


# // 本例中key_path辅助方法是写在utils工具类中的
import jwt
from jwt.algorithms import RSAAlgorithm
from jwt.utils import force_bytes


def get_user_ifon(id_token):
  try:
    algo = RSAAlgorithm(RSAAlgorithm.SHA256)
    pem_key = open(key_path('D:\pythonDemo\key\public_key_pkc8.pem'), 'r')
    public_key = algo.prepare_key(pem_key.read())
    token_info = jwt.decode(force_bytes(id_token), key=public_key, verify=True)
    user_info = json.loads(json.dumps(token_info))
    username = user_info['sub']
    print(username)
    # 3.判断用户名是否在自己系统存在
    # 4.如果用户存在, 则登录成功，创建业务系统自己的会话，返回登录成功后的页面，略
    # 5.如果参数中有target_url，那么返回此指定url页面
    # 6.否则返回系统默认操作页面
    # 7. 如果用户不存在, 返回登录失败页面, 提示用户不存在
  except Exception as e:
    print(e)
