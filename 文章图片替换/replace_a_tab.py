# 替换a标签

import re
from concurrent.futures.thread import ThreadPoolExecutor
from subprocess import call
import io
import json
import os
import time
import threading
from PIL import ImageGrab, ImageFont, ImageDraw
from PIL import Image
import pyperclip
import requests

class Toutiao_picurl():
    def __init__(self):
        self.url = "https://mp.toutiao.com/mp/agw/article_material/photo/upload_picture?type=ueditor&pgc_watermark=1&" \
          "action=uploadimage&encode=utf-8"
        self.header = {
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/83.0.4103.61 Safari/537.36",
                "referer": "https://mp.toutiao.com/profile_v3/graphic/publish",
                "Origin":"https://mp.toutiao.com",
                # "Cookie": "_ga=GA1.2.1838920340.1591889347; __utmz=68473421.1592400213.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=68473421.1838920340.1591889347.1592400213.1592734500.2; tt_webid=6855618365789406728; SLARDAR_WEB_ID=0e3909f6-390f-44d0-9727-09af436760a1; _gid=GA1.2.200393803.1596948295; passport_csrf_token=c0b2df7c7e7e4b99a2d7d6ff6cd0f3fe; s_v_web_id=verify_kdmls7jv_9BX2xa3m_vZzc_4x1D_AIJd_QLy3mQyi4M12; sso_auth_status=801dd1e700f47f2c22c5f80a67c4c6e7; sso_uid_tt=97a2f920d77e2585ccb7abd3682faeb6; sso_uid_tt_ss=97a2f920d77e2585ccb7abd3682faeb6; toutiao_sso_user=7451232a9670d287a611fd84c4c24cfa; toutiao_sso_user_ss=7451232a9670d287a611fd84c4c24cfa; passport_auth_status=d3bc991571cbe17a78247636b02d6a35%2C69b1d85deb0720c4be2547fea32f8d3a; sid_guard=4aa8c025cb0ba0e8976a7fa476fc90d7%7C1596948356%7C5184000%7CThu%2C+08-Oct-2020+04%3A45%3A56+GMT; uid_tt=a5f69c8159558848355015bf72aaf831; uid_tt_ss=a5f69c8159558848355015bf72aaf831; sid_tt=4aa8c025cb0ba0e8976a7fa476fc90d7; sessionid=4aa8c025cb0ba0e8976a7fa476fc90d7; sessionid_ss=4aa8c025cb0ba0e8976a7fa476fc90d7; gftoken=NGFhOGMwMjVjYnwxNTk2OTQ4MzU2NjB8fDAGBgYGBgY; ttcid=560e73f6806a4dbaa94683ce03d0427711; tt_scid=rOW6J.sxx7BszD.wpz14N-z3-KI92pjHwu9FzHd17BRU7zoG9qsTsI2ZOpTATeGGcde5"
                "Cookie": self.get_cookie()
            }

    def upload(self, image):
        # print(f"开始上传图片{image}")
        print("开始上传图片")
        # jpg_content = {"upfile": ("test1.png", open("test1.png", "rb"))}
        jpg_content = {"upfile": ("test1.png", image)}
        response = requests.post(url=self.url, headers=self.header, files=jpg_content).content.decode("utf-8")
        res_dict = json.loads(response)
        message = res_dict.get("message")
        web_uri = res_dict.get("origin_web_uri")
        if message == "用户未登录":
            raise Exception("cookie不可用")
        if message == "success":
            rel_source = "https://p1.pstatp.com/origin/"
            res_jpg_url = rel_source + web_uri
            print(res_jpg_url)
            return res_jpg_url
            # cmd = 'display notification "'+ res_jpg_url +'" with title "图片上传成功"'
            # call(["osascript", "-e", cmd])
            # html_jpg_tage = '<img src="'+ res_jpg_url +'" width="100%" />'
            # return html_jpg_tage

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
                        picture_url = self.upload(imgByteArr)
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
    filter_html = re.sub(r"</?a.*?>", "", html_str)
    print(filter_html)
    print("a标签全部替换完成")
    pyperclip.copy(filter_html)
    spam = pyperclip.paste()
    print("图片全部上传成功，已将htmls复制到剪切板")
    cmd = 'display notification "' + "文章替换成功success" + '" with title "文章替换成功"'
    call(["osascript", "-e", cmd])


def read_html_str():
    # 读取txt中的文本作为数据源
    # 获取cookie
    cookie_path = os.path.join(os.path.split(__file__)[0], "html_str.txt")
    print(cookie_path)
    with open(cookie_path, "r") as f:
        data = f.read()
    return data

def run():
    find_img_urls(htmls)


if __name__ == '__main__':
    toutiao = Toutiao_picurl()
    htmls = read_html_str()
    run()
