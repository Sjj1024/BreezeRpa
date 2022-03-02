import pandas as pd


def init_parser(df: pd.DataFrame, unique_field: str, field_mapping: dict):
  """collector数据通用预处理"""
  if not df.empty:
    more_fields = list(set(df.keys()).difference(set(field_mapping.keys())))
    df.drop(more_fields, axis=1, inplace=True)
    df['update_time'] = df['update_time'].apply(lambda x: pd.to_datetime(x, unit='s').strftime("%Y-%m-%d %H:%M:%S"))
    if unique_field not in df.keys():
      raise ValueError(f'唯一字段 {unique_field} 不存在')
    if not df[unique_field].is_unique:
      num_list = df[unique_field].to_list()
      num_set = set(num_list)
      for n in num_set:
        if num_list.count(n) > 1:
          print(f"重复数据是: {n}，重复次数是:{num_list.count(n)}")
      raise ValueError(f'唯一字段 {unique_field} 存在重复数据')
    df.rename(columns=field_mapping, inplace=True)
    fill_nan(df)
  return df


def fill_nan(df: pd.DataFrame):
  fill_fields = ["S_LAST_UPDATETIME", "CJSJ", "GXSJ", "GSLDSJ", "ZFSJ", "QYBDRQ", "FXBGRQ", "BJSJ", "PDSJ", "YQTS"]
  need_fill = list(set(fill_fields).intersection(set(df.keys())))
  df[need_fill] = df[need_fill].fillna("1970-01-02 00:00:00")
  df.fillna('0', inplace=True)
  # 不要唯一列
  df.drop(["ID"], axis=1, inplace=True)
  return df
