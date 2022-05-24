import logging
import os
import pkgutil
import sys
from logging.handlers import RotatingFileHandler

from flask import Flask, Blueprint
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis

from config import config

# 给变量加注释，让其可以自动提示
redis_store = None  # type: StrictRedis


# 下面这种也是一样的，变量提示，后面引入之后也可以自动获取提示
# redis_store: StrictRedis = None


def setup_log(log_level):
    # 没有日志文件夹就自动创建
    path = os.path.join(os.getcwd(), "logs")
    if not os.path.exists(path):
        os.mkdir(path)
    # 设置日志的记录等级
    logging.basicConfig(level=log_level)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(asctime)s [%(module)s] %(levelname)s [%(lineno)d] %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def search_blueprint(app: Flask):
  """
  扫描蓝图，并自动注入app中
  """
  app_dict = {}
  pkg_list = pkgutil.walk_packages(__path__, __name__ + ".")
  for _, module_name, ispkg in pkg_list:
    __import__(module_name)
    module = sys.modules[module_name]
    module_attrs = dir(module)
    for name in module_attrs:
      var_obj = getattr(module, name)
      if isinstance(var_obj, Blueprint):
        if app_dict.get(name) is None:
          app_dict[name] = var_obj
          app.register_blueprint(var_obj)
          print(" * 注入 %s 模块 %s 成功" % (Blueprint.__name__, var_obj.__str__()))


def creat_app(con: str):
    # 将业务代码抽离出来
    app = Flask(__name__)
    # 可以通过设置环境变量配置不同的环境
    config_env = os.environ.get("config")
    if config_env is not None:
        con = config_env
    app.config.from_object(config[con])
    # 初始化数据库
    db = SQLAlchemy()
    db.init_app(app)
    # 日志等级配置
    setup_log(config[con].LOG_LEVEL)
    # 设置session保存位置: 配置对象里面的属性是类属性
    global redis_store
    redis_store = StrictRedis(host=config[con].REDIS_HOST, port=config[con].REDIS_PORT)
    # 可以指定session的保存位置，要在app的config中配置
    Session(app)
    # 开启CSRF保护
    CSRFProtect(app)
    # 注册蓝图,放到这里就不会出现导入redis_store出错的问题:什么时候使用，什么时候导入
    search_blueprint(app)
    return app
