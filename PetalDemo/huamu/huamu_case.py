import cx_Oracle
import numpy as np
import pandas as pd
from petal import Task
from mdt_util.const import SRS
from petal.util.db import DBEngineX
from petal_tasks.collector_tools.collector_utils import get_template_client_base

huamu_sql_zmy = """
select f.ID                     案件编号,
       f.NAME                   上报人,
       f.PHONE                  联系电话,
       f.ADDRESS                事发地址,
       f.STATUS                 当前状态,
       r.REGION_NAME            所属居委,
       f.CREATE_TIME            立案时间,
       f.LATITUDE               纬度,
       f.LONGITUDE              经度,
       f.DISPOSE_OPINION        结案意见,
       f.END_TIME               结案时间,
       f.THE_MATTERS_BIG_NAME   问题大类,
       f.THE_MATTERS_SMALL_NAME 问题小类,
       f.COMMENTS               问题详情,
       d.DEPT_NAME              主责部门
from HUAMUJIEDAO.FLOWEVENT f
         left join HUAMUJIEDAO.REGION r on f.DATA_AREA_CODE = r.REGION_CODE
         left join HUAMUJIEDAO.DEPT d on f.DEPT_ID = d.ID_
"""


class HuaMuZMY(Task):
  """
  花木自免疫案件
  """

  def run(self):
    # 创建一个etl
    # 从数据库获取
    # 重命名
    # 存储到Collector
    (self.new_etl()
     .from_sql(sql=huamu_sql_zmy, dbe=self.get_db())
     .typecast(["经度", "纬度"], type=float)
     .coord_transform(from_srs=SRS.gcj02, to_srs=SRS.wgs84, c_lng="经度", c_lat="纬度")
     .call_with_df(self.to_collector, "13f63902-38e2-40f3-b291-0059509bdd01")
     )

  @staticmethod
  def to_collector(df, template_id):
    data_mgr = get_template_client_base(template_uuid=template_id)
    # 将历史数据状态设置为False
    old = data_mgr.data_select(to_df=True)
    old["状态"] = False
    old_df = pd.DataFrame({"id": old["id"], "状态": old["状态"]})
    data_mgr.data_update_separate(old_df)
    # 新数据去重并设置状态为True
    df["状态"] = True
    df = data_mgr.df_drop_columns(df)
    df.drop_duplicates(subset=['案件编号'])
    data_mgr.data_create(df)

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
