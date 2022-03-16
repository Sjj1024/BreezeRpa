import pkgutil
import apps

pkg_list = pkgutil.walk_packages(apps.__path__, apps.__name__ + ".")
for _, name, ispkg in pkg_list:
  # name: 模块名字， ispkg:是不是包
  print(name, ispkg)

print("------------------------------------")
file_list = pkgutil.get_data('apps', 'app.py')
print(file_list)

print("------------------------------------")
file_list = pkgutil.get_data('apps', 'app.py')
print(file_list)