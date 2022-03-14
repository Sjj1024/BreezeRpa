#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
  "mysql+pymysql://root:123456@127.0.0.1:3306/local_database?charset=utf8mb4",
  echo=True,  # 设置日志记录方式，可以看到sql
  max_overflow=5)  # 指定连接池最大连接数
Base = declarative_base(engine)  # SQLORM基类
session = sessionmaker(engine)()  # 构建session对象


class Student(Base):
  __tablename__ = 'Student'  # 表名
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50))
  age = Column(Integer)
  sex = Column(String(10))

  def to_json(self):
    dict_str = self.__dict__
    if "_sa_instance_state" in dict_str:
      del dict_str["_sa_instance_state"]
    return dict_str


def creat_table():
  Base.metadata.create_all()  # 将模型映射到数据库中


def add_student():
  student = Student(name='Tony', age=18, sex='male')  # 创建一个student对象
  session.add(student)  # 添加到session
  session.commit()  # 提交到数据库
  session.add_all([
    Student(name='Jane', age=16, sex='female'),
    Student(name='Ben', age=20, sex='male')
  ])
  session.commit()


def query_student():
  item_list = session.query(Student).all()
  json_list = [i.to_json() for i in item_list]
  print(json_list)


if __name__ == '__main__':
  # creat_table()
  # add_student()
  query_student()
