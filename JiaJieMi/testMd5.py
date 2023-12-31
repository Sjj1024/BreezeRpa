import requests
import json
import hashlib
import time


def get_md5(string):
    md5_hash = hashlib.md5()
    md5_hash.update(string.encode("utf-8"))
    return md5_hash.hexdigest()


def post_encode():
    url = "https://dev.hado-official.cn/service_api/user_status"
    payload = {
        'uuid': 'ccc37680-9d5b-11ee-8caa-239d574080e1',
        'status': '0'
    }
    # timestamp = int(time.time())
    timestamp = "1703577664"
    ip = "218.79.126.29"
    jsonStr = json.dumps(payload)
    string = f"{ip}{timestamp}{jsonStr}MeleapHado"
    print(f"时间戳: {timestamp}")
    print(f"加密字符串: {string}")
    md5_value = get_md5(string)
    print(f"加密md5： {md5_value}")
    payload["singkey"] = md5_value
    payload["timestamp"] = timestamp
    headers = {
        'Authorization': 'ccc37680-9d5b-11ee-8caa-239d574080e1/14fa48d6b8685315f933755c7f35f61a',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.content.decode())
    print(response.json())


def get_encode():
    print("get请求加密处理")
    url = "https://dev.hado-official.cn/service_api/get_crmauth?page=1&limit=10"

    headers = {
        'Authorization': 'ccc37680-9d5b-11ee-8caa-239d574080e1/77a7ce37406ef278eec497a4d0497500',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)


def main():
    print("执行主流程")
    post_encode()


if __name__ == '__main__':
    main()
