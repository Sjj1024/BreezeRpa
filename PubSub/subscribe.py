import chardet
import json
import multiprocessing
import redis

# 以下代码是向redis 发命令
QUEUE = "code"
# redisPool = redis.ConnectionPool(host=config.get_redis_host(), port=6379, db=config.get_redis_db())
redisPool = redis.ConnectionPool(host='localhost', port=6379, db=8)
client = redis.Redis(connection_pool=redisPool)


# 以下代码是向redis 取命令，并且采用多进程来实现计算
def func(a, b, c):
  print(a, b)


def worker(pname):
  client = redis.Redis(connection_pool=redisPool)
  # client_ = redis.ConnectionPool(host='localhost', port=6379, db=8)
  while True:
    cmd = client.lpop(QUEUE)
    if cmd is None:
      return
    encode1 = chardet.detect(cmd)["encoding"]
    cmd = cmd.decode(encode1)
    cmd = format_cmd(cmd)
    try:
      func(cmd["label"], cmd['timd'], cmd['timm'])
      # price_fix.update(cmd["city"], cmd["region"], cmd["name"])
      # print(pname + ":", cmd, "计算成功")
    except Exception as ex:
      print(ex)
      print(pname + ":", cmd, "计算失败")


def format_cmd(cmd):
  return json.loads(cmd)


if __name__ == "__main__":
  # 多进程消费
  pro_num = 5
  pool = multiprocessing.Pool(processes=pro_num)
  for pid in range(1, pro_num):
    pid = "PROC" + str(pid).zfill(3)
    pool.apply_async(worker, (pid,))
  pool.close()
  pool.join()
