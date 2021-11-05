import logging
import os


class LogObj(object):
  __instance = None

  def __new__(cls, *args, **kwargs):
    if cls.__instance is None:
      cls.__instance = object.__new__(LogObj)
    return cls.__instance

  def __init__(self, log_path="Logging/receive_mq.txt"):
    self.creat_dir()
    self.logger = logging.getLogger("receive_topic")
    self.logger.setLevel(logging.DEBUG)
    # 添加文件处理者和流处理者
    self.fh = logging.FileHandler(log_path, encoding="utf-8")
    self.fh.setLevel(logging.DEBUG)
    self.sh = logging.StreamHandler()
    self.sh.setLevel(logging.DEBUG)
    # 设置日志格式
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"  # 日志格式化输出：时间，等级，信息
    DATE_FORMAT = "%Y/%m/%d %H:%M:%S"  # 日期格式.,年月日，时分秒
    formatter = logging.Formatter(fmt=LOG_FORMAT, datefmt=DATE_FORMAT)
    self.fh.setFormatter(formatter)

    # 给日志添加处理者
    self.logger.addHandler(self.sh)
    self.logger.addHandler(self.fh)

  def creat_dir(self):
    if not os.path.exists("Log"):
      os.mkdir("Log")

  def get_logger(self):
    return self.logger
