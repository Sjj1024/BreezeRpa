# 清洗安装地址列，使其成为统一
import pandas as pd


# 构造列清洗函数
def loc_change(loc):
  str1 = list(loc)
  if '弄' in loc:  # 清洗有“弄”的元素
    xx = loc.partition('弄')
    xx_x = [xx[0], xx[1]]
    return ''.join(xx_x)
  elif '号' in loc:  # 清洗有“号”的元素
    if '路' in loc:  # 将元素中有“路”的留下，没有的删去
      y1 = str1.index('号')
      y2 = str1.index('路')
      if y1 > y2:
        yy = loc.partition('号')
        yy_y = [yy[0], yy[1]]
        return ''.join(yy_y)
    elif '道' in loc:  # 清洗有“道”的元素
      z1 = str1.index('号')
      z2 = str1.index('道')
      if z1 > z2:
        zz = loc.partition('号')
        zz_z = [zz[0], zz[1]]
        return ''.join(zz_z)
  elif '桥' in loc:
    return loc
  return ''


# 去除特定的前面部分
def del_ts(loc):
  del_list = ['苑', '园', '源', '庭', '第', '期', '区', '厦', ')', '市', '浦东', '花木镇', ' ']
  for o in del_list:
    if o in loc:
      loc = loc.rsplit(o)[1]
  return loc


# 将数字转换一遍，且去除杨高南路严家桥、东北角等字符元素
def trans_dz(loc):
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
  lift_loc_change("/Users/metrodata/Downloads/全量电梯.xlsx")
