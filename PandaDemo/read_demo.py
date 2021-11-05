import pandas as pd


def read_ele():
  print("读取电梯格式")
  ele_data = pd.read_excel("/Users/metrodata/Downloads/全量电梯.xlsx", sheet_name="sheet1")
  path_list = ele_data["安装地址"]
  for i in path_list:
    if i.startswith("上海市浦东新区高科西路"):
      print(f"原来的格式：{i}")
      print(f"转换后的格式:{hasNumbers(i)}")


def hasNumbers(chat):
  res_list = [str(int(i)) if i.isdigit() else i for i in chat]
  return "".join(res_list)


if __name__ == '__main__':
    read_ele()