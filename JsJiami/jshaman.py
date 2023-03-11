import requests

url = "https://www.jshaman.com:4430/submit_js_code/"

payload = "js_code=function+get_copyright()%7B%0A++++var+domain+%3D+%22jshaman.com%22%3B%0A++++var+from_year+%3D+2017%3B%0A++++var+copyright+%3D+%22(c)%22+%2B+from_year+%2B+%22-%22+%2B+(new+Date).getFullYear()+%2B+%22%2C%22+%2B+domain%3B%0A++++return+copyright%3B%0A%7D%0Aconsole.log(get_copyright())%3B%0A&vip_code=free"
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-HK;q=0.8,zh-TW;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://jshaman.com',
    'Referer': 'https://jshaman.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.json().get("content"))
