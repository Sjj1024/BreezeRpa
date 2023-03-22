# 加密所有的数据
import base64
import json
import requests
from github import Github
from Huijia.porndude.url_list import *

"""
再分享一个APP，可以自动获取所有网站免翻地址，并过滤广告：
下载链接：[url]https://wwi.lanzouf.com/iAVES018a55a[/url]
[img]https://1024shen.com/wp-content/uploads/2022/01/2022011714060442.jpg[/img]

app-user-agent:
Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1
"""

# 我自己的
app_down_url = "https://wwd.lanzoue.com/iQeC00912epc"
exe_down_url = "https://wwd.lanzoue.com/iQeC00912epc"
mazinote = ""

# 别人的：
# app_surl = "https://wwd.lanzouf.com/iPi1V008ix3i"
# mazinote = "需要邀请碼请加QQ:2744701847"

# 丹丹：
# app_surl = "https://wwd.lanzouf.com/i2Bvd02ky29i"
# mazinote = "需要邀请碼请邮箱:caoliushequ2022@163.com"

fenxiang_ma = "分享两个1024邀请码：【f617b*f67e038f1a】【2c*e5ae2e1a55721】"


def read_daohang_html(template):
    with open(f"replace_html/{template}", "r", encoding="utf-8") as f:
        return f.read()


def cao_app_exe_page(html_path):
    with open(f"replace_html/{html_path}", "r", encoding="utf-8") as f:
        content_html = f.read()
        content_html = content_html.replace("""<html>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<body>""", "")
        content_html = content_html.replace("""</body>
</html>""", "")
        return content_html


