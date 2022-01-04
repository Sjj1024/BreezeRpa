import os
import re


def read_html_str():
  # 读取txt中的文本作为数据源
  cookie_path = os.path.join(os.path.split(__file__)[0], "demotest.html")
  print(cookie_path)
  with open(cookie_path, "r") as f:
    data = f.read()
  return data


def write_html_str(htmls_str):
  html_res = os.path.join(os.path.split(__file__)[0], "html_res.txt")
  with open(html_res, "w") as f:
    data = f.write(htmls_str)
  return data


def clear_content(html: str):
  html = html.replace('<img src="', "[img]")
  html = re.sub(r'" alt=.*?>', '[/img]', html)
  html = re.sub(r'<.*?>', '', html)
  html = re.sub(r'jpg".*?/>', 'jpg[/img]', html)
  print(html)
  write_html_str(html)


if __name__ == '__main__':
  htmls = read_html_str()
  clear_content(htmls)
