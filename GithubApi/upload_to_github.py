import base64
import json
import requests


def read_file(file_path):
    with open(file_path, "rb+") as f:
        return f.read()


def add_file(path, content, message):
    url = f"https://api.github.com/repos/Sjj1024/CvReport/contents/img/{path}"
    GIT_TOKEN = "ghp_888grzs67MqxbZUH3wmIFKzecaKB0cTLy3ICBkl".replace("888", "")
    headers = {"Authorization": f"Bearer {GIT_TOKEN}",
               'Accept': 'application/vnd.github.v3+json',
               'Content-Type': 'application/json'}
    base64_content = base64.b64encode(content).decode('utf-8')
    # print(base64_content)
    payload = json.dumps({
        "message": message,
        "branch": "gh-pages",
        "content": base64_content
    })
    print("开始推送文件....")
    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response.text)


if __name__ == '__main__':
    file = "nihao".encode("utf-8")
    add_file("1024回家V5.0.1.apk", file, "添加1024文件")