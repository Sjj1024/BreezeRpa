'''
server端
长连接，短连接，心跳
'''
import socket

BUF_SIZE = 1024
host = 'localhost'
port = 8083

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)  # 接收的连接数

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
      client.sendall("success".encode())  # 把收到的数据再全部返回给客户端
      break
    except ConnectionResetError:  # 适用于windows操作系统,防止客户端断开连接后死循环
      print(f"客户端断开连接......")
      break
  client.close()
