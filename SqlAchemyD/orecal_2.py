from sqlalchemy import Column, String, Integer, DateTime, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class JobPlan(Base):
    """
    定义一张表
    """
    __tablename__ = "job_plan"

    id = Column(Integer, primary_key=True, nullable=False)
    row_stamp = Column(Integer, nullable=False, default=0)


# 大写部分替换成真实的 Oracle信息
# dsn = "oracle+cx_oracle://hmjd:hmjd@58.215.228.138:6130/?service_name=orcl.wx"
dsn = "oracle+cx_oracle://system:oracle@localhost:1521/?XE"
engine = create_engine(dsn)
# 创建一张表
# 不会重新创建已经存在的表
Base.metadata.create_all(engine)
