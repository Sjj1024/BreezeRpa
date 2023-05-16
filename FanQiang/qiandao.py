import requests

url = "https://w1.v2free.net/user/checkin"

payload = {}
headers = {
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'Origin': 'https://w1.v2free.net',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://w1.v2free.net/user',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-HK;q=0.8,zh-TW;q=0.7',
    'Cookie': '_ga=GA1.1.1130830921.1644741062; _gcl_au=1.1.335633402.1644741334; crisp-client%2Fsession%2Fa47ae3dd-53d8-4b15-afae-fb4577f7bcd0=session_bd5ca053-887c-40f1-bc91-13ff24abe1ee; uid=37899; email=2950525265%40qq.com; key=5426124ed2a3c4e2a7037d1fd03b765aaf21b780c669d; ip=0de1524ebf2239f624bb860f05af551b; expire_in=1650940365; _ga_NC10VPE6SR=GS1.1.1648348255.8.1.1648348498.0'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
