# 加密所有的数据
import base64
import json

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
# 下面是手机app信息：https://www.cnblogs.com/sdfasdf/p/15019781.html
appInfo = {
    "update": True,
    "version": 3.1,
    "upcontent": "增加了JavBus和2048地址，修复91论坛地址获取失败问题。升级有问题请加QQ/微信：3593211542",
    "upurl": app_surl,
    "showmessage": False,
    "message": "这里是message4",
    "message_url": "",
    "interval": 20,  # 刷贡献的时间间隔/小时
    "more_urls": "https://1024shen.com/gohome.html",  # 更多推荐页面
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
    "version": "0.0.1",
    "dialog": {
        "show": True,
        "content": "这是弹窗信息"
    },
    "update": {
        "show": True,
        "content": "更新了更高级的信息",
        "url": "http://www.jsons.cn/base64/"
    },
    "data": {
        "navigation": {
            "热门区域": [{"title": "百度一下", "url": "www.baidu.com", "icon": ""},
                         {"title": "淘宝一下", "url": "www.baidu.com", "icon": ""}],
            "新闻头条": [{"title": "百度一下", "url": "www.baidu.com", "icon": ""},
                         {"title": "百度一下", "url": "www.baidu.com", "icon": ""}]
        }
    }
}


def creat_exe():
    # jsonStr = json.dumps(exeInfo)
    jsonStr = json.dumps(exeInfo)
    # print("转换后的json字符串是:" + jsonStr)
    # print("")
    res2 = base64.b64encode(jsonStr.encode())
    bs64Str = str(res2).replace("b'", "").replace("'", "")
    realContent = f"pythonpython{bs64Str}pythonpython"
    print("\nexe信息如下：")
    print(realContent)


def creat_app():
    # jsonStr = json.dumps(exeInfo)
    jsonStr = json.dumps(appInfo)
    # print("转换后的json字符串是:" + jsonStr)
    # print("")
    res2 = base64.b64encode(jsonStr.encode())
    bs64Str = str(res2).replace("b'", "").replace("'", "")
    realContent = f"""
<div class="cnblogs_code">
<pre style="display: none;"><span style="color: #000000;">
pythonpython{bs64Str}pythonpython

</span></pre>
</div>
<p><a href="https://img2022.cnblogs.com/blog/2506425/202204/2506425-20220403173022189-492682951.png" data-fancybox="gallery"><img src="https://img2022.cnblogs.com/blog/2506425/202204/2506425-20220403173022189-492682951.png" alt="" class="medium-zoom-image" loading="lazy" /></a></p>
"""
    print("app信息如下：")
    print(realContent)


def encode_chrome():
    jsonStr = json.dumps(appInfo)
    # print("转换后的json字符串是:" + jsonStr)
    # print("")
    res2 = base64.b64encode(jsonStr.encode())
    bs64Str = str(res2).replace("b'", "").replace("'", "")
    realContent = f"""
    <div class="cnblogs_code">
    <pre style="display: none;"><span style="color: #000000;">
    pythonpython{bs64Str}pythonpython

    </span></pre>
    </div>
    <p><a href="https://img2022.cnblogs.com/blog/2506425/202204/2506425-20220403173022189-492682951.png" data-fancybox="gallery"><img src="https://img2022.cnblogs.com/blog/2506425/202204/2506425-20220403173022189-492682951.png" alt="" class="medium-zoom-image" loading="lazy" /></a></p>
    """
    print("app信息如下：")
    print(realContent)


def encode_json(info):
    jsonStr = json.dumps(info)
    b_encode = base64.b64encode(jsonStr.encode("utf-8"))
    bs64_str = b_encode.decode("utf-8")
    realContent = f"VkdWxlIGV4cHJlc3Npb25z{bs64_str}VkdWxlIGV4cHJlc3Npb25z"
    print(realContent)


if __name__ == '__main__':
    creat_app()
    # creat_exe()