# 以下是1024回家插件的数据信息
"""
三个地址:
github:https://api.github.com/repos/Sjj1024/Sjj1024/contents/.github/hubsql/chromHuijia.txt
博客园:https://www.cnblogs.com/sdfasdf/p/15115801.html
CSDN:https://xiaoshen.blog.csdn.net/article/details/129345827
"""
chrome_extension = {
    "name": "Chrome1024",
    "file_path": ".github/hubsql/chromHuijia.txt",
    "version": 0.1,
    # 实验功能访问密码
    "password": "521121",
    "dialog": {
        "show": False,
        "content": "这是弹窗信息",
        "url": "http://www.jsons.cn/base64/"
    },
    "update": {
        "show": True,
        "content": "更新了更高级的信息",
        "url": "http://www.jsons.cn/base64/"
    },
    "data": {
        "interval": 1,  # 展示在草榴URL上的贡献链接
        "brush_rate": 100,  # 刷贡献的百分比，越大越容易触发刷
        "brush_all": False,  # 是否全部刷，只要是headers里面的，就都刷？
        "show_hotUrl": True,  # 是否在热门推荐的URl地址中展示
        # 刷贡献的头部，三个地址平均分布一个
        "GongXians": ["/index.php?u=628155&ext=9a511", "/index.php?u=529913&ext=99ea2",
                      "/index.php?u=595394&ext=c180e"],
        # 匹配cookie的规则
        "cookieRule": {"clcookies": "227c9_winduser",
                       "91VideoCookies": "DUID",
                       "91ImgCookies": "CzG_auth",
                       "98cookies": "cPNj_2132_auth"},
        # 更多消息提醒
        "more_info": f"""<div style="color: red;"><span style="color: red;">提示: 部分网站可能需要VPN翻墙后访问</span>，如果你想感谢我，
我的比特币账户：<span style="padding: 0 5px 0 2px;">3HJTSzf2GL7Bj8r7HakUNS1G9jauemk1Lt</span>我的以太坊账户：<span style="padding: 0 5px 0 2px;">0xb9061992ea948e247a4542209c14c5e7ea79afc6</span></div>
        """,
        # 其他回家客户端下载
        "yongjiu": "http://www.jsons.cn/base64/",
        "android": "https://blog.csdn.net/weixin_42565127/article/details/127068694",
        "windows": "https://element.eleme.cn/#/zh-CN/component/container",
        "macbook": "https://antdv.com/components/layout-cn",
        "iphone": "https://antdv.com/components/layout-cn",
        "share": "老司机来了：http://www.jsons.cn/base64/",
        # 购买邀请码功能: 后面再做，先做桌面端
        "open_pay": {
            "open": False,
            "pay_ma": "老司机来了：http://www.jsons.cn/base64/"
        },
        # 过滤广告或者添加广告配置
        "filter_all": {
            "doumei": {
                "filter": False,
                "down": """<a href="https://www.baidu.com/">百度一下</a>"""
            },
            "caoliu": {
                "filter": False,  # 广告开关
                "invcode_info": "1024邀请码:请加微信",
                "article_tip0": "1024邀请码:请加微信0",
                "article_tip1": "1024邀请码:请加微信1",
                "article_tip2": """<a href="https://www.baidu.com/">百度一下1024</a>""",
                "article_tip3": "1024邀请码:请加微信3",
                "article_tip4": "1024邀请码:请加微信4",
                "article_tip5": "1024邀请码:请加微信5",
                "sptable_footer": "1024邀请码:请加微信sptable_footer",
                "article_hd": "1024邀请码:请加微信article_hd",
                "article_ad": "1024邀请码:请加微信article_ad",
                "app_exe_down_page": cao_app_exe_page("caoliu_app_exe_page.html"),
                "appDownNa": """<a href="https://www.baidu.com/" target="_blank">下载91APP</a>""",
            },
            "91video": {
                "filter": False,  # 广告开关
                "invcode_info": "91邀请码:请加微信",
                "page_header_ad": "91屏蔽头部广告",
                "video_header_ad1": "91屏蔽视频头部广告1",
                "video_header_ad2": "91屏蔽视频头部广告2",
                "rightFirstAd": "91侧边栏第一个广告",
                "appDownLiBox": """<a href="https://www.baidu.com/" target="_blank">下载91APP</a>""",
                "iframeBoxsShow": True
            },
            "91image": {
                "filter": False,  # 广告开关
                "invcode_info": "邀请码:91请加微信",
                "app_exe_down_page": cao_app_exe_page("porn_app_down.html"),
                "porn_vip_page": cao_app_exe_page("porn_vip_page.html"),
                "appDownLiBox": """<a href="https://www.baidu.com/" target="_blank">下载91APP</a>""",
            },
            "tang98": {
                "filter": False,  # 广告开关
                "invcode_info": "邀请码:请加微信",
                "headerAd": "98头部广告",
                "footerAd": "98屏蔽页脚底部广告",
                "listFootAd": "98文章列表页底部内容",
                "articleFooterAd": "98文章详情页底部广告",
                "commitAds0": "98评论区广告0",
                "commitAds1": "98评论区广告1",
                "appDownLiBox": """<a href="https://www.baidu.com/" target="_blank">下载98APP</a>""",
            },
            "heiliao": {
                "filter": False,  # 广告开关
                "invcode_info": "邀请码:请加微信",
                "headerAd": "98头部广告",
                "appDownLiBox": """<a class="nav-link" href="/category/1.html">下载黑料APP</a>""",
                "articleLikeAd0": """<a class="nav-link" href="/category/1.html">下载黑料APP0</a>""",
                "articleLikeAd1": """<a class="nav-link" href="/category/1.html">下载黑料APP1</a>""",
                "articleLikeAd2": """<a class="nav-link" href="/category/1.html">下载黑料APP2</a>""",
                "articleLikeAd3": """<a class="nav-link" href="/category/1.html">下载黑料APP3</a>""",
                "articleLikeAd4": """<a class="nav-link" href="/category/1.html">下载黑料APP4</a>""",
                "articleHeaderAd0": """<a class="nav-link" href="/category/1.html">下载黑料APP0</a>""",
                "articleHeaderAd1": """<a class="nav-link" href="/category/1.html">下载黑料APP0</a>""",
                "articleHeaderAd2": """<a class="nav-link" href="/category/1.html">下载黑料APP0</a>""",
                "articleHeaderAd3": """<a class="nav-link" href="/category/1.html">下载黑料APP0</a>""",
                "articleHeaderAd4": """<a class="nav-link" href="/category/1.html">下载黑料APP0</a>""",
                "articleHeaderAd5": """<a class="nav-link" href="/category/1.html">下载黑料APP0</a>""",
                "articleHeaderAd6": """<a class="nav-link" href="/category/1.html">下载黑料APP0</a>""",
                "articleHeaderAd7": """<a class="nav-link" href="/category/1.html">下载黑料APP0</a>""",
                "articleHeaderAd9": """<a class="nav-link" href="/category/1.html">下载黑料APP0</a>""",
            },
            "pornhub": {
                "filter": False,  # 广告开关
                "invcode_info": "邀请码:请加微信",
                "headerAd": "98头部广告",
                "appDownLiBox": """<a class="nav-link" href="/category/1.html">下载黑料APP</a>""",
            },
            "baidu": {
                "filter": False,
                "appDownLiBox": """<a class="nav-link" href="/category/1.html">下载黑料APP</a>"""
            }
        },
        # 导航链接更新时间
        "guide_time": guide_time,
        # 更多导航列表
        "navigation": cate_list
    }
}

