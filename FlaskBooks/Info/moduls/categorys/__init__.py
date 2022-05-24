from flask import Blueprint

# 创建蓝图，并设置蓝图前缀
categorys_blu = Blueprint("categorys", __name__, url_prefix='/categorys')

from . import categorys