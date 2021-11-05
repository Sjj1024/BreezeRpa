import json
import math
from io import StringIO
import requests
from shapely.geometry import LineString, Polygon
import pandas as pd


def get_poi(params, types, poi_list):
    key = params.get("key")
    city = params.get("city")
    keyword = params.get("keyword")
    print(f"开始获取{city}-{keyword}-{types}的poi数据......")
    url = f"https://restapi.amap.com/v3/place/text?key={key}&keywords={keyword}&types={types}&city={city}&children=0&offset=20&page=1&extensions=all"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }
    res = requests.get(url, headers=headers)
    count = int(res.json()["count"])
    if count == 0:
        return
    print(f"总共{count}条POI数据")
    for page in range(1, 1 + int(count / 20)):
        print(f"开始获取第{page}页数据......")
        url = f"https://restapi.amap.com/v3/place/text?key={key}&keywords={keyword}&types={types}&city={city}&children=0&offset=20&page={page}&extensions=all"
        res = requests.get(url, headers=headers)
        pois = res.json()["pois"]
        for poi in pois:
            print(f"获取{poi['name']}数据......")
            try:
                # dic = {"id": poi['id'],
                #        'location': poi['location'],
                #        'address': poi['pname'] + poi['adname'] + str(poi.get('address', "-")),
                #        'name': poi['name'],
                #        'tel': poi['tel'],
                #        'type': poi['type']
                #        }
                # 坐标转换为84
                poi["location"] = gcj02towgs84(poi["location"])
                poi_list.append(poi)
            except Exception as e:
                print(f"{poi['name']}数据出现异常:{e}")
            # 获取边界区域，并判断是否有值
            # url_id = f"https://ditu.amap.com/detail/get/detail?id={poi['id']}"
            # shape = get_shape(url_id)
            # dic['geompoi'] = shape
            # if shape:
            #     dic['geometry'] = geompoi_to_geometry(shape)
            # else:
            #     dic['geometry'] = 'null'
            # time.sleep(10)


def geompoi_to_geometry(xy):
    xylist = xy.split(";")
    for i in range(len(xylist)):
        xylist[i] = xylist[i].split(',')
        xylist[i][0] = float(xylist[i][0])
        xylist[i][1] = float(xylist[i][1])
    line = Polygon(LineString(xylist))
    return line.wkt


def get_shape(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
        "cookie": "guid=1258-49a6-b991-df8c; UM_distinctid=17c7ce273ea33a-0ce2235a5c8d94-123b6650-13c680-17c7ce273eb821; CNZZDATA1255626299=1980048416-1634174413-https%253A%252F%252Fwww.baidu.com%252F%7C1634174413; cna=hJTuGZopbF8CAYzOMEKB6wXK; xlly_s=1; tfstk=coO5BAMSsHdqhjkUaUg4YkySf6CCZ0F5u4sDPpgvFl7zKwL5iVVNf21X-oCFJZ1..; l=eBrvKg7ggFBxtUgLBOfZhurza779hIRfguPzaNbMiOCP_25p5G6lW6EkMLL9CnGVH6keR3o2xuSYBMFyqP5RUjWvI9owqFzS3dC..; isg=BHJyqNq-R-p_LnvX5GHFOiLXw75UA3ad98o_TjxL9CUQzxPJJJOVrcNtv2vzv-41; x5sec=7b227761676272696467652d616c69626162612d616d61703b32223a223035663366393434323430333939353133646438303764353561313561613033434e584f6e6f7347454e69432b71533067354355585367434d4f71436c654547227d"
        # "Referer": "https://www.amap.com/place/B00156GO95"
    }
    res = requests.get(url, headers)
    # 如果不是json数据，就会报错
    try:
        res_json = res.json()
        if not res_json["data"]["spec"]["mining_shape"]["shape"]:
            return None
        else:
            geo_mpoi = res_json["data"]["spec"]["mining_shape"]["shape"]
            print(f"获取shape成功")
            return geo_mpoi
    except Exception as e:
        print(f"获取shape数据出错:{e}")


# GCJ02/谷歌、高德 转换为 WGS84 gcj02towgs84
def gcj02towgs84(localStr):
    lng = float(localStr.split(',')[0])
    lat = float(localStr.split(',')[1])
    PI = 3.1415926535897932384626
    ee = 0.00669342162296594323
    a = 6378245.0
    dlat = transformlat(lng - 105.0, lat - 35.0)
    dlng = transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * PI
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * PI)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * PI)
    mglat = lat + dlat
    mglng = lng + dlng
    return str(lng * 2 - mglng) + ',' + str(lat * 2 - mglat)


def transformlat(lng, lat):
    PI = 3.1415926535897932384626
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * \
          lat + 0.1 * lng * lat + 0.2 * math.sqrt(abs(lng))
    ret += (20.0 * math.sin(6.0 * lng * PI) + 20.0 *
            math.sin(2.0 * lng * PI)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * PI) + 40.0 *
            math.sin(lat / 3.0 * PI)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * PI) + 320 *
            math.sin(lat * PI / 30.0)) * 2.0 / 3.0
    return ret


def transformlng(lng, lat):
    PI = 3.1415926535897932384626
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
          0.1 * lng * lat + 0.1 * math.sqrt(abs(lng))
    ret += (20.0 * math.sin(6.0 * lng * PI) + 20.0 *
            math.sin(2.0 * lng * PI)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * PI) + 40.0 *
            math.sin(lng / 3.0 * PI)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * PI) + 300.0 *
            math.sin(lng / 30.0 * PI)) * 2.0 / 3.0
    return ret


def cover_positon():
    df = pd.read_excel('shanghai_pd_poi.xlsx', sheet_name='amap_need', converters={"NEW_TYPE": str})
    typ_list = df['location'].tolist()
    print(typ_list)


def run():
    print("开始获取数据......")
    poi_list = []
    # converters
    df = pd.read_excel('20211013-amap_poicode-zjc.xlsx', sheet_name='amap_need', converters={"NEW_TYPE": str})
    typ_list = df['NEW_TYPE'].tolist()
    params = {
        "key": "a11f43417a58b2cb0b8b5e26380a48a0",
        "city": "上海",
        "keyword": "浦东"
    }
    for ty in typ_list:
        get_poi(params, ty, poi_list)
    poi_json = json.dumps(poi_list)
    # Protocol not known error
    df = pd.read_json(StringIO(poi_json))
    df.to_excel(f"shanghai_pd_poi.xlsx")
    print(f"数据全部获取完成，已存入文件")


if __name__ == '__main__':
    run()

    # 坐标转换:
    # loc_pos = gcj02towgs84("121.667003,31.141447")
    # print(loc_pos)
