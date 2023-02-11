import io
import json
import os
import random
import re
import threading
import time
from concurrent.futures.thread import ThreadPoolExecutor
from subprocess import call
import pyperclip
import requests
from PIL import Image
from PIL import ImageGrab, ImageFont, ImageDraw
from bs4 import BeautifulSoup


class Toutiao_picurl():
    def __init__(self, url):
        self.url = url
        self.header = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/83.0.4103.61 Safari/537.36",
            "referer": "https://mp.toutiao.com/profile_v3/graphic/publish",
            "Origin": "https://mp.toutiao.com",
            # "Cookie": "_ga=GA1.2.1838920340.1591889347; __utmz=68473421.1592400213.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=68473421.1838920340.1591889347.1592400213.1592734500.2; tt_webid=6855618365789406728; SLARDAR_WEB_ID=0e3909f6-390f-44d0-9727-09af436760a1; _gid=GA1.2.200393803.1596948295; passport_csrf_token=c0b2df7c7e7e4b99a2d7d6ff6cd0f3fe; s_v_web_id=verify_kdmls7jv_9BX2xa3m_vZzc_4x1D_AIJd_QLy3mQyi4M12; sso_auth_status=801dd1e700f47f2c22c5f80a67c4c6e7; sso_uid_tt=97a2f920d77e2585ccb7abd3682faeb6; sso_uid_tt_ss=97a2f920d77e2585ccb7abd3682faeb6; toutiao_sso_user=7451232a9670d287a611fd84c4c24cfa; toutiao_sso_user_ss=7451232a9670d287a611fd84c4c24cfa; passport_auth_status=d3bc991571cbe17a78247636b02d6a35%2C69b1d85deb0720c4be2547fea32f8d3a; sid_guard=4aa8c025cb0ba0e8976a7fa476fc90d7%7C1596948356%7C5184000%7CThu%2C+08-Oct-2020+04%3A45%3A56+GMT; uid_tt=a5f69c8159558848355015bf72aaf831; uid_tt_ss=a5f69c8159558848355015bf72aaf831; sid_tt=4aa8c025cb0ba0e8976a7fa476fc90d7; sessionid=4aa8c025cb0ba0e8976a7fa476fc90d7; sessionid_ss=4aa8c025cb0ba0e8976a7fa476fc90d7; gftoken=NGFhOGMwMjVjYnwxNTk2OTQ4MzU2NjB8fDAGBgYGBgY; ttcid=560e73f6806a4dbaa94683ce03d0427711; tt_scid=rOW6J.sxx7BszD.wpz14N-z3-KI92pjHwu9FzHd17BRU7zoG9qsTsI2ZOpTATeGGcde5"
            "Cookie": self.get_cookie()
        }
        self.cut_height = 0

    def tt_upload(self, image, img_url):
        """
        将二进制的图片内容上传到头条网站
        :param image:
        :param img_url:
        :return:
        """
        print(f"开始上传图片{img_url}")
        time.sleep(3)
        # jpg_content = {"upfile": ("test1.png", open("test1.png", "rb"))}
        jpg_content = {"upfile": ("test1.png", image)}
        response = requests.post(url=self.url, headers=self.header, files=jpg_content).content.decode("utf-8")
        res_dict = json.loads(response)
        print(f"图片上传完成{img_url}：{res_dict}")
        message = res_dict.get("message")
        web_uri = res_dict.get("origin_web_url")
        if message == "用户未登录":
            raise Exception("cookie不可用")
        if message == "success":
            rel_source = "https://p1.pstatp.com/origin/"
            if web_uri.startswith("http"):
                rel_source = ""
            res_jpg_url = rel_source + web_uri
            print(res_jpg_url)
            return res_jpg_url
            # cmd = 'display notification "'+ res_jpg_url +'" with title "图片上传成功"'
            # call(["osascript", "-e", cmd])
            # html_jpg_tage = '<img src="'+ res_jpg_url +'" width="100%" />'
            # return html_jpg_tage

    def jd_upload(self, image, img_url):
        print("获取京东图床网站链接\n")
        url = "https://image.kieng.cn/upload.html?type=jd"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
            "Referer": "https://image.kieng.cn/jd.html",
            "cookie": "isone=is; Hm_lvt_8948fbcc68dc282165999647dc109378=1635675594; menu=open; Hm_lpvt_8948fbcc68dc282165999647dc109378=1635675760",
            "x-requested-with": "XMLHttpRequest",
            "origin": "https://image.kieng.cn"
        }
        random_num = random.randint(17977, 855765)
        random_i = random.randint(0, 100)
        jpg_content = [
            ('image', (
                'CoUBUmFs7oCAC3akACUsRX0JgBQ580.jpg',
                image,
                'image/jpeg'))
        ]
        data = {'key': '1635675759587',
                'file_id': '0',
                'apiSelect': 'Local'}
        try:
            print("开始发送上传图片请求")
            res = requests.post(url, headers=header, data=data, files=jpg_content)
            rel_str = res.content.decode()
            print(rel_str)
            json_str = json.loads(rel_str)
            jpg_link = json_str["data"]["url"]
            res.close()
            print(jpg_link)
            return jpg_link
        except Exception as e:
            print(e)

    def async_nsaimg_link(self, image, img_url):
        print("获取nsaimg图床网站链接\n")
        url = "https://www.nsaimg.com/upload/upload.html"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
            "Referer": "https://www.nsaimg.com/",
            "cookie": "__cfduid=d243d97546d83e956bf570e56aa04ef691585749351; PHPSESSID=m8679ns7t69nn9l5l70m28l4je",
            "x-requested-with": "XMLHttpRequest",
            "origin": "https://www.nsaimg.com"
        }
        random_num = random.randint(17977, 855765)
        random_i = random.randint(0, 100)
        jpg_content = {"image": (str(random_num), image)}
        data_fileid = str(random_num) + "_" + f"{random_i}.jpg"
        data = {"fileId": (None, data_fileid),
                "initialPreview": [],
                "initialPreviewConfig": [],
                "initialPreviewThumbTags": [],
                }
        try:
            print("开始发送上传图片请求")
            res = requests.post(url, headers=header, data=data, files=jpg_content)
            rel_str = res.content.decode()
            print(rel_str)
            json_str = json.loads(rel_str)
            jpg_link = json_str["data"]["url"]
            res.close()
            print(jpg_link)
            return jpg_link
        except Exception as e:
            print(e)

    def upload_duotu_link(self):
        url = "https://23img.com/application/upload.php"
        payload = {'name': 'ksmehzs6644889.jpg',
                   'uuid': 'o_1gor6k4fk1lia1ra014h1aoi1poaa'}
        files = [
            ('file', ('file', open('/path/to/file', 'rb'), 'application/octet-stream'))
        ]
        headers = {
            'authority': '23img.com',
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9,zh-HK;q=0.8,zh-TW;q=0.7',
            'origin': 'https://23img.com',
            'referer': 'https://23img.com/',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }
        response = requests.request("GET", url, headers=headers, data=payload, files=files)
        print(response.text)

    def async_duotu_link(self, image, img_url="dasfdas.jpg"):
        """
        异步获取头条图床图片链接
        :param jpg_path: 图片路径
        :param jpgs_list: 获取到的图片链接列表
        :return:
        """
        print("获取多图图床网站链接\n")
        url = self.url
        headers = {
            'authority': '23img.com',
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9,zh-HK;q=0.8,zh-TW;q=0.7',
            'origin': 'https://23img.com',
            'referer': 'https://23img.com/',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }
        jpg_content = {"file": (f"{img_url}", image)}
        random_num = random.randint(1000, 900000)
        data = {"name": (None, f"{img_url}random_num.jpg"),
                "uuid": f"o_1feklnhtu122{random_num}t3h5vvhuknrhb"
                }
        try:
            print("开始发送上传图片请求")
            res = requests.post(url, headers=headers, data=data, files=jpg_content)
            rel_str = res.content.decode()
            print(rel_str)
            json_str = json.loads(rel_str)
            jpg_link = json_str["url"]
            res.close()
            print(jpg_link)
            return jpg_link
        except Exception as e:
            print(e)

    def upload_skeing(self, image):
        print("开始上传图片")
        url = self.url
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
            "Referer": self.url
        }
        jpg_name = f"{random.randint(100, 100000000)}.jpg"
        jpg_content = {"file": (jpg_name, image)}
        data_fileid = "399312_" + jpg_name
        data = {"name": f"CoUBXmFs7wGALWjiABs{data_fileid}",
                "uuid": "o_1flblph2c1f1o5j315ge3ha10ola"
                }

        res = requests.post(url, headers=header, data=data, files=jpg_content).json()
        # print(res)
        result = res.get("result")
        if result == "success":
            res_jpg_url = res.get("url")
            print(res_jpg_url)
            return res_jpg_url
        else:
            print(res)

    def get_cookie(self):
        # 获取cookie
        cookie_path = os.path.join(self.get_path(), "cookie.txt")
        print(cookie_path)
        with open(cookie_path, "r") as f:
            data = f.read()
        return data

    def save_cookie(self, cookie):
        # 保存cookie
        cookie_path = os.path.join(self.get_path(), "cookie.txt")
        with open(cookie_path, "w") as f:
            f.write(cookie)

    def get_path(self):
        return os.path.abspath('.')  # 否则使用原本路径

        # if getattr(sys, 'frozen', False):  # 如果是exe状态，sys会有frozen属性，
        #     pathname = sys._MEIPASS  # 当处于冻结状态，也就是exe状态的时候，使用这个路径
        # else:
        #     pathname = os.path.abspath('.')  # 否则使用原本路径
        # return pathname

    # image: 图片  text：要添加的文本 font：字体
    def add_text_to_image(self, image, text):
        rgba_image = image.convert('RGBA')
        text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
        image_draw = ImageDraw.Draw(text_overlay)
        # 设置字体大小和图片成比例
        y = rgba_image.size[1]
        print(f"图片的宽是{y}")
        if y > 1200:
            font_size = 36
        elif y > 860:
            font_size = 34
        elif y > 480:
            font_size = 30
        else:
            font_size = 26
        print(f"字体尺寸是{font_size}")
        font = ImageFont.truetype('/Library/Fonts/Arial Unicode.ttf', font_size)
        text_size_x, text_size_y = image_draw.textsize(text, font=font)
        # 设置文本文字位置
        # print(rgba_image)
        text_xy = (rgba_image.size[0] - text_size_x - 20, rgba_image.size[1] - text_size_y - 20)
        # 设置文本颜色和透明度
        image_draw.text(text_xy, text, font=font, fill=(255, 255, 255, 255))
        # image_draw.text(text_xy, text, font=font, fill=(227, 62, 51, 180))
        image_with_text = Image.alpha_composite(rgba_image, text_overlay)
        return image_with_text

    def run(self):
        print("监听剪切板程序开始运行中...")
        add_flag = input("是否添加水印？1：添加  2：不添加\n")
        while True:
            img = ImageGrab.grabclipboard()
            if isinstance(img, Image.Image):
                # 先讲图片保存到本地
                # img.save('test1.png', 'png')
                # 添加1024水印过程
                if add_flag == "1":
                    img = self.add_text_to_image(img, "1024shen.com")
                # 模拟图床图片过程，将上传后返回的图片url返回到剪切板中
                picture_url = None
                while picture_url is None:
                    try:
                        # 将图片转成二进制流
                        imgByteArr = io.BytesIO()
                        img.save(imgByteArr, format='PNG')  # format: PNG / JPEG
                        imgByteArr = imgByteArr.getvalue()
                        # picture_url = self.upload(imgByteArr)
                        picture_url = self.async_duotu_link(imgByteArr)
                    except Exception as e:
                        print(e)
                        cookie = input("cookie不可用，请输入新Cookie：\n")
                        self.header["Cookie"] = cookie
                        self.save_cookie(cookie)
                pyperclip.copy(picture_url)
                spam = pyperclip.paste()
                print("图片上传成功，已将url复制到剪切板")
            time.sleep(0.1)


