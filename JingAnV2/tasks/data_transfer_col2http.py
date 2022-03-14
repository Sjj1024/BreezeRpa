import logging
from datetime import datetime
from uuid import uuid4

import requests
from mdt_util.enum import StrEnum
from redis import Redis
from sqlalchemy import func
from sqlalchemy import select

from petal import Task
from petal import step
from petal.base.error import InvalidDataError
from petal.util import db


class CatLevel(StrEnum):
  level1 = '事件'
  level2 = '营商环境需求'
  level3 = '配套服务'


MAX_RETRY = 3

REDIS_KEY_PREV = 'ID_JaDataTransCollect2http_START_PREV'
REDIS_KEY_NEXT = 'ID_JaDataTransCollect2http_START_NEXT'
# URL_POST_DISP = 'http://10.101.45.60:8085/paidan_data_route/processedData/upload' # for test
URL_POST_DISP = 'http://10.89.1.161/paidan_data_route/processedData/upload'
ERR_LIMIT = 100
log_filepath = f'/mnt/log_file_order/jaDTC{datetime.today().date()}.log'

# logging.basicConfig(filename=log_filepath,
#                     level=logging.INFO,
#                     format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')


class JaDataTransCollect2http(Task):
  """
  静安派单数据推送, deployed in 12.113.231.52 running every 15min by cron
  docker-compose 在52机器的 /data/etl下，redis做了持久化
  注意: 迁移项目时要先记下两个redis_key的对应值(collector表的row_id)，并且在新的redis环境设置好,
  然后关掉cron 的定时推送
  till 20211124 :
  ID_JaDataTransCollect2http_START_PREV: 238
  ID_JaDataTransCollect2http_START_NEXT: 239
  """

  @classmethod
  def get_arg_parser(cls):
    parser = Task.get_cls_arg_parser(cls)
    parser.add_argument('--template_name', type=str, default='data-a186ef27-f40d-45b9-882b-8c5487466d90')

    return parser

  def init(self):
    self.from_tbl_name = self.p.template_name
    self.from_dbe = db.get_engine_from_config(key='/global/postgres/collector_rw')
    self.from_schema = 'collector'
    self.redis_client = Redis(host='petal-redis',
                              port=6379,
                              db=0,
                              socket_connect_timeout=5)
    self.error_limit = 0

  @step(order=10)
  def run(self):
    self.from_tbl = self.from_dbe.reflect_table(self.from_tbl_name,
                                                schema=self.from_schema)

    self.head_id = self.redis_client.get(REDIS_KEY_NEXT)
    if not self.head_id:
      self.head_id = -1
    else:
      self.head_id = int(self.head_id.decode('utf-8'))

    self.top_id = self.from_dbe.execute(
        select([func.max(self.from_tbl.c.id)]),
        scalar=True
    )
    if self.top_id <= self.head_id:
      logging.error(f'当前数据已是最新 {self.top_id}')
      return
    else:
      logging.info(f'由第{self.head_id}条开始')

    extract_sql = select([self.from_tbl.c.id,
                          self.from_tbl.c.update_time,
                          self.from_tbl.c.extra]).where(self.from_tbl.c.id > self.head_id)

    (
      self.new_etl(stream=False)
          .set_options(chunksize=30000)
          .from_sql(extract_sql, self.from_dbe)
          .pipe(self.post_all_orders)
    )

    if self.error_limit < ERR_LIMIT:
      self.redis_client.set(REDIS_KEY_NEXT, self.top_id)
      self.redis_client.set(REDIS_KEY_PREV, self.head_id)
      res = f'同步完成，next id is {self.top_id}'
      logging.info(res)
    else:
      res = f'失败次数过多，同步终止, curr_id is {self.head_id}',
      logging.error(res)

  def post_all_orders(self, df):
    df.sort_values('id', inplace=True)
    # remove redundancy in terms of source.Id
    df['src_id'] = df.apply(lambda row: dict(row['extra'])['source']['Id'], axis=1)
    df.drop_duplicates(['src_id'], inplace=True)
    df.drop(columns=['src_id', 'update_time'],inplace=True)
    df.apply(lambda row: self.post_order_dispatching(row), axis=1)
    return df

  def post_order_dispatching(self, row):
    counter = MAX_RETRY
    if self.error_limit > ERR_LIMIT:
      logging.error("limit reached: %d", self.error_limit)
      return
    while counter:
      try:
        dct_data = row['extra']
        if 'pdId' in dct_data:
          dct_data.pop('pdId')
        dct_data['jkId'] = str(uuid4()).replace('-', '')
        dct_data['address'] = dct_data.get('address', '上海市')
        resp = requests.post(url=URL_POST_DISP, json=dct_data, timeout=8)
        if resp.status_code != 200:
          raise InvalidDataError(message=f'status: {resp.status_code}',
                                 data=f"resp: {resp.text}"
                                      f"body: {dct_data}")
        logging.info(f'result: {resp.text}')
        resp = resp.json()
        if not resp['code']:
          logging.info(f"post succeed: id {dct_data['source']['Id']}")
      except requests.exceptions.Timeout:
        counter -= 1
        self.error_limit += 1
      else:
        if resp['code'] != 0:
          logging.error(f"err_msg: f{resp['message']}, id:{dct_data['source']['Id']}, data: f{row}")
          counter -= 1
          self.error_limit += 1
        else:
          break
