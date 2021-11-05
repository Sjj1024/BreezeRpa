import datetime
import json
import time
import numpy as np
import pandas as pd
import datetime as dt


def union_test():
  x = {"a", "b", "c"}
  y = {"f", "d", "a"}
  z = {"c", "d", "e"}
  a = {"z", "d", "e"}
  result = x.union(y, z, a)
  print(result)


def df_col_dup():
  data = {'state': [1, 1, 2, 5, 1, 2, 3], 'pop': ['a', 'b', 'c', 'd', 'b', 'c', 'd']}
  frame = pd.DataFrame(data)
  print(frame)
  # 去除重复值的行，指定列名
  res = frame.drop_duplicates(subset=['pop'])
  print("-------------------------")
  print(res)
  # 取列最大值
  max_num = frame["state"].max()
  print(f"最大值是:{max_num}")


def none_if():
  data = {}
  frame = pd.DataFrame(data)
  if frame.empty:
    print(11111)
  else:
    print(22222)


def cast_list():
  data = {'state': [1, 1, 2, 5, 1, 2, 3], 'pop': ['a', 'b', 'c', 'd', 'b', 'c', 'd']}
  frame = pd.DataFrame(data)
  # print(frame)
  frame["state"] = [[i] for i in frame["state"]]
  print(frame)


def list_creat():
  res = ["1" if x % 2 == 0 else "2" for x in range(10)]
  print(res)


def fillter_data():
  data = {'state': [1, 1, 2, 5, 1, 2, 3], 'pop': ['a', 'b', 'c', 'd', 'b', 'c', 'd']}
  frame = pd.DataFrame(data)
  # print(frame)
  res = frame[frame["state"] >= 2]
  print(res)
  print(res.columns.values)
  d1 = datetime.date.today()
  print(f'日期所属的年份为 : {int(d1.year)}')
  print(f'日期所属的月份为 : {type(d1.month)}')
  print(f'日期具体的日期号为 : {d1.day}')


def timestamp_to_date():
  timeStamp = 1635177209
  res = pd.to_datetime(timeStamp, unit='s')
  print(res)


def dataframe_grpupby():
  df = pd.DataFrame({
    '党员编号': ['a', 'a', 'b', 'b', 'a'],
    'key2': ['one', 'two', 'one', 'two', 'three'],
    '本月实缴金额': [2, 2, 2, 2, 2],
    'data2': [5, 5, 5, 10, 5]
  })
  print(df)
  print("--------------------")
  # df["total_num"] = df.data1 + df.data2
  # print(df)
  print("--------------------")
  ass = df.groupby("党员编号").sum()
  print(ass)
  print("--------------------")
  # 只统计值类型的数据列
  # print(ass.get("a"))
  print(type(ass))
  print(ass)
  print("--------------------")
  # df2 = ass.to_frame()
  df2 = ass.rename(columns={"本月实缴金额": "年度汇总金额"})
  # 只保留某列
  df2 = df2[["年度汇总金额"]]
  print(df2)
  df1 = pd.DataFrame({'党员编号': ['a', 'b', 'c', 'd', 'a'], 'feature1': [1, 1, 2, 3, 1], "data2": [10, 10, 10, 10, 10]})
  # 基于共同列alpha的内连接
  df3 = df1.merge(df2, how='left', on='党员编号')
  print(df3)


def two_df_merge():
  print("两个DF合并")
  # df1 = pd.DataFrame({
  #   'key': ['a', 'a', 'b', 'b', 'a'],
  #   'data2': [5, 5, 5, 10, 5]
  # })
  # df2 = pd.DataFrame({
  #   'key': ['a', 'a', 'b', 'b', 'a'],
  #   'data1': [2, 2, 2, 2, 2],
  # })
  # df3 = pd.merge(df1, df2, how="right", on="key")
  # print(df3)
  # 单列的内连接
  # 定义df1

  df1 = pd.DataFrame({'alpha': ['A', 'B', 'C', 'D', 'E'], 'feature1': [1, 1, 2, 3, 1]})
  # 定义df2
  df2 = pd.DataFrame({'alpha': ['A', 'B', 'C', 'D'], 'pazham': ['apple', 'orange', 'pine', 'pear']})
  # print(df1)
  # print(df2)
  # 基于共同列alpha的内连接
  df3 = df1.merge(df2, how='left', on='alpha')
  print(df3)


def time_df():
  time_date = datetime.date.today()
  new_df = pd.DataFrame({
    "年度": [time_date.year],
    "月度": [time_date.month]
  })
  print(new_df)


