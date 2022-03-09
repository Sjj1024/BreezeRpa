import pandas as pd
import pymysql
from tqdm import tqdm


class CollectorToSql:
  def __init__(self, data: pd.DataFrame, table_name: str, unique_field: str, field_mapping):
    self.data = data
    self.table_name = table_name
    self.unique_field = unique_field
    self.field_mapping = field_mapping
    self.conn = None
    self.cursor = None

  def get_db_engine(self):
    # conn = pymysql.connect(
    #   host="12.113.231.49",
    #   port=3306,
    #   user="qxzfwzxlydt",
    #   password="!QAZ2wsx",
    #   database="qxzfwzxlydt"
    # )
    conn = pymysql.connect(
      host="127.0.0.1",
      port=3306,
      user="root",
      password="123456",
      database="jingan"
    )
    return conn

  def close_conn(self):
    self.cursor.close()
    self.conn.close()

  def truncate_table(self):
    self.conn = self.get_db_engine()
    self.cursor = self.conn.cursor()
    sql = f"truncate table {self.table_name}"
    try:
      self.cursor.execute(sql)
      print(f"\n同步的表名称：{self.table_name}")
    except Exception as e:
      print(f"执行SQL出错: {sql}, 错误原因:{e}")
      self.conn.rollback()

  def insert_and_update(self):
    """
    向数据库中插入新数据或更新旧数据，每100条执行一次
    """
    self.conn = self.get_db_engine()
    self.cursor = self.conn.cursor()
    keys = self.data.keys()
    values = self.data.values.tolist()
    key_sql = ",".join(keys)
    update_sql = ",".join([f"{key}=values({key})" for key in keys])
    buffer_list = []
    for index, value in enumerate(tqdm(values, desc="数据同步进度:")):
      buffer_list.append([str(i).strip().replace("\'", '"') if isinstance(i, (list, str)) else i for i in value])
      if (index + 1) % 100 == 0 or (index + 1) == len(values):
        value_sql = ','.join(['%s'] * self.data.shape[1])
        sql_str = f"insert into {self.table_name}({key_sql}) values ({value_sql}) on duplicate key update {update_sql}"
        try:
          self.cursor.executemany(sql_str, buffer_list)
          self.conn.commit()
        except Exception as e:
          print(f"执行SQL出错: {sql_str}, 错误原因:{e}")
          self.conn.rollback()
        buffer_list.clear()
    self.close_conn()

  def run(self):
    self.truncate_table()
    self.insert_and_update()
