import datetime
import time
from collector_utils import *
import pandas as pd


# from petal.etl.transform import *


def get_temp_man():
  data_manager = get_manager_client_base()
  lst = data_manager.template_list().keys()
  print(lst)


def convert(x):
  d = datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
  t = d.timetuple()
  timeStamp = int(time.mktime(t))
  return timeStamp


def read_data_from_excel():
  df = pd.read_excel("/Users/metrodata/Desktop/PyProject/BreezeRpa/CollectClient/已获取未关联地块信息-V1.xlsx")
  # print(df.columns.values)
  # df["土地创建时间"] = pd.to_datetime(df["土地创建时间"])
  # df["土地更新时间"] = pd.to_datetime(df["土地更新时间"])
  return df


def update_dangyuan():
  """
  更新党员编号
  """
  df = pd.read_excel("/Users/metrodata/Desktop/PyProject/BreezeRpa/CollectClient/dangyuan.xlsx")
  data_client = get_template_client_base("6c18d1b6-406e-4961-965c-c4b9cfc14cc4")
  data_client.data_update_separate(df)


def clear_douhao():
  data_client = get_template_client_base("09090641-9559-4e77-a3c8-227740e43937")
  target_df = data_client.data_select(to_df=True)
  need_df = target_df[target_df["土地编码"].apply(lambda x: "," in x if isinstance(x, str) else False)]
  # need_df = target_df.filter(regex='e$', axis=1)
  # need_df = target_df["土地编码"].contains(",")
  # print(need_df)
  need_df["土地编码"] = need_df["土地编码"].apply(lambda x: x.replace(",", "，"))
  # print(need_df)
  data_client.dataframe_to_json(need_df)
  target_df.to_excel("")
  data_client.data_update_separate(need_df)
  # data_client.data_update_separate(need_df.loc[:, ["id", "土地编码"]])


def run():
  data_client = get_template_client_base("47100530-2e14-481b-8613-86062f609a16")
  target_df = data_client.data_select(to_df=True)
  # 读数据从excel
  res_inner = target_df[(target_df["月度"] == 1) & (target_df["年度"] == 2022)]
  # source_data = read_data_from_excel()
  # res_inner = pd.merge(source_data, target_df, on=["land_uuid"], how="inner", suffixes=("_s", "_t"))
  # print(res_inner)
  data_client.data_delete(res_inner)
  # data_client.data_create(res_inner)


if __name__ == '__main__':
  # get_temp_man()
  # get_temp_client()
  run()
  # clear_douhao()
  # update_dangyuan()
