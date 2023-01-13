import ddddocr
import requests

url = "https://cl.7801x.xyz/require/codeimg.php"
payload={}
headers = {
  'authority': 'cl.7801x.xyz',
  'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
  'accept-language': 'zh-CN,zh;q=0.9,zh-HK;q=0.8,zh-TW;q=0.7',
  'cookie': 'PHPSESSID=f90v70mknlmihgb3o8q75jj8sm; 227c9_lastvisit=0%091671197001%09%2Fregister.php%3F; 227c9_lastvisit=0%091671197149%09%2Fregister.php%3F',
  'referer': 'https://cl.7801x.xyz/register.php',
  'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'image',
  'sec-fetch-mode': 'no-cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
response = requests.request("GET", url, headers=headers, data=payload)
with open("test.jpg", "wb") as f:
    f.write(response.content)
ocr = ddddocr.DdddOcr(beta=True)
res = ocr.classification(response.content)
print(res)