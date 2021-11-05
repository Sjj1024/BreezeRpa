# -*- coding: utf-8 -*-
import time
import requests
import pandas as pd
import json
from shapely.geometry import LineString, Point, Polygon

key = "a11f43417a58b2cb0b8b5e26380a48a0"
keyword = "浦东"
city = "上海"
payload = {}
headers = {
    "sec-fetch-dest": "empty",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Connection": "keep-alive"
}
payload_id = {}
headers_id = {
    'authority': 'ditu.amap.com',
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'x-csrf-token': '24333ba6dd2d8f836e5e2fe38f162a65',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'accept': '*/*',
    'amapuuid': 'af244c57-9076-42bd-8368-2069af4f3e5e',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://ditu.amap.com/place/B00154DUI6',
    'accept-language': 'zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'cookie': 'UM_distinctid=17be8900c28dfb-0b1b5260bf3e6-a7d173c-1fa400-17be8900c29ace; cna=EGTCGeSTcHgCAbSoTyLZnfQj; _uab_collina=163169436138666495903301; passport_login=MTI5NjU0MDU2LGFtYXBDQWVtUnVmZHEsYXlqNm1pb215bXhxZXZrNHBicWlxb2ZlcW91bzVhNmMsMTYzMTg2OTkwMSxObVZrWmpJME5UWTRPR1ExTlRNd05EVmpNMkpoTURBek5tRXhOMkkyWkRNPQ%3D%3D; guid=d57a-53e4-7b0e-8dd9; xlly_s=1; x5sec=7b227761676272696467652d616c69626162612d616d61703b32223a2235306365623662663035643034316537636463376562326663633131306238614349586d6c6f6f47454c3670693636446f38482b555444716770586842673d3d227d; x-csrf-token=24333ba6dd2d8f836e5e2fe38f162a65; CNZZDATA1255626299=760822146-1631685940-https%253A%252F%252Fcn.bing.com%252F%7C1631953511; tfstk=cTUfBvwFiKvbdPswuS1y3elk5Io1a7RI1iM0GklYwxLOc1PjesDH8vtsilv9yDh5.; l=eBSyZW7PgbRX8CIaBO5wKurza77tNIdfCsPzaNbMiInca6GApe-x6NCLNU-BXdtj_tfAuexrd8LeqREw8yUg7xiX2QWVVWh_Y6v6-; isg=BFpa4Mif7xAzH2O4OlsYPf3QqwB8i95lMEaP3WTSo-241_8RThq7djphp6vLB1b9'
}


def geompoi_to_geometry(xy):
    xylist = xy.split(";")
    for i in range(len(xylist)):
        xylist[i] = xylist[i].split(',')
        xylist[i][0] = float(xylist[i][0])
        xylist[i][1] = float(xylist[i][1])
    line = Polygon(LineString(xylist))
    return line.wkt


def get_poi(types):
    url = f"https://restapi.amap.com/v3/place/text?key={key}&children=1&keywords={keyword}&types={types}&city={city}&children=0&offset=20&page=1&extensions=all"
    response = requests.request("GET", url, headers=headers, data=payload)
    count = int(response.json()["count"])
    print(count)
    if count == 0: return
    for page in range(1, 1 + int(count / 20)):
        url_page = f"https://restapi.amap.com/v3/place/text?key={key}&children=1&keywords={keyword}&types={types}&city={city}&children=1&offset=20&page={page}&extensions=all"
        response_page = requests.request("GET", url_page, headers=headers, data=payload)
        pois = response_page.json()["pois"]
        for poi in pois:
            print(poi)
            dic = {}
            dic["id"] = poi['id']
            print(dic)
            dic['location'] = poi['location']
            dic['address'] = poi['pname'] + poi['adname'] + str(poi['address'])
            dic['name'] = poi['name']
            dic['tel'] = poi['tel']
            dic['type'] = poi['type']
            url_id = f"https://ditu.amap.com/detail/get/detail?id={poi['id']}"
            response_id = requests.request("GET", url_id, headers=headers_id, data=payload_id)
            print(response_id)
            print(response_id.content.decode())

            response_json = response_id.json()
            if not response_json["data"]["spec"]["mining_shape"]["shape"]: break
            dic['geompoi'] = response_json["data"]["spec"]["mining_shape"]["shape"]
            if dic['geompoi'] == '':
                dic['geometry'] = 'null'
            else:
                dic['geometry'] = geompoi_to_geometry(dic['geompoi'])
            poi_list.append(dic)
            print(dic['geometry'])
            print(poi_list)
            time.sleep(10)
        print("success!")

    # url = f"http://restapi.amap.com/v3/place/text?key={key}&keywords={keyword}&types={types}&city={city}&children=1&offset=20&page=1&extensions=all"
    # res={"name":"",}
    # return res


if __name__ == '__main__':
    df = pd.read_excel(r'amap_poicode.xlsx')
    typ = df['NEW_TYPE'].tolist()
    poi_list = []
    # get_poi('高等院校')
    for ty in typ:
        poi_list = []
        get_poi(str(ty))
        poi_json = json.dumps(poi_list)
        df = pd.read_json(poi_json)
        df.to_excel(fr"D:\Python\Mi\data\{ty}poi.xlsx")