# 以下是1024回家跨平台桌面软件
"""
三个地址:
github:https://api.github.com/repos/Sjj1024/Sjj1024/contents/.github/hubsql/deskHuijia.txt
博客园:https://www.cnblogs.com/sdfasdf/p/16101765.html
CSDN:https://xiaoshen.blog.csdn.net/article/details/129388703
"""
desk_platform = {
    "name": "Desk1024",
    "file_path": ".github/hubsql/deskHuijia.txt",
    "version": 0.1,
    # 实验功能访问密码
    "password": "521121",
    "dialog": {
        "show": True,
        "content": "这是弹窗信息",
        "url": "http://www.jsons.cn/base64/"
    },
    "update": {
        "show": True,
        "content": "更新了更高级的信息",
        "url": "http://www.jsons.cn/base64/"
    },
    "data": {
        "interval": 1,  # 展示在草榴URL上的贡献链接
        "brush_rate": 100,  # 刷贡献的百分比，越大越容易触发刷
        "brush_all": False,  # 是否全部刷，只要是headers里面的，就都刷？
        "show_hotUrl": True,  # 是否在热门推荐的URl地址中展示
        # 刷贡献的头部，三个地址平均分布一个
        "GongXians": ["/index.php?u=628155&ext=9a511", "/index.php?u=529913&ext=99ea2",
                      "/index.php?u=595394&ext=c180e"],
        # 更多消息提醒
        "more_info": f"""<div style="color: red;"><span style="color: red;">提示: 部分网站可能需要VPN翻墙后访问</span>，如果你想感谢我，
        我的比特币账户：<span style="padding: 0 5px 0 2px;">3HJTSzf2GL7Bj8r7HakUNS1G9jauemk1Lt</span>我的以太坊账户：<span style="padding: 0 5px 0 2px;">0xb9061992ea948e247a4542209c14c5e7ea79afc6</span></div>
""",
        # 其他回家客户端下载
        "android": "https://blog.csdn.net/weixin_42565127/article/details/127068694",
        "windows": "https://element.eleme.cn/#/zh-CN/component/container",
        "macbook": "https://antdv.com/components/layout-cn",
        "iphone": "https://www.baidu.com/",
        "yongjiu": "http://www.jsons.cn/base64/",
        "share": "老司机带你回家：https://wwd.lanzoue.com/iQeC00912epc，\n浏览器插件：https://wwd.lanzoue.com/iQeC00912epc",
        # 购买邀请码功能: 后面再做，先做桌面端
        "open_pay": {
            "open": False,
            "pay_ma": "老司机来了：http://www.jsons.cn/base64/"
        },
        # 导航链接更新时间
        "guide_time": guide_time,
        # 更多导航列表
        "navigation": cate_list
    }
}


def url_to_html(more_info, is_iphone=False):
    # 先将热门导航里面的内容通过模板写入到daohang.html中
    """
      <div class="tabBox">
        <h3 class="tabTitle">热门推荐</h3>
        <div class="aBox">
          <a href="https://www.baidu.com/" class="alink" target="_blank">百度一下</a>
        </div>
      </div>
    """
    # 提示的内容
    guide_div_str = f"""<div class="guide-time">{guide_time}</div>"""
    tips_div_str = f"""<div class="tips">{more_info}</div>"""
    tab_box_list = [guide_div_str, tips_div_str]
    for key, val in cate_list.items():
        # print(f"{key} : {val}")
        title = val["title"]
        data_url = val["data"]
        a_box_list = []
        for url_a in data_url:
            a_template = f"""<a href="{url_a["url"]}" class="alink" target="_blank">{url_a["title"]}</a>\n"""
            a_box_list.append(a_template)
        a_box_strs = "".join(a_box_list)
        tab_box_template = f"""<div class="tabBox">
            <h3 class="tabTitle">{title}</h3>
            <div class="aBox">
              {a_box_strs}
            </div>
          </div>"""
        tab_box_list.append(tab_box_template)
    tab_box_strs = "".join(tab_box_list)
    daohang_html = read_daohang_html("daohang_app_template.html")
    daohang_html_res = daohang_html.replace("templatePalace", tab_box_strs)
    with open("replace_html/daohang_app_releases.html", "w", encoding="utf-8") as f:
        f.write(daohang_html_res)
    if is_iphone:
        iphone_html = daohang_html_res.replace("""<!DOCTYPE html>
<html lang="zh">""", "").replace("</html>", "")
        return iphone_html
    else:
        return daohang_html_res


