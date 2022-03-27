import inspect
import pkgutil
import sys

import Refect2.apps as apps
from Refect2.apps.app import Person


def load_modul(name):
    init_params = None
    app_dict = {}
    __import__(name)
    module = sys.modules[name]
    module_attrs = dir(module)
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
    print(app_dict)


print(apps.__path__, apps.__name__ + ".")
pkg_list = pkgutil.walk_packages(apps.__path__, apps.__name__ + ".")
for _, name, ispkg in pkg_list:
    # name: 模块名字， ispkg:是不是包
    print(name, ispkg)
    if not ispkg:
        load_modul(name)
