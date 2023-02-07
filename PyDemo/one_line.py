import requests

url = "https://www.google.com/"

payload={}
headers = {
  'authority': 'www.google.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-language': 'zh-CN,zh;q=0.9,zh-HK;q=0.8,zh-TW;q=0.7',
  'cache-control': 'max-age=0',
  'cookie': 'CONSENT=PENDING+215; SOCS=CAISHwgBEhJnd3NfMjAyMjEwMDUtMF9SQzMaBXpoLUNOIAEaBgiAnoiaBg; SID=SgjXJX1IJMF4yOR45sq3BbXZGbukIIhzXTLOw0M4TJsHCae2e_mO6N4MX0bjLRhwyN_rlg.; __Secure-1PSID=SgjXJX1IJMF4yOR45sq3BbXZGbukIIhzXTLOw0M4TJsHCae2RmdZQTNdx9oJPo8FoO0khg.; __Secure-3PSID=SgjXJX1IJMF4yOR45sq3BbXZGbukIIhzXTLOw0M4TJsHCae2ClcA1M0ZPJZLA8qTdCpOrw.; HSID=A3ITUjpoj6Dk0U9dx; SSID=A2J_JE0PE9nW6aLZ2; APISID=fIEGLhP16GGl3Xvm/AQiDHnyUNWmd3Akie; SAPISID=Ec2wYqZZ-khUnWIF/A3XNP21dAEMej-EtG; __Secure-1PAPISID=Ec2wYqZZ-khUnWIF/A3XNP21dAEMej-EtG; __Secure-3PAPISID=Ec2wYqZZ-khUnWIF/A3XNP21dAEMej-EtG; OTZ=6851656_24_24__24_; SEARCH_SAMESITE=CgQIu5cB; 1P_JAR=2023-02-03-08; AEC=ARSKqsKbkX8WaLkuh5lSd6rVTxJ-apgImltqAfQI8QAfrg8m16fplKv9Uw; NID=511=drgQkwULtqPgPeiYZBRwV_L2VJvLVQp9kVWIUMgupVxpGu5cYlp104akzy5zIh4dRVzOI6pFuwjPEnBn4gNSjJ1nT6RZLTDrfbYR9hejVkSsFBS1hbQL75RVOwsi_mWpW7p4ULPWuTZbequZ6wGeT-en2r9ZkvaKle29I4T0hUSjPMOa5bRUCiQT75pC4bqd_lqL3bKb3F3pNtCCDvh8R-k3xvnafhbCPNlMX9XWzTi6WMLpyzRuEWLl0ITbmeRZXQ; SIDCC=AFvIBn99p2MGYHL79PREhK846jL08y0jh78swrUFW4I2PsHV1pUte0XA1rQbd-wZBRuna5iRRA; __Secure-1PSIDCC=AFvIBn-LGC8OSrw9lP7W1QkoUYSTgHXgEWnyjHo8MTNg3EfO7HMBvgUAGdK39pUuRivB1h6dOlI; __Secure-3PSIDCC=AFvIBn92-aaErenifPD1NG95969BVHUN1hcn9O5GkjRhZySQVwwlgD0oWG8AGdRCHsfzRZLf1g; 1P_JAR=2023-02-03-08; SIDCC=AFvIBn-7VEtn8G46ANtp5TG3kASByu2QkjyeMAEPccJyEegUdrDOeQwXbEa6ECmmhZk0LJd5Gg; __Secure-1PSIDCC=AFvIBn9M4AoeR0He1d-grQuxEFtqSH9hK2spojahVOnWcEhAPGye8x4WlOLICJU5Tx6RMhQgAuU; __Secure-3PSIDCC=AFvIBn-qaQ_ZyyXTqfvHse3MaI9fXNwyr9K7xQ59CeM9lKOf7AX72v3-4xBTsdKd81VRbe5Cvg',
  'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
  'sec-ch-ua-arch': '"x86"',
  'sec-ch-ua-bitness': '"64"',
  'sec-ch-ua-full-version': '"109.0.5414.120"',
  'sec-ch-ua-full-version-list': '"Not_A Brand";v="99.0.0.0", "Google Chrome";v="109.0.5414.120", "Chromium";v="109.0.5414.120"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-model': '""',
  'sec-ch-ua-platform': '"Windows"',
  'sec-ch-ua-platform-version': '"10.0.0"',
  'sec-ch-ua-wow64': '?0',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
  'x-client-data': 'CJO2yQEIorbJAQjBtskBCKmdygEI0ebKAQiUocsBCPGCzQEI/YfNAQjeic0BCPGJzQEI9orNAQjwi80BCIuMzQEI2IzNAQjHjc0BCNLhrAI='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
