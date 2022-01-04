import datetime
import pandas as pd
from petal import Task
from petal_tasks.collector_tools.collector_utils import get_template_client_base


class HuaMuMidFunds(Task):

  def run(self):
    """
    党费中间表，根据党组织编号对党费进行管理
    """
    data = get_template_client_base(template_uuid="47100530-2e14-481b-8613-86062f609a16").data_select(to_df=True)
    mid_df = pd.DataFrame(columns=('所属党组织', '所属党组织编号', '党费收缴总额', "已完成缴纳月数", "已缴纳人次"))
    self.get_funds_count(data, mid_df)

  def get_funds_count(self, data: pd.DataFrame, mid_df: pd.DataFrame):
    """
    获取当月党费收缴总额
    """
    month = datetime.datetime.now().month
    current_mouth = data[data["月度"] == month]
    agg = current_mouth.groupby(["所属党组织", "所属党组织编号"]).sum()["本月实缴金额"]
    for index, row in agg.iterrows():
      mid_df.append([{"所属党组织": index[0], "所属党组织编号": index[1], "本月实缴金额": row["本月实缴金额"]}])

  def get_month_count(self, data: pd.DataFrame):
    """
    已完成缴纳的月数
    """
    agg = data.groupby(["所属党组织", "月度"]).agg({"本月实缴金额": ["sum"], "本月缴费基数": ["sum"]})
