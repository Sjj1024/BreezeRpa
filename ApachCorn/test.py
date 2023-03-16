from bs4 import BeautifulSoup
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Referer': 'https://mlr.lanzoul.com'}
shareUrl = 'https://mlr.lanzoul.com/iDNVx0l76tih'
shareHtml = requests.get(shareUrl, headers=headers)
shareHtml = BeautifulSoup(shareHtml.content, "lxml")
jumpUrl = 'https://mlr.lanzoul.com' + shareHtml.find_all('iframe', class_='ifr2')[0]['src']
jumpHtml = requests.get(jumpUrl, headers=headers)
sign = re.search('[0-9a-zA-Z\_]{20,1000}', jumpHtml.text)
json = requests.post('https://lanzous.com/ajaxm.php', headers=headers,
                     data={'action': 'downprocess', 'sign': sign.group(), 'ves': '1'}).json()
downUrl = json['dom'] + '/file/' + json['url']
print(downUrl)