def url_to_iphone(more_info, is_iphone=True):
    # 先将热门导航里面的内容通过模板写入到daohang.html中
    """
      <div class="tabBox">
        <h3 class="tabTitle">热门推荐</h3>
        <div class="aBox">
          <a href="https://www.baidu.com/" class="alink" target="_blank">百度一下</a>
        </div>
      </div>
    """
    # 提示的内容
    guide_div_str = f"""<div class="guide-time">{guide_time}</div>"""
    tips_div_str = f"""<div class="tips">{more_info}</div>"""
    tab_box_list = [guide_div_str, tips_div_str]
    for key, val in cate_list.items():
        # print(f"{key} : {val}")
        title = val["title"]
        data_url = val["data"]
        a_box_list = []
        for url_a in data_url:
            a_template = f"""<a href="{url_a["url"]}" class="alink" target="_blank">{url_a["title"]}</a>\n"""
            a_box_list.append(a_template)
        a_box_strs = "".join(a_box_list)
        tab_box_template = f"""<div class="tabBox">
                <h3 class="tabTitle">{title}</h3>
                <div class="aBox" >
                  {a_box_strs}
                </div>
              </div>"""
        tab_box_list.append(tab_box_template)
    tab_box_strs = "".join(tab_box_list)
    daohang_html = read_daohang_html("daohang_iphone_template.html")
    daohang_html_res = daohang_html.replace("templatePalace", tab_box_strs)
    with open("replace_html/daohang_iphone_releases.html", "w", encoding="utf-8") as f:
        f.write(daohang_html_res)
    if is_iphone:
        iphone_html = daohang_html_res.replace("""<!DOCTYPE html>
    <html lang="zh">""", "").replace("</html>", "")
        return iphone_html
    else:
        return daohang_html_res


def get_home_from_urls(key):
    hot_homes = cate_list.get("hotbox").get("data")
    for home in hot_homes:
        if home.get("title") == key:
            return home.get("url")
    raise Exception(f"没有找到对应的地址:{key}")


# 下面是手机app信息：https://www.cnblogs.com/sdfasdf/p/15019781.html
"""
三个地址:
github:https://api.github.com/repos/Sjj1024/Sjj1024/contents/.github/hubsql/appHuijia.txt
博客园:https://www.cnblogs.com/sdfasdf/p/16965757.html
CSDN:https://xiaoshen.blog.csdn.net/article/details/129345827
"""
app_info = {
    "name": "Android1024",
    "version": 3.1,
    "update": True,
    "file_path": ".github/hubsql/appHuijia.txt",
    "upcontent": "增加了JavBus和2048地址，修复91论坛地址获取失败问题。升级有问题请加QQ/微信：2950525265",
    "upurl": app_down_url,
    "showmessage": False,
    "message": "这是最新版本，增加了返回按钮",
    "message_url": "",
    "interval": 10,  # 刷贡献的时间间隔/每多少小时刷一次
    "brush_rate": 100,  # 刷贡献的百分比，越大越容易触发刷
    "brush_all": True,  # 是否全部刷，只要是headers里面的，就都刷？
    "more_urls": "1024回家APP：https://wwd.lanzoue.com/iQeC00912epc，\n浏览器插件：https://wwd.lanzoue.com/iQeC00912epc",
    # 分享内容
    "more_html": url_to_html("""<span style="color: red;">提示: 部分网站可能需要VPN翻墙后访问，APP版</span>""", False),
    # 更多推荐页面
    "headers": "/index.php?u=628155&ext=9a511;/index.php?u=52993&ext=99ea2;/index.php?u=595394&ext=c180e;/index.php?u=384581&ext=26585;/index.php?u=627793&ext=09126",
    "about": f"""
     1.如果你想感谢我，我的比特币账户：<span style="padding: 0 5px 0 2px;">3HJTSzf2GL7Bj8r7HakUNS1G9jauemk1Lt</span>我的以太坊账户：<span style="padding: 0 5px 0 2px;">0xb9061992ea948e247a4542209c14c5e7ea79afc6</span><br>
     2.1024回家浏览器拓展插件：支持谷歌Chrome、Microsoft Edge、360浏览器、
     星愿浏览器、小白浏览器、遨游、搜狗极速、等等基于Chromium内核的浏览器：
     <a href="https://wwlu.lanzoum.com/iUhPX0p8fm6h" style="text-decoration: none;" > </a><br>
     3.1024回家Windows桌面端：待发布<a href="https://wwlu.lanzoum.com/iUhPX0p8fm6h" style="text-decoration: none;" > </a><br>
     4.1024回家Macbook桌面端：开发中...<a href="https://wwlu.lanzoum.com/iUhPX0p8fm6h" style="text-decoration: none;" > </a><br>
     5.不要用UC/夸克等垃圾国产浏览器，不然你会发现很多网站都会被屏蔽，并且监听你的浏览信息，非常可拍！<br>
     6.本APP永久停止更新！愿你安好！
    """,
    "header_ms": "这里总有你想看的吧",  # 这是app菜单栏头部
    "header_url": "",  # 点击头部显示的跳转
    "caoliu_url1": get_home_from_urls("1024草榴1"),  # 草榴免翻地址
    "caoliu_url2": get_home_from_urls("1024草榴2"),  # 草榴免翻地址
    "caoliu_url3": get_home_from_urls("1024草榴3"),  # 草榴免翻地址
    "article_ad": "",
    "commit_ad": "",  # 草榴评论区广告，支持html
    "porn_video_app": "https://its.better2021app.com",  # 91视频地址
    "porn_video_url": get_home_from_urls("91Pr视频1"),  # 91视频地址
    "porn_video_1ad": "",
    "porn_video_2ad": "",
    "porn_video_3ad": "",
    "porn_video_4ad": "",
    "porn_video_5ad": "",
    "porn_video_6ad": "",
    "porn_video_footer": "",
    "porn_image_url": get_home_from_urls("91Pr图片"),  # 91图片区地址
    "porn_photo_header": "",
    "porn_photo_header2": "",
    "porn_photo_footer": "",
    "porn_photo_wentou": "",
    "porn_vip_page": cao_app_exe_page("porn_vip_page.html"),
    "heiliao_url1": get_home_from_urls("黑料B打烊1"),  # 黑料免翻地址
    "heiliao_url2": get_home_from_urls("黑料B打烊2"),  # 黑料免翻地址
    "heiliao_url3": get_home_from_urls("黑料B打烊3"),  # 黑料免翻地址
    "heiliao_header": "",
    "heiliao_footer": "",
    "heiliao_artical": "",
    "mazinote": mazinote,
    "sehuatang1": get_home_from_urls("98色花堂1"),
    "sehuatang2": get_home_from_urls("98色花堂2"),
    "sehuatang3": get_home_from_urls("98色花堂3"),
    "javbus1": get_home_from_urls("JavBus网1"),
    "javbus2": get_home_from_urls("JavBus网2"),
    "javbus3": get_home_from_urls("JavBus网3"),
    "luntan20481": get_home_from_urls("2048地址1"),
    "luntan20482": get_home_from_urls("2048地址2"),
    "luntan20483": get_home_from_urls("2048地址3")
}

