import datetime
import time
import pandas as pd
import numpy as np

from CollectClient.collector_utils import get_manager_client_base, get_template_client_base


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
  data_client = get_template_client_base("f5bc963e-eb7b-4361-acad-88d9a50e018b")
  target_df = data_client.data_select(to_df=True)
  # 读数据从excel
  res_inner = target_df[(target_df["月度"] == 1) & (target_df["年度"] == 2022)]
  # source_data = read_data_from_excel()
  # res_inner = pd.merge(source_data, target_df, on=["land_uuid"], how="inner", suffixes=("_s", "_t"))
  # print(res_inner)
  data_client.data_delete(res_inner)
  # data_client.data_create(res_inner)


def creat_data_to_renkou():
  """
  存储人口数据
  """
  data_client = get_template_client_base("f5bc963e-eb7b-4361-acad-88d9a50e018b")
  df = pd.read_csv("/Users/metrodata/Desktop/PyProject/BreezeRpa/CollectClient/ChangSanJiao/现状人口栅格-utf8.csv")
  df = df.rename(columns={"name": "名称", "lon": "经度", "lat": "纬度", "geom": "geometry"})
  df["人口总数"] = df["人口总数"].replace(np.nan, 0).replace(np.inf, 0).astype("int")
  data_client.data_create(df)


def creat_data_to_quekou():
  """
  存储缺口推荐
  """
  data_client = get_template_client_base("a16dd3ee-e994-49b6-8789-f2c1db4a9364")
  df = pd.read_csv("/Users/metrodata/Desktop/PyProject/BreezeRpa/CollectClient/ChangSanJiao/缺口选址推荐表_utf8.csv")
  df = df.rename(columns={"中心点经度": "经度", "中心点纬度": "纬度", "area": "面积", "覆盖面积": "服务面积"})
  df["是否水乡单元"] = df["是否水乡单元"].apply(lambda x: True if x == "是" else False)
  df = data_client.df_drop_columns(df)
  # df["面积"] = df["面积"].replace(np.nan, 0).replace(np.inf, 0).astype("float")
  data_client.data_create(df)


def creat_data_to_quyu():
  """
  存储区域表
  """
  data_client = get_template_client_base("e898098a-1c10-4a72-adb4-89c79896e6a0")
  df = pd.read_csv("/Users/metrodata/Desktop/PyProject/BreezeRpa/CollectClient/ChangSanJiao/区域情况总表_utf8.csv")
  df = df.rename(columns={"是否在水乡客厅": "是否水乡单元"})
  df["是否水乡单元"] = df["是否水乡单元"].apply(lambda x: True if x == "是" else False)
  df = data_client.df_drop_columns(df)
  # df["面积"] = df["面积"].replace(np.nan, 0).replace(np.inf, 0).astype("float")
  data_client.data_create(df)


def creat_data_to_dikuai():
  """
  存储地块表
  """
  data_client = get_template_client_base("59039ac2-9f67-416f-938b-831c79c8fea6")
  df = pd.read_csv("/Users/metrodata/Desktop/PyProject/BreezeRpa/CollectClient/ChangSanJiao/地块信息总表-utf8.csv")
  df = df.rename(columns={"是否在水乡客厅": "是否水乡单元"})
  df["是否水乡单元"] = df["是否水乡单元"].apply(lambda x: True if x == "是" else False)
  df = data_client.df_drop_columns(df)
  # df["面积"] = df["面积"].replace(np.nan, 0).replace(np.inf, 0).astype("float")
  data_client.data_create(df)


def creat_data_to_sheshi():
  """
  存储设施表
  """
  data_client = get_template_client_base("67c038ee-a812-4396-9b61-bb713f3691dc")
  # old_data = data_client.data_select(to_df=True)
  # data_client.data_delete(old_data)
  df = pd.read_csv("/Users/metrodata/Desktop/PyProject/BreezeRpa/CollectClient/ChangSanJiao/1现状设施一览表-utf8.csv")
  df = df.rename(columns={"name": "设施名称", "组团": "组团单元", "规划单元": "控规单元"})
  df = data_client.df_drop_columns(df)
  # df["面积"] = df["面积"].replace(np.nan, 0).replace(np.inf, 0).astype("float")
  data_client.data_create(df)


if __name__ == '__main__':
  # get_temp_man()
  # get_temp_client()
  # run()
  # creat_data_to_renkou()
  # creat_data_to_quekou()
  # creat_data_to_quyu()
  # creat_data_to_dikuai()
  creat_data_to_sheshi()
