from flask import Blueprint

# 生成蓝图
index_blu = Blueprint("index", __name__)

# 让视图起作用，就得导入进去
from . import views