from flask import Blueprint

# 创建蓝图，并设置蓝图前缀
books_blu = Blueprint("books", __name__, url_prefix='/books')

from . import books