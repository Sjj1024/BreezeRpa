import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
from bs4 import BeautifulSoup


def get_img_links(url):
    payload = {}
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
    html = response.content.decode()
    # print(html)
    soup = BeautifulSoup(html, "lxml")
    title_span = soup.select("span#thread_subject")
    title = title_span[0].get_text()
    title = title.replace("【", "").replace("】", "").replace("|", "")
    image_tags = soup.select("img.zoom")
    image_links = []
    for img in image_tags:
        img_link = img.get("file")
        image_links.append(img_link)
    print(f"title: {title}, images: {len(image_links)}")
    return title, image_links


def down_load_imgs(title, imgs):
    print("开始下载图片")
    path = os.path.join(os.getcwd(), "自拍套图", title)
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print(f"已经存在:{title}")
        return
    threadpool = ThreadPoolExecutor(max_workers=20)
    task_list = []
    for index, img_url in enumerate(imgs):
        print(f"开始下载标题：{title},图片链接是{img_url}")
        image_type = img_url.split(".")[-1]
        image_name = f"{index + 1}.{image_type}"
        task_list.append(threadpool.submit(down_jpg, path, img_url, image_name))
    for future in as_completed(task_list):
        name = future.result()
        print(f"name: {name}已下载完成")


def down_jpg(path, img_url, image_name):
    # 开始下载图片
    print(f"开始下载图片{image_name}-------->")
    res = requests.get(img_url)
    if res.status_code == 404:
        print(f"图片{img_url}下载出错------->")
    img_name = os.path.join(path, image_name)
    with open(img_name, "wb") as f:
        f.write(res.content)
    print(f"图片{image_name}下载完成--------->")
    return image_name


def run():
    url = "https://www.djsd997.com/thread-1105248-1-1.html"
    title, image_links = get_img_links(url)
    down_load_imgs(title, image_links)


if __name__ == '__main__':
    run()
