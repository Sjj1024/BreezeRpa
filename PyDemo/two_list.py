import time
from time import sleep
from tqdm import *


def buji():
  print("补集")
  a_list = [1, 2, 3, 4, 5]
  b_list = [1, 4, 5]
  # 方法1
  # ret_list = list(set(a_list) ^ set(b_list))
  # 方法2
  ret_list = list(set(a_list).difference(set(b_list)))
  # ret_list = list(set(b_list).difference(set(a_list)))
  print(ret_list)
  print(tuple(ret_list))
  for index, value in enumerate(a_list):
    print(index, value)


def jiaoji():
  print("交集")
  a_list = [1, 2, 3, 4, 5]
  b_list = [1, 4, 5]
  res_list = list(set(a_list).intersection(set(b_list)))
  print(res_list)


def bingji():
  print("并集")
  a_list = [1, 2, 3, 4, 5]
  b_list = [1, 4, 5]
  res_list = list(set(a_list).union(set(b_list)))
  print(res_list)


def meige_num():
  num_list = [1, 4, 6, 7, 8, 89, 2, 2, 4, 6, 7, 2, 3, 4, 23, 5, 6, 2, 2]
  # 查找重复数据
  num_set = set(num_list)
  for n in num_set:
    if num_list.count(n) > 1:
      print(f"重复数据有: {n}")
  buffer_list = []
  for index, value in enumerate(num_list):
    buffer_list.append(value)
    if (index + 1) % 5 == 0 or (index + 1) == len(num_list):
      print(index, buffer_list)
      buffer_list.clear()


def map_fillter():
  some_dict = {
    "name": "wang",
    "age": "19"
  }
  if "19" in some_dict:
    print("在里面")


def creat_alter_table():
  # 快速生成一个改变表结构的数据
  collector_to_mysql = {
    "园区基本信息wb1207": "YQJBXX",  # 园区基本信息
    "楼宇基本信息0308": "LYJBXX",  # 楼宇基本信息
    "静安全量企业": "JAQLQY",  # 静安全量企业
    "全量楼宇_面": "JAQLLY",  # 静安全量楼宇
    "静安区税收_月度累计税收总额": "JAQYDLJSS",  # 静安区月度累计税收
    "静安区税收_楼宇年度累计税收": "JAQLYNDLJSS",  # 静安区楼宇年度累计税收
    "一楼一图_楼层结构属性": "JALYLCMX",  # 静安楼宇楼层明细
    "静安_安商_记录表": "ZDQYASWSQYFXBG",  # 重点企业安商稳商企业风险变更
    "静安_安商_企业表": "ZDQYASWSQY",  # 重点企业安商稳商企业
    "静安-安商-需求表": "ZDQYASWSQYXQJL",  # 重点企业安商稳商企业需求记录
    "静安_安商_走访事件表": "ZDQYASWSZFJL",  # 重点企业安商稳商走访记录
    "静安领导驾驶舱-企业采核表": "JAQYJYDCHJL",  # 静安企业经营地采核记录
    "静安领导驾驶舱-园区空置信息": "JALYYQKZXX",  # 静安楼宇园区空置信息
    "静安_引进_走访事件表": "XYJZDXMZFJL",  # 新引进重大项目走访记录
    "静安_引进_企业表": "XYJZDXM"  # 新引进重大项目
  }
  for table_name in collector_to_mysql.values():
    print(f"""
    truncate table {table_name};
    alter table {table_name}
    drop primary key,
    add column ID int,
    add primary key (ID);""")

  # 删除表


def jindutiao():
  for i in tqdm(range(20)):
    sleep(0.5)

  # 不带提示文字，带索引
  for i, v in enumerate(tqdm(range(20))):
    # print(i, v)
    sleep(0.05)

  # 带提示文字
  for i in tqdm(range(100), desc='Processing'):
    time.sleep(0.05)

  # 带提示文字和索引的进度条
  for i, v in enumerate(tqdm(range(100), desc='Processing')):
    # print(i, v)
    time.sleep(0.01)


