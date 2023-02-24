# 加密所有的数据
import base64
import json

import requests
from github import Github

from Huijia.porndude.url_list import cate_list

"""
再分享一个APP，可以自动获取所有网站免翻地址，并过滤广告：
下载链接：[url]https://wwi.lanzouf.com/iAVES018a55a[/url]
[img]https://1024shen.com/wp-content/uploads/2022/01/2022011714060442.jpg[/img]

app-user-agent:
Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1
"""

# 我自己的
app_surl = "https://wwd.lanzoue.com/iQeC00912epc"
mazinote = ""

# 别人的：
# app_surl = "https://wwd.lanzouf.com/iPi1V008ix3i"
# mazinote = "需要邀请碼请加QQ:2744701847"

# 丹丹：
# app_surl = "https://wwd.lanzouf.com/i2Bvd02ky29i"
# mazinote = "需要邀请碼请邮箱:caoliushequ2022@163.com"

fenxiang_ma = "分享两个1024邀请码：【f617b*f67e038f1a】【2c*e5ae2e1a55721】"


def read_daohang_html():
    with open("daohang.html", "r", encoding="utf-8") as f:
        return f.read()


# 下面是手机app信息：https://www.cnblogs.com/sdfasdf/p/15019781.html
appInfo = {
    "update": True,
    "version": 3.1,
    "file_path": ".github/hubsql/appHuijia.txt",
    "upcontent": "增加了JavBus和2048地址，修复91论坛地址获取失败问题。升级有问题请加QQ/微信：648133599",
    "upurl": app_surl,
    "showmessage": False,
    "message": "这是最新版本，增加了返回按钮",
    "message_url": "",
    "interval": 20,  # 刷贡献的时间间隔/每多少小时刷一次
    "brush_rate": 30,  # 刷贡献的百分比，越大越容易触发刷
    "brush_all": False,  # 是否全部刷，只要是headers里面的，就都刷？
    "more_urls": "https://1024shen.com/gohome.html",  # 更多推荐页面
    "more_html": read_daohang_html(),  # 更多推荐页面
    "headers": "/index.php?u=606071&ext=e869f;/index.php?u=605858&ext=8ba05;/index.php?u=601703&ext=3d887",
    "about": "1.黑料视频可以点右上角用浏览器打开观看，本APP看不了，不知道问题<br>"
             f"2.{fenxiang_ma}<br>"
             "3.隐藏其中一位，不定时分享几个1024码子，用户名用全中文注册！<br>"
             "4.不要用UC/夸克等垃圾国产浏览器，不然你会发现很多网站都会被屏蔽！<br>"
             '5.本APP永久停止更新！愿你安好',
    "header_ms": "这里总有你想看的吧",  # 这是app菜单栏头部
    "header_url": "",  # 点击头部显示的跳转
    "caoliu_url1": "https://cl.5252x.xyz",  # 草榴免翻地址
    "caoliu_url2": "https://cl.5252y.xyz",  # 草榴免翻地址
    "caoliu_url3": "https://cl.5252z.xyz",  # 草榴免翻地址
    "article_ad": "",
    "commit_ad": "",  # 草榴评论区广告，支持html
    "porn_video_url": "https://f0310.91p48.com/index.php",  # 91视频地址
    "porn_video_1ad": "",
    "porn_video_2ad": "",
    "porn_video_3ad": "",
    "porn_video_4ad": "",
    "porn_video_5ad": "",
    "porn_video_6ad": "",
    "porn_video_footer": "",
    "porn_image_url": "https://t0328.wonderfulday27.live/index.php",  # 91图片区地址
    "porn_photo_header": "",
    "porn_photo_header2": "",
    "porn_photo_footer": "",
    "porn_photo_wentou": "",
    "heiliao_url1": "https://zztt40.com/",  # 黑料免翻地址
    "heiliao_url2": "https://zztt41.com/",  # 黑料免翻地址
    "heiliao_url3": "https://zztt42.com/",  # 黑料免翻地址
    "heiliao_header": "",
    "heiliao_footer": "",
    "heiliao_artical": "",
    "mazinote": mazinote,
    "sehuatang1": "https://dsadsfgd.art",
    "sehuatang2": "https://www.dkd644.com",
    "sehuatang3": "https://www.djsd997.com",
    "javbus1": "https://www.seejav.pw",
    "javbus2": "https://www.busjav.fun",
    "javbus3": "https://www.javsee.club",
    "luntan20481": "https://4s.aaa567.com/2048/",
    "luntan20482": "https://3q.gouxie8.com/2048/",
    "luntan20483": "https://lsp.souaiqin.com/2048/"
}

