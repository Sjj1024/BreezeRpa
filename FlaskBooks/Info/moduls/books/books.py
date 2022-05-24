import logging

from flask import jsonify, request

from Info.models import Books
from Info.moduls.books import books_blu
from ... import db


@books_blu.route("/", methods=["GET"])
def regist():
    logging.info("欢迎访问图书管理系统")
    return "欢迎访问图书管理系统"


@books_blu.route("/all", methods=["GET"])
def query_books():
    user_list = Books.query.all()
    result = [u.to_json() for u in user_list]
    return jsonify(result), 200


@books_blu.route("/del", methods=["GET"])
def del_book():
    book_id = request.args['id']
    delete_num = db.session.query(Books).filter(Books.id == book_id).delete()
    db.session.commit()
    return jsonify(res_code=200, res_msg=f"删除图书{book_id}成功，删除记录{delete_num}条")


@books_blu.route("/update", methods=["POST"])
def update_book():
    # 修改记录条数
    param_dict = request.json
    id = param_dict.get("id")
    book_name = param_dict.get("book_name")
    author = param_dict.get("author")
    publisher = param_dict.get("publisher")
    res = db.session.query(Books).filter(Books.id == id).update(
        {'book_name': book_name, 'author': author, "publisher": publisher}
    )
    db.session.commit()
    return jsonify(res_code=200, res_msg=f"更新成功，更新条数{res}")


@books_blu.route("/add", methods=["POST"])
def add_book():
    logging.info("添加图书信息")
    # param_dict = request.json
    param_dict = request.form
    book_name = param_dict.get("book_name")
    author = param_dict.get("author")
    publisher = param_dict.get("publisher")
    book = Books()
    book.book_name = book_name
    book.author = author
    book.publisher = publisher
    # 将用户添加到数据库会话中
    db.session.add(book)
    # 将数据库会话中的变动提交到数据库中,如果不Commit,数据库中是没有改动的
    db.session.commit()
    return jsonify(res_code=2000, res_msg="添加成功")
