import json

import pandas as pd


def read_excel():
  df = pd.read_excel("20211104电梯基本信息表-映射.xlsx", sheet_name="Sheet2")
  df_json = json.loads(df.to_json(orient="values", force_ascii=False))
  name_make = {}
  for ls in df_json:
    if ls[0]:
      name_make[ls[0]] = ls[1] if ls[1] else ""
  print(str(name_make))
  with open("make_pinpai.json", "w", encoding="utf-8") as f:
    f.write(str(name_make).replace("'", '"'))

  df = pd.read_excel("20211104电梯基本信息表-映射.xlsx", sheet_name="Sheet3")
  df_json = json.loads(df.to_json(orient="values", force_ascii=False))
  name_make = {}
  for ls in df_json:
    if ls[0]:
      name_make[ls[0]] = ls[1] if ls[1] else ""
  print(str(name_make))
  with open("name_type.json", "w", encoding="utf-8") as f:
    f.write(str(name_make).replace("客梯e'NT", "客梯e1NT").replace("'", '"').replace("客梯e1NT", "客梯e'NT"))



if __name__ == '__main__':
    read_excel()