import os
import re


def read_html_str():
    # 读取txt中的文本作为数据源
    cookie_path = os.path.join(os.path.split(__file__)[0], "html_res.txt")
    print(cookie_path)
    with open(cookie_path, "r", encoding="utf-8") as f:
        data = f.read()
    return data


def write_html_str(htmls_str):
    html_res = os.path.join(os.path.split(__file__)[0], "caoliu_html_res.txt")
    with open(html_res, "w", encoding="utf-8") as f:
        data = f.write(htmls_str)
    return data


def clear_content(html: str):
    html = html.replace(' ', "")
    html = re.sub(r'<img +.*?src="data', "[img]", html)
    html = re.sub(r'<img +.*?src="', "[img]", html)
    html = re.sub(r'" alt=.*?>', '>', html)
    html = re.sub(r'" data-src=.*?>', '>', html)
    html = re.sub(r'<.*?>', '', html)
    html = re.sub(r'\S.*?上传', '', html)
    html = re.sub(r' ', '', html)
    html = re.sub(r'	', '', html)
    html = re.sub(r'\n+', '', html)
    html = re.sub(r'&nbsp;', '', html)
    html = re.sub(r'微信.*?上传', '', html)
    html = re.sub(r'QQ.*?上传', '', html)
    html = re.sub(r'<div class="xs0">.*?</div>', '', html, re.S)
    html = re.sub(r'\[img\]', '\n[img]', html)
    html = re.sub(r'jpg.*?/?>', 'jpg[/img]\n', html)
    html = re.sub(r'\S.*?下载附件', '', html)
    html = re.sub(r'堂', '', html)
    html = re.sub(r'\[img\]st.*?">', '', html)
    html = re.sub(r'static.*?zoomfile="', '', html)
    html = re.sub(r'\[/img\]', '[/img]\n', html)
    html = re.sub(r'\[img\]static.*?>', '', html)
    html = re.sub(r'\[img\]static.*?\]', '', html)
    print(html)
    write_html_str(html)


if __name__ == '__main__':
    htmls = read_html_str()
    clear_content(htmls)
