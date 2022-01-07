import cx_Oracle
from petal import Task
from petal.util.db import DBEngineX
from petal_tasks.collector_tools.collector_utils import get_template_client_base
import pandas as pd

huamu_sql_flow = """
select fh.NAME                   上报人,
       fh.MEETING_DECISION       会议决策,
       fh.MEETING_ACCESSORY_PATH 会议图片,
       fh.MEETING_ADDRESS        会议地址,
       fh.MEETING_OPINION        会议意见,
       fh.MEETING_TIME           会议时间,
       hf.DISPOSE_ACCESSORY_PATH 处理图片,
       fh.COMMENTS               处理意见,
       fh.ACCOUNT_NAME           操作人员,
       hd.DEPT_NAME              操作部门,
       fh.CREATE_TIME            更新时间,
       fh.STATUS                 案件状态,
       hf.ID                     案件编号,
       fh.SIGN                   联动等级,
       hf.PICTURE_ACCESSORY_PATH 问题图片,
       fh.COMMENTS               问题描述,
       fh.TAGS                   被流转操作
from HUAMUJIEDAO.FLOWEVENT_HIS fh
         left join HUAMUJIEDAO.FLOWEVENT hf on fh.ID = hf.ID
         left join HUAMUJIEDAO.DEPT hd on hd.ID_ = fh.ID
"""


class HuaMuFlow(Task):
  """
  花木案件流转：
  从Collector取最后时间，
  从HUAMUJIEDAO拿这个时间点之后的数据
  再将新数据存到Collector中
  """

  def run(self):
    (
      self.new_etl()
        .from_sql(sql=huamu_sql_flow, dbe=self.get_db())
        .call_with_df(self.to_collector, "695ae7db-6bc9-42d6-ae5d-c41111ceacbb")
    )

  @staticmethod
  def get_db():
    host = '58.215.228.138'
    port = 6130
    user = 'hmjd'
    passwd = 'hmjd'
    service_name = 'orcl.wx'
    dsn = cx_Oracle.makedsn(host, port, service_name=service_name)
    dsn = f'oracle+cx_oracle://{user}:{passwd}@{dsn}'
    db = DBEngineX.from_url(dsn)
    return db

  @staticmethod
  def to_collector(df, template_id):
    data_mgr = get_template_client_base(template_uuid=template_id)
    old = data_mgr.data_select(to_df=True)
    if not old.empty:
      # 如果有历史数据，就取出最后的历史时间
      last_time = old["更新时间"].max()
      last_time = pd.to_datetime(last_time, unit='s').to_datetime64()
      df = df[df["更新时间"] > last_time]
    # 将图片转为数组存储到Collector
    df["会议图片"] = [[pic] if pic else [''] for pic in df["会议图片"]]
    df["处理图片"] = [[pic] if pic else [''] for pic in df["处理图片"]]
    df["问题图片"] = [[pic] if pic else [''] for pic in df["问题图片"]]
    df = data_mgr.df_drop_columns(df)
    data_mgr.data_create(df)