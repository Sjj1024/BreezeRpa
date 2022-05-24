from flask import Blueprint

# 创建蓝图，并设置蓝图前缀
roles_blu = Blueprint("roles", __name__, url_prefix='/roles')

from . import roles