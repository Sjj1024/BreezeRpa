class Query(object):
    def __init__(self):
        self.name = "查询对象"
        self.query_res = {}

    def filter(self, **kwargs):
        # 将参数缓存起来
        self.query_res.update(kwargs)
        # 返回自己本身
        return self


q = Query()
res = (q.
       filter(name="song", age=19)
       .filter(home="luoyang")
       .query_res
       )

print(res)
