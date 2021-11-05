import cx_Oracle
from sqlalchemy import create_engine, String
import pandas as pd

# engine = create_engine("oracle+cx_oracle://hmjd:hmjd@58.215.228.138:6130/HUAMUJIEDAO")
engine = create_engine("oracle+cx_oracle://hmjd:hmjd@58.215.228.138:6130/?service_name=orcl.wx")
sql_string = """
select f.ID                      事件编号,
       f.NAME                    上报人,
       f.PHONE                   联系电话,
       f.ADDRESS                 事发地址,
       f.STATUS                  当前状态,
       r.REGION_NAME             所数居委,
       f.CREATE_TIME             立案时间,
       f.LATITUDE                纬度,
       f.LONGITUDE               经度,
       f.DISPOSE_OPINION         结案意见,
       f.END_TIME                结案时间,
       f.THE_MATTERS_BIG_NAME    问题大类,
       f.THE_MATTERS_SMALL_NAME  问题小类,
       f.COMMENTS                问题详情
from HUAMUJIEDAO.FLOWEVENT f
         left join HUAMUJIEDAO.REGION r on f.DATA_AREA_CODE = r.REGION_CODE
"""

res = engine.execute(sql_string)
print(res.fetchall())

# patel_task 连接orcle数据库
# host = '58.215.228.138'
# port = 6130
# user = 'hmjd'
# passwd = 'hmjd'
# service_name = 'orcl.wx'
# dsn = cx_Oracle.makedsn(host, port, service_name=service_name)
# dsn = f'oracle+cx_oracle://{user}:{passwd}@{dsn}'
# print('dsn: ', dsn)
# db = DBEngineX.from_url(dsn)
# res = db.execute("select count(*) from HUAMUJIEDAO.FLOWEVENT")
# print(res.fetchall())


# import cx_Oracle
# from sqlalchemy import create_engine
#
# ip = '58.215.228.138'
# port = '6130'
# uname = 'hmjd'  # 用户名
# pwd = 'hmjd'  # 密码
# tnsname = 'orcl.wx'  # 实例名
#
# dsnStr = cx_Oracle.makedsn(ip, port, service_name=tnsname)
# connect_str = "oracle://%s:%s@%s" % (uname, pwd, dsnStr)
# engine = create_engine(connect_str)
# sql_string = "select count(*) from HUAMUJIEDAO.FLOWEVENT"
# res = engine.execute(sql_string)
# print(res.fetchall())

# conn = cx_Oracle.connect("hmjd:hmjd@58.215.228.138:6130")
# conn = cx_Oracle.connect("hmjd/hmjd@58.215.228.138:6130/orcl.wx")
# # 使用cursor()方法获取操作游标
# cursor = conn.cursor()
# res = cursor.execute("select count(*) from HUAMUJIEDAO.FLOWEVENT")
# print(res.fetchall())

# dsn = cx_Oracle.makedsn("58.215.228.138", 6130, service_name="orcl.wx")
# connection = cx_Oracle.connect(user="hmjd", password="hmjd",
#                                dsn=dsn,
#                                encoding="UTF-8")
