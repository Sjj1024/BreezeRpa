import queue
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

    def upload(self, image, img_url):
        # print(f"开始上传图片{image}")
        print(f"开始上传图片{img_url}")
        time.sleep(3)
        # jpg_content = {"upfile": ("test1.png", open("test1.png", "rb"))}
        jpg_content = {"upfile": ("test1.png", image)}
        response = requests.post(url=self.url, headers=self.header, files=jpg_content, timeout=5).content.decode("utf-8")
        res_dict = json.loads(response)
        print(f"图片上传完成{img_url}：{res_dict}")
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
    def add_text_to_image(self, images, text):
        image = Image.open(images)
        rgba_image = image.convert('RGBA')
        text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
        image_draw = ImageDraw.Draw(text_overlay)
        # 设置字体大小和图片成比例
        y = rgba_image.size[1]
        print(f"图片的宽是{y}")
        if y > 1200:
            font_size = 30
        elif y > 860:
            font_size = 26
        elif y > 480:
            font_size = 22
        else:
            font_size = 18
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


lock = threading.Lock()
q = queue.Queue(100)

def down_upload_img(img_url):
    # 下载并上传图片到头条图床
    header = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
        "cookie":"__cfduid=d7bf56a09d59c63153be646a4240dc5351598684917; _ga=GA1.2.1719031425.1598684863; _gid=GA1.2.742131085.1598684863"
    }
    print(f"开始下载图片{img_url}")
    res = requests.get(img_url, headers=header, timeout=5)
    print(f"图片下载完成{img_url}")
    img_content = res.content
    img_content = toutiao.add_text_to_image(img_content, "1024shen.com")
    # 开始上传到头条
    picture_url = toutiao.upload(img_content, img_url)
    lock.acquire()
    global htmls
    htmls = htmls.replace(img_url, picture_url)
    lock.release()
    q.task_done()

def read_html_str():
    # 读取txt中的文本作为数据源
    # 获取cookie
    cookie_path = os.path.join(os.path.split(__file__)[0], "html_str.txt")
    print(cookie_path)
    with open(cookie_path, "r") as f:
        data = f.read()
    return data

def product_imgurl(html_str):
    urls_img = re.findall(r'<img.*?src="(.*?)"', html_str)
    print(urls_img)
    for i in urls_img:
        if i.endswith("html") or not i.startswith("http"):
            continue
        else:
            q.put(i)

def consume_uplod():
    executor = ThreadPoolExecutor(max_workers=10)
    while not q.empty():
        image_url = q.get()
        down_upload_img(image_url)
        # q.task_done()
        # executor.submit(down_upload_img, image_url)
    print("图片全部替换完成")
    print(htmls)
    filter_html = re.sub(r"</?a.*?>", "", htmls)
    pyperclip.copy(filter_html)
    spam = pyperclip.paste()
    print("图片全部上传成功，已将htmls复制到剪切板")
    cmd = 'display notification "' + "文章替换成功success" + '" with title "文章替换成功"'
    call(["osascript", "-e", cmd])

def run():
    t_product = threading.Thread(target=product_imgurl, args=(htmls, ))
    t_consume = threading.Thread(target=consume_uplod)
    t_product.start()
    t_consume.start()



if __name__ == '__main__':
    add_flag = input("是否添加水印？1：添加  2：不添加\n")
    toutiao = Toutiao_picurl()
    htmls = read_html_str()
    run()