lock = threading.Lock()


def find_img_urls(html_str):
    urls_img = re.findall(r'<img.*?file="(.*?)"', html_str)
    urls_img = [i for i in urls_img if i.startswith("http")]
    urls_img = [i for i in urls_img if not i.endswith("html")]
    urls_img = [i for i in urls_img if not i.endswith("gif")]
    urls_img = [i for i in urls_img if "face" not in i]
    urls_img = [i for i in urls_img if not i.startswith("https://23img")]
    urls_img = [i for i in urls_img if not i.startswith("http://skeimg")]
    urls_img = [i for i in urls_img if not i.startswith("https://vxotu.com")]
    urls_img = [i for i in urls_img if not i.startswith("https://s1.xoimg.com")]
    urls_img = set(urls_img)
    print(urls_img)
    imgs_unm = len(urls_img)
    count_upload = []
    executor = ThreadPoolExecutor(max_workers=10)
    for i in urls_img:
        executor.submit(down_upload_img, i, count_upload, urls_img)
        # t = threading.Thread(target=down_upload_img, args=(i, count_upload))
        # t.start()
        # down_upload_img(i, count_upload)
    # print(html_str)
    while True:
        print(f"正在等待替换图片，当前已替换：{len(count_upload)},总的图片数：{imgs_unm}")
        # print("11111111111111111111")
        # print(htmls)
        write_html_str(htmls)
        # print("2222222222222222222222")
        print(f"还剩图片链接是:{urls_img}")
        print(f"还剩图片个数是:{len(urls_img)}")
        # print("33333333333333333333333")
        if len(count_upload) == imgs_unm:
            print("图片全部替换完成")
            # print(htmls)
            filter_html = htmls
            filter_html = re.sub(r"马蜂窝", "", filter_html)
            filter_html = re.sub(r"</?a.*?>", "", filter_html)
            filter_html = re.sub(r"</?video.*?>", "", filter_html)
            filter_html = re.sub(r'class=".*?"', "", filter_html)
            filter_html = re.sub(r'style=".*?"', "", filter_html)
            filter_html = re.sub(r'id=".*?"', "", filter_html)
            filter_html = re.sub(r'data-seq=".*?"', "", filter_html)
            filter_html = re.sub(r'data-pid=".*?"', "", filter_html)
            filter_html = re.sub(r'data-index=".*?"', "", filter_html)
            filter_html = re.sub(r'data-p', "", filter_html)
            filter_html = re.sub(r'&nbsp;', "", filter_html)
            filter_html = re.sub(r'<div data-cs-t="ginfo_kw_hotel"><div></div><div>', "", filter_html)
            write_html_str(filter_html)
            pyperclip.copy(filter_html)
            spam = pyperclip.paste()
            print("图片全部上传成功，已将htmls复制到剪切板")
            cmd = 'display notification "' + "文章替换成功success" + '" with title "文章替换成功"'
            # call(["osascript", "-e", cmd])
            break
        time.sleep(2)


