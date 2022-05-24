import logging

from flask import jsonify, render_template, redirect, current_app

from . import index_blu
from ... import redis_store, db
from ...models import User


@index_blu.route("/")
def index():
    return render_template("index.html")


@index_blu.route("/favicon.ico")
def favicon():
    # return redirect("static/news/favicon.ico", code=302)
    return current_app.send_static_file("news/favicon.ico")


@index_blu.route("/user_sql")
def query_sql():
    logging.info("访问首页")
    # 使用session存储session
    redis_store.set("name", "song")
    res = db.session.execute("select nick_name from users").fetchall()
    emp_json_list = [dict(zip(item.keys(), item)) for item in res]
    print(emp_json_list)
    return "首页内容"


@index_blu.route("/user")
def query_user():
    # 返回所有用户保存到list中
    user_list = User.query.all()
    print(user_list)
    result = [u.to_json() for u in user_list]
    return jsonify(result), 200


@index_blu.route("/adduser")
def add_user():
    # 测试数据库
    u = User()
    u.nick_name = "wang"
    # 将用户添加到数据库会话中
    db.session.add(u)
    # 将数据库会话中的变动提交到数据库中,如果不Commit,数据库中是没有改动的
    db.session.commit()
    return "添加成功"
