import requests

url = "https://e94eabc5-e97b-4962-bfc4-106ee31eaf6d.mock.pstmn.io/api/goods"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json())