def down_upload_img(img_url, count_upload, urls_img):
    # 下载并上传图片到头条图床
    header = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
        # "cookie":"__cfduid=d7bf56a09d59c63153be646a4240dc5351598684917; _ga=GA1.2.1719031425.1598684863; _gid=GA1.2.742131085.1598684863"
    }
    print(f"开始下载图片{img_url}")
    res = requests.get(img_url, headers=header)
    print(res)
    print(f"图片下载完成{img_url}")
    img_content = res.content
    # 剪切图片，去除98水印
    img = Image.open(io.BytesIO(img_content))
    size = img.size
    width = size[0]
    height = size[1] - toutiao.cut_height
    cropped = img.crop((0, 0, width, height))  # (left, upper, right, lower)
    imgByteArr = io.BytesIO()
    cropped.save(imgByteArr, format='JPEG')
    res = imgByteArr.getvalue()
    # 开始上传到头条
    # picture_url = toutiao.tt_upload(img_content, img_url)
    # picture_url = toutiao.jd_upload(img_content, img_url)
    picture_url = toutiao.async_duotu_link(res, img_url)
    # picture_url = toutiao.upload_skeing(img_content)
    # picture_url = toutiao.async_nsaimg_link(img_content, img_url)
    lock.acquire()
    global htmls
    htmls = htmls.replace(img_url, picture_url)
    count_upload.append(picture_url)
    urls_img.remove(img_url)
    lock.release()


