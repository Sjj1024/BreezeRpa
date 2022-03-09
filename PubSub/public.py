import json
import redis

# 以下代码是向redis 发命令
QUEUE = "code"  # 队列名称key

# redisPool = redis.ConnectionPool(host=config.get_redis_host(), port=6379, db=config.get_redis_db())
redisPool = redis.ConnectionPool(host='localhost', port=6379, db=8)
client = redis.Redis(connection_pool=redisPool)


def send_cmd(seaweed):
    json_cmd = json.dumps(seaweed, ensure_ascii=False)
    client.rpush(QUEUE, json_cmd)


ll = list(range(3))
# get_weekend('20180325')})
if __name__ == "__main__":
    for k in ll:
        send_cmd({"label": k, 'timd': 20160503, 'timm': 20170430})