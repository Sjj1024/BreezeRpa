import requests

url = "https://zcdsade.cfd/thread-1039093-1-1.html"

payload={}
headers = {
  'authority': 'zcdsade.cfd',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-language': 'zh-CN,zh;q=0.9,zh-HK;q=0.8,zh-TW;q=0.7',
  'cache-control': 'max-age=0',
  'cookie': 'cPNj_2132_saltkey=G8v1t4AN; cPNj_2132_lastvisit=1675770126; cPNj_2132_lastfp=97e80f5f7a17f5dcf6230a6e3d0e202e; cPNj_2132_st_t=0%7C1675773742%7Cd12307e805c94abbb0dbb1d6a83d6ab9; cPNj_2132_atarget=1; cPNj_2132_forum_lastvisit=D_155_1675773742; cPNj_2132_visitedfid=155; cPNj_2132_st_p=0%7C1675773754%7C58e08a5c2eb8dd005ed05a958c165531; cPNj_2132_viewid=tid_1039093; cPNj_2132_lastact=1675774086%09forum.php%09ajax; cPNj_2132_lastact=1675774132%09forum.php%09viewthread; cPNj_2132_st_p=0%7C1675774132%7Ca9a2317a6a920606f35aadf6e25e2fde; cPNj_2132_viewid=tid_1039093',
  'referer': 'https://zcdsade.cfd/forum-155-1.html',
  'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