def drop_columns():
  # 删除某列
  df = pd.DataFrame({
    '党员编号': ['a', 'a', 'b', 'b', 'a'],
    'key2': ['one', 'two', 'one', 'two', 'three'],
    '本月实缴金额': [2, 2, 2, 2, 2],
    'data2': [5, 5, 5, 10, 5]
  })
  print(df)
  df.drop(["data2"], axis=1, inplace=True)
  print(df)


def generate_age(row):
  print(row)
  age = row["data2"]
  if age < 6:
    row["data2"] = 100
  row["shuzu"] = [age, age * 2]
  row["array_date"].append({"a": 8, "b": 8})
  return row


def apply_datarow():
  print("dataframe应用行数据:")
  df = pd.DataFrame({
    '党员编号': ['a', 'a', 'b', 'b', 'a'],
    'key2': ['one', 'two', 'one', 'two', 'three'],
    '本月实缴金额': [2, 2, 2, 2, 2],
    'data2': [5, 5, 5, 10, 5],
    "array_date": [[{"a": 5, "b": 6}, ], [{"a": 5, "b": 6}, ], [{"a": 5, "b": 6}, ], [{"a": 5, "b": 6}, ],
                   [{"a": 5, "b": 6}, ], ]
  })
  df2 = df.apply(generate_age, axis=1)
  print(df2)


def test_axis():
  # 测试轴的使用
  df = pd.DataFrame([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]],
                    columns=['col0', 'col1', 'col2', 'col3'])
  print(df)
  print("-------------------")
  # 0轴表示y方向，那肯定是列下的均值，
  print(df.mean(axis=0))
  # 1轴表示X方向，那肯定是行的均值
  print(df.mean(axis=1))
  print("-------------------")
  # 删除索引行
  print(df.drop(1))
  # 删除列
  print(df.drop("col2", axis=1))


def pipei_two_df():
  # dianti_df = pd.read_excel("dianti.xlsx")
  # columns_name = dianti_df.columns.values
  # print(columns_name)
  # with open("dianti_jsonschema.json", "r") as f:
  #   dianti_json = json.load(f)
  #   print(dianti_json.get("json_schema").get("properties"))
  # 对两个df进行匹配
  df1 = pd.DataFrame({
    '电梯编号': ['a', 'b', 'c', 'd', 'e'],
    'key2': ['one', 'two', 'one', 'two', 'three'],
    '本月实缴金额': [2, 2, 2, 2, 2],
    'data2': [5, 5, 5, 10, 5]
  })

  df2 = pd.DataFrame({
    '电梯编号': ['c', 'd', 'e', 'f', 'g'],
    'key2': ['one', 'two', 'one', 'two', 'three'],
    '本月实缴金额': [2, 2, 2, 2, 2],
    'data2': [6, 6, 6, 6, 6],
    'data3': [5, 5, 5, 10, 5],
  })
  # inner是取交集
  data_mer = pd.merge(df1, df2, on=["电梯编号"], how="inner")
  print(data_mer)
  print("------------------------------------")
  # left是以左表为主
  data_mer = pd.merge(df1, df2, on=["电梯编号"], how="left")
  print(data_mer)
  print("------------------------------------")
  # 以右表为主
  data_mer = pd.merge(df1, df2, on=["电梯编号"], how="right")
  print(data_mer)
  print("------------------------------------")
  # 全部的
  data_mer = pd.merge(df1, df2, on=["电梯编号"], how="outer")
  print(data_mer)
  print("------------------------------------")
  # 取df1中在df2里没有的数据，也就是补集
  df1 = df1.append(df2)
  print(df1)
  print("------------------------------------")
  """
  subset 为去重的列，默认为None，keep：表示是否保留，first表示保留第一次出现的，
  last表示保留最后出现的，false表示删除所有的重复项，inplace表示是否在原表上修改,
  
  """
  another = df1.drop_duplicates(subset=["电梯编号"], keep=False)
  print(another)
  print("----------------------------------")
  df1["key2"] = df1["key2"].apply(key_func)
  print(df1)


def key_func(path):
  if path.startswith("o"):
    return "ooooo"
  return path


if __name__ == '__main__':
  # union_test()
  # df_col_dup()
  # none_if()
  # cast_list()
  # list_creat()
  # fillter_data()
  # timestamp_to_date()
  # dataframe_grpupby()
  # two_df_merge()
  # time_df()
  # drop_columns()
  # apply_datarow()
  # test_axis()
  pipei_two_df()
