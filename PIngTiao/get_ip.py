import socket
import time


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


if __name__ == '__main__':
  get_host_ip()
  time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
  print(time_str)


