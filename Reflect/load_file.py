import os
import sys
import inspect
from apps.app import Person


def load_model(file, init_params=None):
  module_name = ''
  if len(file) > 3 and (file[-3:] == '.py' or file[-4:] == '.pyc'):
    if file[-3:] == '.py':
      module_name = file[:-3]
    if file[-4:] == '.pyc':
      module_name = file[:-4]
  __import__(module_name)
  module = sys.modules[module_name]
  module_attrs = dir(module)
  app_dict = {}
  for name in module_attrs:
    var_obj = getattr(module, name)
    if inspect.isclass(var_obj):
      if issubclass(var_obj, Person) and var_obj.__name__ != Person.__name__:
        if app_dict.get(name) is None:
          if init_params is None:
            app_dict[name] = var_obj()
          else:
            app_dict[name] = var_obj()
          print("注入 %s 模块 %s 成功" % (Person.__name__, var_obj.__name__))
  return app_dict


def recursive_dir(path, f, file_list):
  """
  递归获取文件夹中所有的文件
  :param path:根目录
  :param f:子目录
  :param file_list:文件列表
  :return:
  """
  print(f"{path}:{f}")
  file_names = os.listdir(os.path.join(path, f))
  for file in file_names:
    newDir = path + '/' + f.split(".")[-1] + '/' + file
    if os.path.isfile(newDir):
      if "pycache" not in f and "pycache" not in file:
        py_file = "apps" + newDir.split("apps")[1].replace("/", ".")
        file_list.append(py_file)
    else:
      if "__pycache__" not in file:
        fi = "/".join(newDir.split("/")[0:-1])
        fl = newDir.split("/")[-1]
        if "." in fl:
          print(fl)
        recursive_dir(fi, fl, file_list)


def search_file():
  app_dicts = {}
  app_files = []
  recursive_dir(os.getcwd(), "apps", app_files)
  print(app_files)
  for app in app_files:
    if app.endswith(".py") or app.endswith(".pyc"):
      app_dicts.update(load_model(app))
  print(f"所有模块已加载完成: {app_dicts}")
  params = {"a": "1", "b": "2"}
  for key in app_dicts.keys():
    obj = app_dicts.get(key)
    if isinstance(obj, Person):
      print(f"开始调用{key}对象的run方法:")
      obj.run(params)


if __name__ == '__main__':
  search_file()