## 下面是exe程序的信息：https://www.cnblogs.com/sdfasdf/p/15266773.html
exeInfo = {
    "update": True,
    "version": 6.3,
    "file_path": ".github/hubsql/exeHuijia.txt",
    "upcontent": "修复分享手机APP的链接过期问题，升级有问题请加微信：sxsuccess",
    "upurl": "https://wwx.lanzoui.com/iKII9w8zcre",
    "appurl": app_surl,
    "showmessage": False,
    "message": f"{fenxiang_ma}隐藏其中一位，也可以直接购买哦",
    "headers": "/index.php?u=585098&ext=ba2d3;/index.php?u=589569&ext=bf7f6;",
    "about": "1024老司机带你回家啊，上车请滴滴我：1024xiaoshen@gmail.com",
    "weixinxin": "sxsuccess",
    "weiphoto": "photo",
    "mazinote": "需要邀请码才可以注册哦!",
}

# 以下是1024回家插件的数据信息
chrome_extension = {
    "name": "Chrome浏览器1024回家插件",
    "file_path": ".github/hubsql/chromHuijia.txt",
    "version": "0.0.1",
    "dialog": {
        "show": False,
        "content": "这是弹窗信息"
    },
    "update": {
        "show": False,
        "content": "更新了更高级的信息",
        "url": "http://www.jsons.cn/base64/"
    },
    "data": {
        "navigation": cate_list
    }
}


def encode_json(info):
    jsonStr = json.dumps(info)
    b_encode = base64.b64encode(jsonStr.encode("utf-8"))
    bs64_str = b_encode.decode("utf-8")
    realContent = f"VkdWxlIGV4cHJlc3Npb25z{bs64_str}VkdWxlIGV4cHJlc3Npb25z"
    print(f"加密结果:\n{realContent}")
    return realContent


def decode_bs64(content):
    content = content.replace("VkdWxlIGV4cHJlc3Npb25z", "")
    info_str = base64.b64decode(content).decode("utf-8")
    json_info = json.loads(info_str)
    print(f"解密结果:{json_info}")


def creat_chrome_file():
    # using an access token
    GIT_TOKEN = "ghp_888grzs67MqxbZUH3wmIFKzecaKB0cTLy3ICBkl".replace("888", "")
    g = Github(GIT_TOKEN)
    repo = g.get_repo("Sjj1024/Sjj1024")
    res = repo.create_file(".github/hubsql/user.sql", "添加一个新文件", "这是数据库")
    print(res)


def creat_new_file(content):
    # using an access token
    GIT_TOKEN = "ghp_888grzs67MqxbZUH3wmIFKzecaKB0cTLy3ICBkl".replace("888", "")
    g = Github(GIT_TOKEN)
    repo = g.get_repo("Sjj1024/Sjj1024")
    res = repo.create_file(".github/hubsql/chromHuijia.txt", "添加一个新文件", content)
    print(res)


def update_file_content(content):
    print(f"更新文件内容.....")
    # 现获取文件sha
    GIT_TOKEN = "ghp_888grzs67MqxbZUH3wmIFKzecaKB0cTLy3ICBkl".replace("888", "")
    url = "https://api.github.com/repos/Sjj1024/Sjj1024/contents/.github/hubsql/chromHuijia.txt"
    payload = {}
    headers = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    sha = response.json().get("sha")
    g = Github(GIT_TOKEN)
    repo = g.get_repo("Sjj1024/Sjj1024")
    res = repo.update_file(".github/hubsql/chromHuijia.txt", "更新插件内容", content, sha)
    print(res)


def creat_update_file(path, content, commit=""):
    print("判断文件是否存在，存在就更新，不存在就增加")
    GIT_TOKEN = "ghp_888grzs67MqxbZUH3wmIFKzecaKB0cTLy3ICBkl".replace("888", "")
    url = f"https://api.github.com/repos/Sjj1024/Sjj1024/contents/{path}"
    payload = {}
    headers = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    sha = response.json().get("sha", None)
    g = Github(GIT_TOKEN)
    repo = g.get_repo("Sjj1024/Sjj1024")
    if sha:
        res = repo.update_file(path, "更新插件内容", content, sha)
        print(f"更新文件结果:{res}")
    else:
        res = repo.create_file(path, "添加一个新文件", content)
        print(f"添加文件结果:{res}")


def get_gitsql_content():
    GIT_TOKEN = "ghp_888grzs67MqxbZUH3wmIFKzecaKB0cTLy3ICBkl".replace("888", "")
    g = Github(GIT_TOKEN)
    repo = g.get_repo("Sjj1024/Sjj1024")
    res = repo.get_contents(".github/hubsql/chromHuijia.txt").decoded_content.decode("utf-8")
    res = res.replace("VkdWxlIGV4cHJlc3Npb25z", "")
    print(res)
    info_str = base64.b64decode(res).decode("utf-8")
    json_info = json.loads(info_str)
    print(f"GitHub解密结果:{json_info}")


if __name__ == '__main__':
    content_json = chrome_extension
    # content_json = chrome_extension
    # content_json = appInfo
    file_path = content_json.get("file_path")
    print(f"原始信息:{content_json}")
    content = encode_json(content_json)
    decode_bs64(content)
    creat_update_file(file_path, content)
