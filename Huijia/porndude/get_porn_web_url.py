import bs4
import requests


def get_soup(web_path):
    print("获取汤")
    with open(web_path, "r", encoding="utf-8") as f:
        content = f.read()
        soup = bs4.BeautifulSoup(content, "html.parser")
        return soup


def get_url_soup(url):
    # url = "https://theporndude.com/zh/6205/mdr18"
    payload = {}
    headers = {
        'authority': 'theporndude.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,zh-HK;q=0.8,zh-TW;q=0.7',
        'cache-control': 'max-age=0',
        'cookie': '_ga=GA1.1.733819656.1677056778; _ym_uid=1677056779692492959; _ym_d=1677056779; _ym_isad=2; _hjSessionUser_1067239=eyJpZCI6IjMxYTEyM2E3LTRjMjYtNTk1ZS1iYzczLWQ1YTMzZTBmNWFlMyIsImNyZWF0ZWQiOjE2NzcwNTY3Nzg5OTgsImV4aXN0aW5nIjp0cnVlfQ==; _hjIncludedInSessionSample_1067239=0; _hjSession_1067239=eyJpZCI6ImEyMjI0NzA4LWYyMjktNDhmMS1hYWY0LTE4ODNhM2IyOWZlYyIsImNyZWF0ZWQiOjE2NzcwNjgwOTcyMDYsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _ym_visorc=b; _ga_GY2W669H8Q=GS1.1.1677065729.2.1.1677068105.0.0.0',
        'if-modified-since': 'Fri, 27 Jan 2023 21:31:08 GMT',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    print(response.text)
    return bs4.BeautifulSoup(response.text, "html.parser")


def get_url(soup):
    print("提取url")
    main_container = soup.select("#main_container")[0]
    category_container = main_container.select("div.category-container")
    category_dict = {}
    for index, category in enumerate(category_container):
        title = category.select("h2 > a")[0].get_text()
        desc = category.select("div.category-text-block")[0].get_text()
        category_wrapper = category.select("div.category-wrapper > ul > li")
        a_link_list = []
        for link in category_wrapper:
            a_text = link.select("a.link-analytics")[0].get_text().replace(" ", "").replace("\n", "")
            a_link = link.select("a.link-analytics")[0].get("href")
            print(f"标题：{title}, 网站：{a_text}, 链接：{a_link}")
            if "theporndude" in a_link:
                # 需要跳转
                print(f"标题：")
            else:
                # 不需要跳转
                print(f"标题：{title}, 网站：{a_text}, 链接：{a_link}")
                a_link_list.append({"title": a_text, "url": a_link})
        if a_link_list:
            category_dict[str(index)] = {}
            category_dict[str(index)]["title"] = title
            category_dict[str(index)]["data"] = a_link_list
    print(f"最后的结果是:{category_dict}")
    print(f"{category_dict}")


def run():
    print("rin")
    soup = get_soup("PornDude.html")
    get_url(soup)


if __name__ == '__main__':
    run()