def write_html_str(htmls_str):
    html_res = os.path.join(os.path.split(__file__)[0], "html_res.txt")
    with open(html_res, "w", encoding="utf-8") as f:
        data = f.write(htmls_str)
    return data


def read_html_res_str():
    html_res = os.path.join(os.path.split(__file__)[0], "html_res.txt")
    with open(html_res, "r", encoding="utf-8") as f:
        data = f.read()
    return data


def read_html_str(url):
    payload = {}
    headers = {
        'authority': 'www.djsd997.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9,zh-HK;q=0.8,zh-TW;q=0.7',
        'cache-control': 'max-age=0',
        'cookie': 'cPNj_2132_saltkey=rAn74F3P; cPNj_2132_lastvisit=1675774221; cPNj_2132_lastfp=66abe79b56fe4d1db0defa055279da8b; cPNj_2132_atarget=1; cPNj_2132_st_t=0%7C1675941723%7Ca1f3e77896f05f6faeee5b1abeb96dbb; cPNj_2132_forum_lastvisit=D_142_1675855944D_125_1675861867D_165_1675861875D_95_1675941563D_154_1675941719D_155_1675941723; cPNj_2132_visitedfid=155D154D95D165D125D142; cPNj_2132_viewid=tid_992050; cPNj_2132_st_p=0%7C1675943535%7C7ebf9161c05f7d405c9f79ace6fea3e2; cPNj_2132_lastact=1675943535%09home.php%09misc; cPNj_2132_lastact=1675946504%09forum.php%09viewthread; cPNj_2132_st_p=0%7C1675946504%7Ce45d44ad73f9968a43b344b00d00599d; cPNj_2132_viewid=tid_1169430; cPNj_2132_visitedfid=95D155D154D165D125D142',
        'referer': 'https://www.djsd997.com/forum-95-1.html',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    html = response.content.decode()
    soup = BeautifulSoup(html, "lxml")
    content = soup.select("div.t_fsz")[0].decode()
    # print(content)
    return content


def write_caoliu_html_str(htmls_str):
    html_res = os.path.join(os.path.split(__file__)[0], "caoliu_html_res.txt")
    with open(html_res, "w", encoding="utf-8") as f:
        data = f.write(htmls_str)
    return data


def clear_content(html: str):
    html = html.replace(' ', "")
    html = re.sub(r'<img +.*?src="data', "[img]", html)
    html = re.sub(r'<img +.*?src="', "[img]", html)
    html = re.sub(r'" alt=.*?>', '>', html)
    html = re.sub(r'" data-src=.*?>', '>', html)
    html = re.sub(r'<.*?>', '', html)
    html = re.sub(r'\S.*?上传', '', html)
    html = re.sub(r' ', '', html)
    html = re.sub(r'	', '', html)
    html = re.sub(r'\n+?', '', html)
    html = re.sub(r'&nbsp;', '', html)
    html = re.sub(r'微信.*?上传', '', html)
    html = re.sub(r'QQ.*?上传', '', html)
    html = re.sub(r'<div class="xs0">.*?</div>', '', html, re.S)
    html = re.sub(r'\[img\]', '\n[img]', html)
    html = re.sub(r'jpg.*?/?>', 'jpg[/img]\n', html)
    html = re.sub(r'\S.*?下载附件', '', html)
    html = re.sub(r'堂', '', html)
    html = re.sub(r'\[img\]st.*?">', '', html)
    html = re.sub(r'static.*?zoomfile="', '', html)
    html = re.sub(r'\[/img\]', '[/img]\n', html)
    html = re.sub(r'\[img\]static.*?>', '', html)
    html = re.sub(r'\[img\]static.*?\]', '', html)
    print(html)
    write_caoliu_html_str(html)


def run(htmls):
    find_img_urls(htmls)
    second_html = read_html_res_str()
    clear_content(second_html)


if __name__ == '__main__':
    url = "https://23img.com/application/upload.php"
    toutiao = Toutiao_picurl(url)
    toutiao.cut_height = 48
    url = "https://www.djsd997.com/forum.php?mod=viewthread&tid=1165797&extra=page%3D1%26filter%3Dtypeid%26typeid%3D712"
    htmls = read_html_str(url)
    run(htmls)
