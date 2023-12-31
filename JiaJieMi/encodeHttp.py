import requests
import hashlib
import time


def get_md5(string):
    md5_hash = hashlib.md5()
    md5_hash.update(string.encode("utf-8"))
    return md5_hash.hexdigest()


def send(ip, token):
    print("发送数据")
    timestamp = int(time.time())
    string = f"{ip}{timestamp}Hado2023"
    # string = "222.67.121.1671701776573Hado2023"
    md5_value = get_md5(string)
    print(f"时间戳:{timestamp}")
    print(f"MD5动态：", md5_value)
    url = f"https://dev.hado-official.cn/service_api/provider_list?page=1&limit=1&singkey={md5_value}&timestamp={timestamp}"
    headers = {
        'Authorization': token,
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
    }
    response = requests.request("GET", url, headers=headers)
    print(response.json())


def login():
    print("登录")
    url = "https://dev.hado-official.cn/service_auth/login"
    payload = {'login': '15129431397',
               'passwd': '888888'}
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.json())
    return response.json()


def run():
    print("开始运行")
    res = login()
    token = res.get("data").get("token")
    ip = res.get("data").get("ip")
    # ip = "127.0.0.1"
    send(ip, token)


if __name__ == '__main__':
    run()
