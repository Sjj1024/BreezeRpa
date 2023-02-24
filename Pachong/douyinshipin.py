import os
import time
import re
from lxml import etree
import requests
from selenium import webdriver


# 定义函数get_video_ids(author_url),返回UP主全部短视频的ID的列表
# 参数author_url:抖音UP主的主页
# 例如，XXX的主页 https://www.douyin.com/user/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def get_video_ids(author_url):
    ids = list()
    count = 0
    retry = 0
    n = 0
    flag = True
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument('headless')  # 静默模式
    driver = webdriver.Chrome(options=chrome_option)
    driver.get(author_url)
    while flag and retry <= 5:
        driver.execute_script("window.scrollBy(0,2000)")  # scrollBy(x, y)，JavaScript中操作内容滚动指定的像素数
        n = n + 1
        time.sleep(2)
        html_source = driver.page_source
        items = etree.HTML(html_source).xpath("//li[@class='ECMy_Zdt']")
        count_items = len(items)
        print("操作页面内容滚动{0:0>3}次后,获取视频ID{1:0>4}个。".format(n, count_items))
        if count_items != count:
            count = count_items
        else:
            if retry < 5:
                retry = retry + 1
            else:
                flag = False
                print("已经达到可获取视频ID的最大数量,开始逐个获取视频ID:\n")
                for item in items:
                    video_id = item.xpath("a/@href")[0].split("/")[-1]
                    print("获取短视频ID:{}".format(video_id))
                    ids.append(video_id)
    return ids


# 定义函数get_video_info(video_id),返回元组(短视频下载地址,短视频标题)
# 参数video_id:抖音短视频唯一ID
def get_video_info(video_id):
    # 通过url0获取json数据(Chrome浏览器，F12进入开发者模式，模拟手机端，可以看到url0)
    url0 = "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=" + video_id
    r_url0 = requests.get(url0, headers={"user-agent": "Mozilla/5.0"})
    # 获取json数据中的视频地址及视频标题
    url1 = r_url0.json()["item_list"][0]['video']["play_addr"]["url_list.py"][0]
    # 防止出现空标题，加上短视频ID
    title = video_id + "-" + r_url0.json()["item_list"][0]['share_info']["share_title"].split("#")[0].split("@")[0]
    # 获取url1重定向后的真实视频地址
    r_url1 = requests.get(url1, headers={"user-agent": "Mozilla/5.0"}, allow_redirects=False)
    url = r_url1.headers['Location']
    return url, title


# 定义函数get_file_name(string),从字符串中提取合法文件名
def get_file_name(string):
    pattern = re.compile(r'[?*/\\|.:><]')
    txt = re.sub(pattern, '', string)
    return txt


# 定义函数download_video(save_path, url, title),下载并以短视频标题作为文件名保存短视频到指定路径
def download_video(save_path, url, title):
    if os.path.exists(save_path):
        pass
    else:
        os.makedirs(save_path)
    with requests.get(url, headers={"user-agent": "Mozilla/5.0"}, stream=True) as r:
        total_size = int(int(r.headers["Content-Length"]) / 1024 + 0.5)
        file_name = get_file_name(title)
        full_path = save_path + get_file_name(title) + ".mp4"
        with open(file=full_path, mode="wb") as f:
            print('当前下载:【{}】,视频文件大小:【{}KB】'.format(file_name, total_size))
            count = 0
            scale = 50
            start = time.perf_counter()
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)
                count = count + 1
                i = int(scale * (count / total_size))
                a = "=" * i
                b = "." * (scale - i)
                c = (i / scale) * 100
                dur = time.perf_counter() - start
                speed = count / dur
                print("\r下载进度:{0:^3.0f}%[{1:}>{2:}] 耗时:{3:.2f}s 平均下载速度:{4:.2f}KB/S。".format(c, a, b, dur, speed),
                      end="")
            print("\n视频文件下载完毕,存放于:【{0:}】。".format(full_path))


# 定义主程序
def main():
    # 获取UP主全部短视频的ID
    url = "https://www.douyin.com/user/MS4wLjABAAAALqebR_NoLBNj6YeR_byEkXOYTah8iXHMjsBftPDQkz4"
    print("\n获取UP主全部短视频的ID...")
    ids = get_video_ids(url)
    print("获取完毕!共获取短视频ID{}个!".format(len(ids)))

    # 根据短视频ID,批量获取下载地址、短视频标题
    print("\n根据短视频的ID获取短视频的下载地址、标题信息...")
    videos_info = list()
    for video_id in ids:
        video_info = get_video_info(video_id)
        videos_info.append(video_info)
        print("短视频标题:【{0:}】;下载地址:【{1:}】".format(video_info[1], video_info[0]))

    # 批量下载短视频
    print("\n开始批量下载短视频:")
    cwd = os.getcwd()
    path = cwd + "/videos/"
    total = len(videos_info)
    for i in range(total):
        print("\n将下载第【{0:0>4}/{1:0>4}】个短视频:".format(i + 1, total))
        print("=" * 50)
        download_video(path, videos_info[i][0], videos_info[i][1])


if __name__ == "__main__":
    main()