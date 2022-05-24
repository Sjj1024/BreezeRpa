import logging

from flask import request

from Info.moduls.roles import roles_blu


@roles_blu.route("/", methods=["POST"])
def regist():
    logging.info("添加角色")
    # 1. 获取参数
    param_dict = request.json
    mobile = param_dict.get("role_name")
    smscode = param_dict.get("smscode")
    password = param_dict.get("password")
    return "sss"

