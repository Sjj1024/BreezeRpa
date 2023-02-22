import requests
import base64
from github import Github


def creat_file(path, content, message):
    print(f"添加一个文件进去...")
    GIT_TOKEN = "ghp_888grzs67MqxbZUH3wmIFKzecaKB0cTLy3ICBkl".replace("888", "")
    g = Github(GIT_TOKEN)
    repo = g.get_repo("Sjj1024/Sjj1024")
    res = repo.create_file(path, "添加一个新文件", "这是数据库")
    print(res)


def delete_file():
    print(f"删除文件")