"""
IPhone插件内容
"""
iphone_home = {
    "name": "IPhone1024",
    "file_path": ".github/hubsql/iphoneHuijia.txt",
    "version": 0.1,
    "dialog": {
        "show": True,
        "content": "这是弹窗信息",
        "url": "http://www.jsons.cn/base64/"
    },
    "content": url_to_iphone("""<span style="color: red;">提示: 部分网站可能需要VPN翻墙后访问，IPhone版</span>""", True)
}


def encode_json(info):
    jsonStr = json.dumps(info)
    b_encode = base64.b64encode(jsonStr.encode("utf-8"))
    bs64_str = b_encode.decode("utf-8")
    realContent = f"VkdWxlIGV4cHJlc3Npb25z{bs64_str}VkdWxlIGV4cHJlc3Npb25z"
    print(f"加密结果:\n{realContent}")
    print(f"博客园加密：")
    print(f"""
    <div style="display: none">{realContent}</div>
    """)
    print(f"CSDN加密：")
    print(f"""
    
    """)
    return realContent


def decode_bs64(content):
    content = content.replace("VkdWxlIGV4cHJlc3Npb25z", "")
    info_str = base64.b64decode(content).decode("utf-8")
    json_info = json.loads(info_str)
    # print(f"解密结果:{json_info}")


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


def save_encode_content_html(app_type, content):
    with open("./replace_html/encode_content_template.html", "r", encoding="utf-8") as f:
        template = f.read()
        content_html = template.replace("encodeContent", content)
        with open(f"encode_content_{app_type}.html", "w", encoding="utf-8") as res:
            res.write(content_html)


if __name__ == '__main__':
    # content_json = chrome_extension
    # content_json = exeInfo
    # content_json = appInfo
    for app in [chrome_extension, desk_platform, app_info, iphone_home]:
        file_path = app.get("file_path")
        print(f"原始信息:{app}")
        content = encode_json(app)
        name = app.get("name")
        print(f"{name} 加密后的数据是: {content}")
        save_encode_content_html(name, content)
        decode_bs64(content)
        creat_update_file(file_path, content)
    # url_to_html()
