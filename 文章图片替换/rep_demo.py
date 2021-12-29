import requests

url = "https://image.kieng.cn/upload.html?type=jd"

payload = {'key': '1635675759587',
           'file_id': '0',
           'apiSelect': 'Local'}
files = [
    ('image', (
    'CoUBUmFs7oCAC3akACUsRX0JgBQ580.jpg', open('/Users/jiang/Pictures/CoUBUmFs7oCAC3akACUsRX0JgBQ580.jpg', 'rb'),
    'image/jpeg'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
