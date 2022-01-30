import abc
import inspect
import sys


class Plugin(object):

  @abc.abstractmethod
  def run(self, data):
    print("父插件的方法")
    return data


def load_plugin():
  module_name = "plugin"
  __import__(module_name)
  module = sys.modules[module_name]
  module_attrs = dir(module)
  for name in module_attrs:
    var_obj = getattr(module, name)
    if inspect.isclass(var_obj) and var_obj.__name__ != Plugin.__name__:
      return var_obj()
  return None


def init(data):
  print(f"一、方法得到的值:{data}")
  run(data)


def run(data):
  print(f"二、方法得到的初值:{data}")
  plugin = load_plugin()
  if plugin:
    data = plugin.run(data)
    print(f"二、方法插件的结果值:{data}")
  died(data)


def died(data):
  print(f"三、方法得到的值:{data}")
  print("流程结束")


def flow():
  init(100)


if __name__ == '__main__':
  print("执行流程")
  flow()
