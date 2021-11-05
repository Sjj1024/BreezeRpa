# 清洗安装地址列，使其成为统一


# 构造列清洗函数
import pandas as pd


def loc_change(loc):
  if '弄' in loc:  # 清洗有“弄”的元素
    if '路' in loc:  # 将元素中有“路”的留下，没有的删去
      return bj_func('弄', '路', loc)
    elif '道' in loc:  # 清洗有“道”的元素
      return bj_func('弄', '道', loc)
  elif '号' in loc:  # 清洗有“号”的元素
    if '路' in loc:  # 将元素中有“路”的留下，没有的删去
      return bj_func('号', '路', loc)
    elif '道' in loc:  # 清洗有“道”的元素
      return bj_func('号', '道', loc)
  elif '桥' in loc:
    return loc
  return ''


def bj_func(word1, word2, loc):  # 比较函数，保留‘号’在后面的字符，同时取前面部分
  if loc.index(word1) > loc.index(word2):
    a1 = loc.partition(word1)
    a_a = [a1[0], a1[1]]
    return ''.join(a_a)


def del_ts(loc):
  del_list = ['苑', '园', '源', '庭', '第', '期', '区', '厦', ')', '市', '浦东', '花木镇', ' ']
  for o in del_list:
    if o in loc:
      loc = loc.rsplit(o)[1]
    else:
      pass
  return loc


# 将数字转换一遍，且去除杨高南路严家桥、东北角等字符元素
def trans_dz(loc):
  if '路站' in loc:
    return ''
  if '杨高南路严家桥' in loc:
    return ''
  if '东北角' in loc:
    return ''
  else:
    loc = loc_change(loc)
    loc = del_ts(loc)
    res_list = [str(int(i)) if i.isdigit() else i for i in loc]
    return "".join(res_list)


# 构造地址清洗函数
def lift_loc_change(path):  # path为excel文件的路径
  df = pd.read_excel(path)
  df['安装地址'] = df['安装地址'].apply(lambda x: trans_dz(x))
  df.to_excel('全量电梯_安装地址清洗完成.xlsx', sheet_name="sheet1", index=False)


# 主程序
if __name__ == '__main__':
  lift_loc_change("./全量电梯.xlsx")
