import requests


def get_page_content(url):
    # import requests
    #
    # url = "https://book.douban.com/tag/%E5%8E%86%E5%8F%B2?start=60&type=T"

    payload = {}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'll="108296"; bid=uQ904kluqpE; __utmc=30149280; __gads=ID=6c46bffcdbae4b68-228badfecddb0098:T=1679475398:RT=1679475398:S=ALNI_MaeI4EPb0sreW_3tYEEb2Za8ipNFA; __gpi=UID=00000963a5c59f76:T=1679475398:RT=1679475398:S=ALNI_MYgD_lc7PNhhTfLHx1idm85C3nNYg; _vwo_uuid_v2=DEB876097893186CF5B4815027A18E7E4|2811258d05f2bc3e54a941eed9e6f186; __utmc=81379588; viewed="30767820"; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1681628034%2C%22https%3A%2F%2Fsearch.douban.com%2Fbook%2Fsubject_search%3Fsearch_text%3D%25E4%25B8%25B0%25E5%25AD%2590%25E6%2581%25BA%25E5%2584%25BF%25E7%25AB%25A5%25E6%25BC%25AB%25E7%2594%25BB%25E9%259B%2586%26cat%3D1001%22%5D; _pk_ses.100001.3ac3=*; ap_v=0,6.0; __utma=30149280.1184520908.1679369257.1681619827.1681628046.4; __utmz=30149280.1681628046.4.2.utmcsr=market.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt_douban=1; __utma=81379588.1360286923.1681619827.1681619827.1681628046.2; __utmz=81379588.1681628046.2.2.utmcsr=market.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; _pk_id.100001.3ac3=be3b3b3ed3c2df9b.1681619825.2.1681628085.1681619841.; __utmb=30149280.5.10.1681628046; __utmb=81379588.5.10.1681628046',
        'Pragma': 'no-cache',
        'Referer': 'https://book.douban.com/tag/%E5%8E%86%E5%8F%B2?start=40&type=T',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)

    if "人评价)" in response.text:
        print(f"成功: {url}")
    else:
        print(f"失败:{url}")


def run():
    print(f"开始")
    for i in range(1, 1000):
        url = f"https://book.douban.com/tag/%E5%8E%86%E5%8F%B2?start={0 + (i-1) * 20}&type=T"
        get_page_content(url)


if __name__ == '__main__':
    run()
