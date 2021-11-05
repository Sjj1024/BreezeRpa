import socket
import threading

import stomp
import time
import json
from ActiveMQ.log_obj import LogObj
from collector_utils import get_template_client_base

# nc -vz -w 2 60.191.78.86 8184

__topic_name = '/topic/IOT_THIRD_WARN'
__host = "60.191.78.86"
__port = 8184
__user = "thrid"
__password = "thrid123"


# __topic_name = 'SampleQueue'
# __topic_name = 'SampleTopic'
# __host = "127.0.0.1"
# __port = 61613
# __user = 'admin'
# __password = 'admin'


class Queue_Listener(stomp.ConnectionListener):
  def __init__(self, conn):
    self.conn = conn

  def on_error(self, frame):
    print('received an error "%s"' % frame)
    logger.debug('received an error "%s"' % frame)

  def on_message(self, frame):
    print('received a message "%s"' % frame.body)
    logger.debug('received a message "%s"' % frame.body)
    try:
      res = json.loads(frame.body)
      # res["createTime"] = int(res["createTime"] / 1000)
      # data_manager = get_template_client_base(template_uuid="efff8118-4a95-4a1c-a6c4-2b58b3405eda")
      # data_manager.data_create([res])
    except Exception as e:
      print(f"接收消息出错:{e}")
      logger.debug(f"接收消息出错:{e}")

  def on_disconnected(self):
    # 连接失败后的操作
    print('connection......')
    logger.debug("connection......")
    connect_and_subscribe(self.conn)


def connect_and_subscribe(conn):
  conn.connect(username=__user, passcode=__password, wait=True)
  conn.subscribe(destination=__topic_name, ack='auto')


def connect_listen(host, port):
  connect = stomp.Connection10([(host, port)], reconnect_attempts_max=5)
  connect.set_listener("SampleListener", Queue_Listener(connect))
  connect.connect(username=__user, passcode=__password, wait=True)
  connect.subscribe(__topic_name, ack='auto', id="1")
  return connect


def get_host_ip():
  """
  查询本机ip地址
  :return: ip
  """
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  try:
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    print(f"获取到的IP是:{ip}")
  finally:
    s.close()
  return ip


def start_ping():
  host = get_host_ip()
  port = 8083
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind((host, port))
  server.listen(5)  # 接收的连接数
  logger.debug(f"心跳服务已启动......{host}:{port}")
  while True:  # 循环收发数据包，长连接
    print(f"正在等待新的连接......")
    client, address = server.accept()  # 因为设置了接收连接数为1，所以不需要放在循环中接收
    print(f"收到的客户端地址是:{address}")
    while True:
      try:
        data = client.recv(1024)  # 接收1024个字节
        if not data: break  # 适用于linux操作系统,防止客户端断开连接后死循环
        print('客户端的数据:', data.decode())
        # 读取日志文件最后10行并返回
        with open(log_path, "r") as f:
          res_log = f.readlines()[-10:]
          res_data = "".join(res_log).encode("utf-8")
          client.sendall(res_data)  # 把收到的数据再全部返回给客户端
      except ConnectionResetError:  # 适用于windows操作系统,防止客户端断开连接后死循环
        print(f"客户端断开连接......")
      break
    client.close()


def listen_active(conn):
  while True:
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f"开始进入检测链接是否正常：{conn.is_connected()}")
    logger.debug(f"开始进入检测链接是否正常：{conn.is_connected()}, 检测时间:{time_str}")
    time.sleep(30)


def start():
  # t = threading.Thread(target=start_ping)
  # t.start()
  print("receive topic server start.....")
  logger.debug("receive topic server start.....")
  conn = connect_listen(__host, __port)
  while True:
    conn = connect_listen(__host, __port)
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f"开始进入检测链接是否正常：{conn.is_connected()}")
    logger.debug(f"开始进入检测链接是否正常：{conn.is_connected()}, 检测时间:{time_str}")
    time.sleep(30)


if __name__ == '__main__':
  # 存储log日志的位置
  log_path = "Log/receive_mq.txt"
  logger = LogObj(log_path).get_logger()
  start()
