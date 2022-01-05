import datetime
import pandas as pd
from petal_tasks.collector_tools.collector_utils import get_template_client_base


class HuaMuMidFunds(object):

  def run(self):
    """
    党费中间表，根据党组织编号对党费进行管理
    """
    data = get_template_client_base(template_uuid="47100530-2e14-481b-8613-86062f609a16").data_select(to_df=True)
    mid_df = pd.DataFrame(columns=('所属党组织', '所属党组织编号', '党费收缴总额', "已完成缴纳月数", "已缴纳人次"))
    mid_df = self.get_funds_total(data, mid_df)
    mid_df = self.get_month_count(data, mid_df)
    mid_df = self.get_paid_person(data, mid_df)

  def get_funds_total(self, data: pd.DataFrame, mid_df: pd.DataFrame):
    """
    获取当月党费收缴总额
    """
    # month = datetime.datetime.now().month
    month = 12
    current_mouth = data[data["月度"] == month]
    # agg = current_mouth.groupby(["所属党组织", "所属党组织编号"]).sum()["本月实缴金额"]
    agg = current_mouth.groupby(["所属党组织", "所属党组织编号"]).agg({"本月实缴金额": ["sum"]})
    for index, row in agg.iterrows():
      mid_df = mid_df.append([{"所属党组织": index[0], "所属党组织编号": index[1], "本月实缴金额": row["本月实缴金额"][0]}])
    return mid_df

  def get_month_count(self, data: pd.DataFrame, mid_df: pd.DataFrame):
    """
    已完成缴纳的月数
    """
    dang_funds = {}
    agg = data.groupby(["所属党组织", "月度"]).agg({"本月实缴金额": ["sum"], "本月缴费基数": ["sum"]})
    for index, row in agg.iterrows():
      if row["本月实缴金额"][0] == row["本月缴费基数"][0]:
        dang_funds[index[0]] = dang_funds.get(index[0], 0) + 1
    print(dang_funds)
    mid_df.set_index(["所属党组织"], inplace=True)
    for key, value in dang_funds.items():
      mid_df.loc[key, "已完成缴纳月数"] = value
    print(mid_df)
    return mid_df

  def get_paid_person(self, data: pd.DataFrame, mid_df: pd.DataFrame):
    """
    获取已缴纳人次
    :return:
    """
    person_paid = {}
    agg = data.groupby(["所属党组织", "月度"]).agg({"本月实缴金额": ["sum"], "本月缴费基数": ["sum"]})
    for index, row in agg.iterrows():
      if row["本月实缴金额"][0] == row["本月缴费基数"][0]:
        person_paid[index[0]] = person_paid.get(index[0], 0) + 1
    print(dang_funds)
    mid_df.set_index(["所属党组织"], inplace=True)
    for key, value in dang_funds.items():
      mid_df.loc[key, "已完成缴纳月数"] = value
    print(mid_df)
    return mid_df


if __name__ == '__main__':
  huamu_ele = HuaMuMidFunds()
  huamu_ele.run()
