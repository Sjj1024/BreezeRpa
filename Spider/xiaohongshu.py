import json
import os

import requests


def get_imgs():
    print("下载图片")
    # 读取json文件
    json_dict = {}
    with open("/Users/jiang/PyProjects/BreezeRpa/Spider/xhs.json", "r") as json_file:
        json_dict = json.load(json_file)
        # print(json_dict)
    # 获取图片列表
    images_list = []
    title = ""
    desc = ""
    note_dict = {}
    type = ""
    if json_dict:
        note_dict = json_dict["data"][0]
        type = note_dict.get("type")
    if type == "video":
        note_dict = json_dict["data"][0]
        title = note_dict.get("title")
        desc = note_dict.get("desc")
        video_url = note_dict.get("video_info_v2").get("media").get("stream").get("h264")[0].get("master_url")
        # 开始下载视频
        if video_url:
            title = title if title else desc
            title = title[:10]
            print(f"得到的视频{title}链接是:{video_url}")
            down_video(title, video_url)
    else:
        note_dict = json_dict["data"][0]["note_list"][0]
        images_list = note_dict.get("images_list")
        desc = note_dict.get("desc")
        title = title if title else desc
        title = title[:10]
        img_lists = []
        if images_list:
            for i in images_list:
                img_lists.append(i.get("url_size_large"))
        print(f"得到{title}图片链接是:{img_lists}")
        down_img(title, img_lists)


def down_img(title: str, imgs: list):
    print("down_img")
    path = os.getcwd()
    root_path = f"{path}/images/{title}"
    if not os.path.exists(root_path):
        os.makedirs(root_path)
    # 下载图片
    for index, value in enumerate(imgs):
        res = requests.get(value).content
        with open(f"{path}/images/{title}/{index + 100}.jpg", "wb") as f:
            f.write(res)
    print("图片下载完成")


def down_video(title: str, video: str):
    print("down_video")
    path = os.getcwd()
    root_path = f"{path}/videos"
    if not os.path.exists(root_path):
        os.makedirs(root_path)
    res = requests.get(video).content
    with open(f"{root_path}/{title}.mp4", "wb") as f:
        f.write(res)
    print("视频下载完成")


def run():
    print("总控制器")
    get_imgs()


if __name__ == '__main__':
    run()
