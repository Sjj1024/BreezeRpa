import base64
import json

"""
再分享一个APP，可以自动获取所有网站免翻地址，并过滤广告：
下载链接：[url]https://wwi.lanzoup.com/irezWz6l08f[/url]
[img]https://1024shen.com/wp-content/uploads/2022/01/2022011714060442.jpg[/img]

app-user-agent:
Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1
"""

app_surl = "https://wwi.lanzoup.com/i0WELyxcc5g"
fenxiang_ma = "1月分享两个邀请码：【a6aff412*e2dee7e】【65d*db9db9089820】"


# 下面是手机app信息：https://www.cnblogs.com/sdfasdf/p/15019781.html
appInfo = {
    "update": True,
    "version": 2.9,
    "upcontent": "增加了JavBus和2048地址，修复91论坛地址获取失败问题。升级有问题请加微信：sxsuccess",
    "upurl": app_surl,
    "showmessage": False,
    "message": "这里是message",
    # 我真的爱你，爱你的宝贝,我的大吗
    # "headers": "/index.php?u=595021&ext=8c45d;/index.php?u=587907&ext=962d2;/index.php?u=595023&ext=15a7e;",
    "headers": "/index.php?u=587907&ext=962d2;/index.php?u=587906&ext=88a67;/index.php?u=598447&ext=a3102;",
    "about": "1.黑料视频可以点右上角用浏览器打开观看，本APP看不了，不知道问题<br>"
             f"2.{fenxiang_ma}<br>"
             "3.隐藏其中一位，每月都会不定时在这里分享两个1024码子！<br>"
             '4.本APP永久停止更新！愿你安好',
    "header_ms": "这里总有你想看的吧", # 这是app菜单栏头部
    "header_url": "", # 点击头部显示的跳转
    "article_ad": "微信:sxsuccess",
    "commit_ad": "", # 草榴评论区广告，支持html
    "porn_share_url":"",
    "porn_video_1ad":"",
    "porn_video_2ad":"",
    "porn_video_3ad":"",
    "porn_video_4ad":"",
    "porn_video_5ad":"",
    "porn_video_6ad":"",
    "porn_video_footer":"",
    "porn_photo_header":"",
    "porn_photo_header2":"",
    "porn_photo_footer":"",
    "porn_photo_wentou":"",
    "heiliao_header":"",
    "heiliao_footer":"",
    "heiliao_artical":"",
    "mazinote": "需要邀请碼请加微信:sxsuccess",
    "sehuatang": "https://warwetretyry.com/portal.php",
    "sehuatang1": "https://www.qwerwrrt.one",
    "sehuatang2": "https://qweqwtret.best",
    "sehuatang3": "https://retreytryuyt.top",
    "javbus1": "https://www.dmmbus.fun",
    "javbus2": "https://www.busjav.fun",
    "javbus3": "https://www.cdnbus.fun",
    "luntan20481": "https://bbs.yyyz.cc/2048/",
    "luntan20482": "https://bbs.yyyz.cc/2048/",
    "luntan20483": "https://bbs.yyyz.cc/2048/"
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
    realContent = f"pythonpython{bs64Str}pythonpython"
    print("app信息如下：")
    print(realContent)


if __name__ == '__main__':
    creat_app()
    creat_exe()


