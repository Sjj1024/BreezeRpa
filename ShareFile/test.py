# 使用python读取访问远程共享文件目录

root_dir = '//DESKTOP-5KE8K1B/TestFileShare/每天一记.txt'  # 用正斜杠访问网络路径，绝对路径

with open(root_dir, "r") as f:
    print(f.read())