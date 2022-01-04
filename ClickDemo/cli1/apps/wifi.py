

class WifiTest(object):
  def __init__(self):
    self.name = '我是wifi'

  def say(self):
    print(f"开始打印自己的名字:{self.name}")

  def play(self):
    print(f"开始自己玩")


def get_name():
  print("我的名字是WifiTest")