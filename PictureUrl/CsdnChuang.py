import os
import sys

os.chdir(os.path.dirname(os.path.realpath(sys.executable)))  # 这是打包版本的代码

import requests
import re
from threading import Thread
import time
import requests
import http.cookiejar as cookielib
import psutil
import os
from requests_toolbelt import MultipartEncoder

requests.packages.urllib3.disable_warnings()


def is_login():
    session = requests.session()
    try:
        session.cookies = cookielib.LWPCookieJar(filename='.cookie/csdn.txt')
        session.cookies.load()

        url = 'https://me.csdn.net/api/user/show'
        response = session.post(url)
        if response.json()['message'] == "成功":
            return True
        else:
            return False
    except Exception as e:
        return False


def login():
    session = requests.session()
    session.cookies = cookielib.LWPCookieJar(filename='.cookie/csdn.txt')
    response = session.get(
        'https://open.weixin.qq.com/connect/qrconnect?appid=wx0ae11b6a28b4b9fc&scope=snsapi_login&redirect_uri=https%3A%2F%2Fpassport.csdn.net%2Fv1%2Fregister%2FpcAuthCallBack%3FpcAuthType%3Dweixin&state=csdn&login_type=jssdk&self_redirect=default&style=white&href=https://csdnimg.cn/release/passport/history/css/replace-wx-style.css',
        verify=False)
    uuid = re.findall('<img class="qrcode lightBorder" src="(.*?)" />', response.text)[0]
    img_url = 'https://open.weixin.qq.com' + uuid
    imgData = session.get(img_url).content
    with open("qrcode.jpg", "wb") as f:
        f.write(imgData)
    os.popen("qrcode.jpg")

    uuid = uuid.split('/')[-1]
    url = 'https://long.open.weixin.qq.com/connect/l/qrconnect?uuid=' + uuid
    while True:
        response = session.get(url, verify=False)
        code = re.findall("window.wx_code='(.*?)'", response.text)
        if code != ['']:
            for proc in psutil.process_iter():  # 遍历当前process
                try:
                    if proc.name() == "dllhost.exe":
                        proc.kill()  # 关闭该process
                except Exception as e:
                    pass
            break
        time.sleep(1)

    url = 'https://passport.csdn.net/v1/register/pcAuthCallBack?pcAuthType=weixin&code=%s&state=csdn' % code[0]
    session.get(url)
    session.cookies.save()


def updatePicture(picList):
    for pic in picList:
        session = requests.session()
        session.cookies = cookielib.LWPCookieJar(filename='.cookie/csdn.txt')
        session.cookies.load()
        fields = {
            'file': (os.path.basename(pic), open(pic, 'rb'), "image/jpeg"),
        }
        m = MultipartEncoder(fields, boundary='------WebKitFormBoundarynTBa3OWoSMrcVf0F')
        headers = {

            'content-Type': m.content_type,
        }
        url = 'https://blog-console-api.csdn.net/v1/upload/img?shuiyin=2'
        res = session.post(url, headers=headers, data=m, verify=False)
        print(res.json()["data"]["url"])


if __name__ == '__main__':
    if not os.path.exists(".cookie"):
        os.mkdir(".cookie")
    if not os.path.exists(os.path.join(".cookie", "csdn.txt")):
        with open(os.path.join(".cookie", "csdn.txt"), "w") as f:
            f.write("")

    if not is_login():
        login()
    updatePicture(sys.argv[1:])
