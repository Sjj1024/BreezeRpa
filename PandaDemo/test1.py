import pandas as pd
import linecache

# 一，打开一个文件，文件对象f
f = open("1.txt", 'wt')

for i in range(10):
  # 二，将打印内容打印到文件中，重定向参数file=f
  print("第{0}条数据".format(i), file=f)
