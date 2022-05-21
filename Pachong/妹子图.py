import os

import requests
import re


bpath = os.path.join(os.getcwd(), "meizi")
page = 1

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55"
}
while True:
    url = "https://www.mmlme.com/jp/xgmv?/page/" + str(page) + "nofilter=true"
    resp = requests.get(url=url, headers=head)
    rem = re.compile('<h2 class="item-heading"><a href="(?P<tdz>.*?)">.*?</a>')
    ren = re.compile(
        '.*?<a href="javascript:;" box-img="(?P<turl>.*?)" data-imgbox="imgbox"><img alt="(?P<tit>.*?)" .*?')
    pt = rem.finditer(resp.text)
    if resp.status_code == 404:
        break
    for m in pt:
        tud = m.group("tdz")
        print(tud)
        rep = requests.get(url=tud, headers=head)
        tudz = ren.finditer(rep.text)
        for n in tudz:
            ptit = n.group("tit")
            print(ptit)
            ptu = n.group("turl")
            print(ptu)
            tup = requests.get(url=ptu, headers=head)
            path = bpath + "\\" + ptit + "." + "jpg"
            open(path, "wb").write(tup.content)
    page = page + 1
input("下载完成")