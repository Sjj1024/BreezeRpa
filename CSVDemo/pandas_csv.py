#!/usr/bin/env python

# -*- coding: utf-8 -*-

# @File  : ImportDataToMysql.py

# @Author: Small-orange

# @Date  : 2019-12-13

# @Desc  :将Excel中的数据导入到Mysql数据库中

# 1.创建数据库连接

# 2.测试数据库连接

# 3.读入数据

# 4.将数据写入数据库

import pandas as pd

from sqlalchemy import create_engine, String

import time

# 创建数据库连接
start = time.time()

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/local_database?charset=utf8')

# 读取表--测试数据库连接

# result = pd.read_sql_table('testdemo_test', con=engine)

# 读入Excel中的数据

# file_name = '/Users/metrodata/Downloads/customer_info.csv'
file_name = 'person.csv'

# 分块读取多少行chunksize
data = pd.read_csv(file_name, chunksize=2, skiprows=3)
# data.to_sql('BI招聘岗位信息',con=engine,if_exists='append')

for chunk in data:
    # 将读取的数据写入Mysql,dtype：执行数据类型,如果是字典，就会按照对应列指定,否则可能会让pd猜错，而导致存储失败
    chunk.to_sql('customer_info', con=engine, if_exists='append', dtype=String(60))
    print("正在添加数据......")

end = time.time()

print('运行时间：', end - start)

print('--success--')