def error_list():
  list_e = [[20579, '2022-02-16 09:36:44', '正常', '0', '测试公司', '区投资办', '[{"单位": "区发展改革委", "姓名": "测试", "联系方式": "2"}]',
             '2021-12-21 00:00:00', '测试一下下一秒就可以了😌，我们的生活方式是什么时候回来的时候才发现自己的', '0',
             '["33bf3837adfd12cfd456bb7a547059fb", "787df79308911a55464eecfe76412e81"]', '2021-12-21 06:21:05',
             '2021-12-21 06:21:05'],
            [20580, '2022-02-16 09:36:44', '正常', '0', '师南客（上海）贸易有限公司', '南西功能区',
             '[{"单位": "南西功能区", "姓名": "吴家麟", "联系方式": "18019118679"}, {"单位": "南西功能区", "姓名": "殷程女一", "联系方式": "13761532490"}]',
             '2021-12-16 00:00:00',
             '该企业今年被逸仙电商收购以后，办公室已搬迁至徐汇。今年企业销售情况较好，双十一期间销售额过亿，天猫旗舰店卸妆膏排名第二。企业总体上还是希望能长期在静安发展，目前正在进行历年税收情况统计以及未来三年税收情况测算，希望等测算报表完成以后能与区里申请相应扶持政策。南西功能区将持续跟进，做好安商稳商工作。',
             '91310000MA1FYD9Q37', '0', '2021-12-21 07:00:52', '2021-12-21 07:00:52'],
            [20581, '2022-02-16 09:36:44', '正常', '0', '上海铧福创盛置业有限公司', '市北功能区',
             '[{"单位": "市北功能区", "姓名": "陈军", "联系方式": "56770133"}, {"单位": "市北功能区", "姓名": "宣晨炜", "联系方式": "13816916620"}]',
             '2021-12-21 00:00:00',
             '今天与陈军总裁走访了上海铧福创盛置业有限公司的刘总和陈总，沟通企业准备迁移的情况。企业表示目前的情况是企业总部在珠海横琴可以享受到个调税部分30%的财政奖励，华发集团希望上海的平台公司也可以在本地在相关政策有一些平衡的方式，让企业的员工也可以享受相关政策。企业目前跟上海临港新区沟通，临港给企业个调税纳税总额的17%作为财政奖励。今天上门沟通之后，我们争取企业暂时不做迁移的动作，需要政府对该政策进行反馈，并尽快反馈给企业，希望尽量可以留住企业。',
             '91310106312594987Q', '["f4a3a6190a587d02a8ecc6f80ab171cb"]', '2021-12-21 09:28:04',
             '2021-12-21 09:11:45'],
            [20582, '2022-02-16 09:36:44', '正常', '0', '戴比尔斯珠宝商贸（上海）有限公司', '静安寺街道',
             '[{"单位": "静安寺街道", "姓名": "何晓航", "联系方式": "13062818616"}]', '2021-12-21 00:00:00',
             '跟企业进行了电话沟通，分别是行政人员张小姐、财务人员孙小姐。目前公司因经营业务需要，申请电子执照，准备在静安区设立分公司。街道也提出可以帮忙指导一网通办等服务，企业表示后续有需求会联系街道。',
             '91310000569603682E', '0', '2021-12-21 09:36:52', '2021-12-21 09:36:52'],
            [20583, '2022-02-16 09:36:44', '正常', '0', '上海其晓国际贸易有限公司', '北站街道',
             '[{"单位": "北站街道", "姓名": "郑勇", "联系方式": "63818827"}, {"单位": "北站街道", "姓名": "赵靓", "联系方式": "63818827"}]',
             '2021-12-16 00:00:00', '经走访，企业反应由于税务要求百万元发票将至十万元发票，影响企业正常经营，希望区相关部门能帮忙协调该情况。', '913101060885644915', '0',
             '2021-12-22 02:29:47', '2021-12-22 02:29:47']]


def emo_test():
  import emoji

  print(emoji.emojize('Python is :thumbs_up:'))
  print(emoji.emojize('Python is :thumbsup:', use_aliases=True))  # 使用别名
  print(emoji.demojize('Python is 👍'))


if __name__ == '__main__':
  # jiaoji()
  # bingji()
  # buji()
  # meige_num()
  # map_fillter()
  # creat_alter_table()
  # jindutiao()
  emo_test()