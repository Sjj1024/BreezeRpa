import datetime
import pandas as pd
from petal import Task
from petal_tasks.collector_tools.collector_utils import get_template_client_base


class HuaMuFunds(object):

  def run(self):
    """
    从党员基本信息获取数据,筛选正式在册党员,得到新的数据
    """
    source_data = self.get_data_from_base()
    clean_data = self.transform_data(source_data)
    self.to_collector(clean_data)

  def get_data_from_base(self):
    """
    从党员基本信息获取数据
    """
    data_mgr = get_template_client_base(template_uuid="6c18d1b6-406e-4961-965c-c4b9cfc14cc4")
    # 将数据转化为df
    old = data_mgr.data_select(to_df=True)
    # 筛选正式在册党员
    new = old.loc[(old['是否在册党员']) & (old['党员身份'] == "正式党员")]
    return new

  def get_data_from_feature(self):
    """
    从党费管理里面拿出数据
    """
    time_date = datetime.date.today()
    data_mgr = get_template_client_base(template_uuid="47100530-2e14-481b-8613-86062f609a16")
    # 将数据转化为df
    feature = data_mgr.data_select(to_df=True)
    # 筛选出本年度的所有数据
    feature = feature[feature["年度"] == time_date.year]
    feature.drop(["年度汇总金额"], axis=1, inplace=True)
    # 按照党员编号分组合并本年度党费的和
    feature = feature.groupby("党员编号").sum().rename(columns={"本月实缴金额": "年度汇总金额"})
    # 仅保留党员编号和年度汇总金额
    feature = feature[["年度汇总金额"]]
    return feature

  def transform_data(self, data):
    new_df = pd.DataFrame()
    new_df["所属党组织"] = data["所属党组织名称"]
    new_df["所属党组织编号"] = data["党组织编号"]
    new_df["本月缴费基数"] = data["月缴纳基数"]
    new_df["党员编号"] = data["党员编号"]
    new_df["姓名"] = data["姓名"]
    time_date = datetime.date.today()
    new_df["年度"] = time_date.year
    new_df["月度"] = time_date.month
    new_df["本月实缴金额"] = 0
    new_df["缴费时间"] = 0
    # 从主表拿出数据，统计年度汇总金额
    feature_data = self.get_data_from_feature()
    # 按照左关联合并党员基本信息和党费管理
    df3 = new_df.merge(feature_data, how="left", on="党员编号")
    # 将空值填充0
    df3.fillna(0, inplace=True)
    return df3

  def to_collector(self, data):
    data_manager = get_template_client_base(template_uuid="47100530-2e14-481b-8613-86062f609a16")
    data_manager.data_create(data)


if __name__ == '__main__':
  HuaMuFunds().run()
