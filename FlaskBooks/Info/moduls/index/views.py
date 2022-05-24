from . import index_blu
from ... import redis_store


@index_blu.route("/")
def index():
    # 使用session存储session
    redis_store.set("age", "1000")
    return "首页内容"