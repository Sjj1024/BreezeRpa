import requests

url = "https://www.amazon.com/s?bbn=4&rh=n%3A2578999011%2Cp_n_feature_five_browse-bin%3A2578998011%7C2578999011%2Cp_72%3A1250221011%2Cp_n_feature_nine_browse-bin%3A3291437011%2Cp_n_feature_eight_browse-bin%3A3269847011&s=exact-aware-popularity-rank&dc&page=1&qid=1681623745&rnid=3269843011&ref=sr_pg_3"

payload={}
headers = {
  'authority': 'www.amazon.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
  'cache-control': 'no-cache',
  'cookie': 'aws_lang=cn; regStatus=pre-register; aws-target-data=%7B%22support%22%3A%221%22%7D; session-id=139-5309082-7209250; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:CN"; ubid-main=132-9387470-5266737; session-token="zu4vtXcWCw1lrJ3aySfP1/jpoDf2Ew8XFvStw6gwe4uJZNrJUHSsW5PNmTsOvNXQ2xH5oCA6YQNb1YeZNpUzZiiaV0XzHLcS/e07HnBbc/+U41dqU511Q4DLEseNt3lwpu/pDcd38hjmLffC6H+npVSh68Rtz3hurfSIzH388nIKrdOf9xkjR3ri6FlGnI8APTZh2UTMsNg/96hZREnRQ1YjJP94AnmMPf94mrw9jq8="; csm-hit=tb:BT69CVGQNVH8AY2WWHZT+sa-AADT141AYZ2CQ07XTPYC-KJQ8P4TVTJ8710WJ4Y9C|1681623754662&t:1681623754662&adb:adblk_yes; session-token="6irbHUwJEUi2yhKCJ3j676/tThaGP6kPfbyA7QuTQ8xlHOZzRrwQdoDABFbRm/Izqu2sXvCHxzaP1MMThKoKdfo3SyuBirnH9b+MOFtFLNaJsad1FCkfCKy6uVgDyLXS1orRNXsbln/Xx3OvwGTThbfnriXDx7spb2nwiigs5gg0mrEKZJNxWKn8aipj3VeWs8SQlVHpT83VSwUg6j8KKXmcge2hDG3zTD7HoDXvQ3I="',
  'device-memory': '8',
  'downlink': '1.3',
  'dpr': '1.25',
  'ect': '3g',
  'pragma': 'no-cache',
  'rtt': '350',
  'sec-ch-device-memory': '8',
  'sec-ch-dpr': '1.25',
  'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-ch-ua-platform-version': '"10.0.0"',
  'sec-ch-viewport-width': '1536',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
  'viewport-width': '1536'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
