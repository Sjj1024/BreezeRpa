# 定义装饰器

def outer(fun):
  print("开始执行装饰器")

  def inner():
    print("开始执行inner里面内容g")
    return 2
    # res = fun()
    # print("开始执行inner里面执行结束")
    # return res
  print("装饰器执行结束")
  return inner


@outer
def test() -> list:
  print("test")
  return '1'


if __name__ == '__main__':
  res = test()
  print(res)
