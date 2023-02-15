import os
from concurrent.futures.thread import ThreadPoolExecutor
import requests
from lxml import etree
from bs4 import BeautifulSoup


def down_jpg(title, img_url):
    # 开始下载图片
    path = os.path.join(os.getcwd(), "欧美套图", title)
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print(f"已经存在:{title}")
        return
    name = img_url.split("/")[-1]
    print(f"开始下载图片{name}-------->")
    res = requests.get(img_url)
    if res.status_code == 404:
        print(f"图片{img_url}下载出错------->")
    img_name = os.path.join(path, name)
    with open(img_name, "wb") as f:
        f.write(res.content)
    print(f"图片{name}下载完成--------->")


def get_one_img(one_url):
    print(f"one_url:{one_url}")
    res = requests.get(one_url)
    html = res.content.decode()
    selector = etree.HTML(html)
    title = selector.xpath("//div[2]/div/h1/text()")[0]
    content = selector.xpath("//div/div[3]/div/a/@href")
    threadpool = ThreadPoolExecutor(max_workers=20)
    for img_url in content:
        print(f"开始下载标题：{title},图片链接是{img_url}")
        # down_jpg(title, img_url)
        threadpool.submit(down_jpg, title, img_url)


def page_url(pag_url):
    print(f"pag_url:{pag_url}")
    html = requests.get(pag_url).content.decode()
    selector = etree.HTML(html)
    content = selector.xpath("//div/div[2]/div/a/@href")
    for url in content:
        full_url = f"http://www.picsmetart.com/{url}"
        get_one_img(full_url)


def start_ru():
    # 一共176页
    # page_threadpool = ThreadPoolExecutor(max_workers=10)
    for i in range(1, 176):
        page_i = f"http://www.picsmetart.com/?page={i}"
        page_url(page_i)
        # page_threadpool.submit(page_url, page_i)
    print("所有图片已经下载完了")


if __name__ == '__main__':
    start_ru()
