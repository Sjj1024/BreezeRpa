import stomp
import time
import json
from collector_utils import get_template_client_base
from log_obj import LogObj
from ding_robot import DingRobot

__listener_name = 'SampleListener'
__topic_name = '/topic/IOT_THIRD_WARN'
__host = "60.191.78.86"
__port = 8184
__user = "thrid"
__password = "thrid123"

# __listener_name = 'SampleListener'
# __topic_name = '/topic/IOT_THIRD_WARN'
# __host = "127.0.0.1"
# __port = 61613
# __user = 'admin'
# __password = 'admin'


class Queue_Listener(stomp.ConnectionListener):
  def __init__(self):
    self.conn = conn

  def on_error(self, frame):
    logger.debug('received an error "%s"' % frame)

  def on_message(self, frame):
    logger.debug('received a message "%s"' % frame.body)
    ding_robot.send_msg(f'received a message:{frame.body}')
    try:
      res = json.loads(frame.body)
      res["createTime"] = int(res["createTime"] / 1000)
      data_manager = get_template_client_base(template_uuid="efff8118-4a95-4a1c-a6c4-2b58b3405eda")
      data_manager.data_create([res])
    except Exception as e:
      logger.debug(f"接收消息出错:{e}")

  def on_disconnected(self):
    # 连接失败后的操作
    logger.debug("连接断开了，正在尝试重连......")
    ding_robot.send_msg("连接断开了，正在尝试重连......")
    self.conn = connect_and_subscribe()


def connect_and_subscribe():
  global conn
  conn = stomp.Connection10([(__host, __port)], reconnect_attempts_max=-1)
  conn.set_listener("SampleListener", Queue_Listener())
  conn.connect(username=__user, passcode=__password, wait=True)
  conn.subscribe(__topic_name, ack='auto', id="1")
  return conn


def start():
  logger.debug("receive topic server start.....")
  while True:
    logger.debug(f"开始检测链接是否正常：{conn.is_connected()}")
    ding_robot.send_msg(f"开始检测链接是否正常:{conn.is_connected()}")
    time.sleep(60)


if __name__ == '__main__':
  # 存储log日志的位置
  log_path = "Log/receive_mq.txt"
  logger = LogObj(log_path).get_logger()
  ding_robot = DingRobot()
  conn = connect_and_subscribe()
  start()
