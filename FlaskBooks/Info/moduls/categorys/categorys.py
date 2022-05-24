import logging

from flask import request
from flask import jsonify

from Info import db
from Info.models import Categorys
from Info.moduls.categorys import categorys_blu


@categorys_blu.route("/", methods=["GET", "POST"])
def regist():
    logging.info("添加分类")
    # 1. 获取参数
    # param_dict = request.json
    # mobile = param_dict.get("category")
    # smscode = param_dict.get("parent_id")
    category = Categorys()
    category.category = "后端编程"
    category.parent_id = 0
    db.session.add(category)
    db.session.commit()
    return "success"

@categorys_blu.route("/query", methods=["GET", "POST"])
def query():
    logging.info("查找文章分类")
    user_list = Categorys.query.all()
    print(user_list)
    result = [u.to_json() for u in user_list]
    return jsonify(result), 200

@categorys_blu.route("/query_sql", methods=["GET", "POST"])
def query_sql():
    logging.info("查找文章分类")
    res = db.session.execute("select * from categorys").fetchall()
    emp_json_list = [dict(zip(item.keys(), item)) for item in res]
    print(emp_json_list)
    return jsonify(emp_json_list), 200