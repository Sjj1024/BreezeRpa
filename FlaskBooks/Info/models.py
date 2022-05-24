import datetime

from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from . import db


class BaseModel(object):
    __tablename__ = "users"

    def __repr__(self):
        """
        格式化输出
        """
        return f"{self.__tablename__}: {self.to_json()}"

    def to_json(self):
        """
        为了转json提供的方法
        """
        _dict = self.__dict__
        if "_sa_instance_state" in _dict:
            del _dict["_sa_instance_state"]
        return _dict


class User(db.Model, BaseModel):
    """用户"""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)  # 用户编号
    user_name = db.Column(db.String(255), unique=True, nullable=False)  # 用户名
    password_hash = db.Column(db.String(255), unique=False, nullable=True, name="password")  # 用户密码
    nick_name = db.Column(db.String(255), unique=False, nullable=True)  # 用户昵称
    email = db.Column(db.String(255), unique=False, nullable=True)  # 用户邮箱
    phone = db.Column(db.String(255), unique=False, nullable=True)  # 用户手机号
    gender = db.Column(db.String(255), unique=False, nullable=True)  # 用户性别
    signature = db.Column(db.String(255), unique=False, nullable=True)  # 用户签名
    head_img = db.Column(db.String(255), unique=False, nullable=True)  # 用户头像链接
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 用户创建时间
    role_id = db.Column(db.Integer, unique=True, nullable=False)  # 角色id

    @property
    def password(self):
        # 一定要有这个属性，即便这个属性不允许访问
        raise Exception("密码不能被访问")

    # 赋值password，则自动加密存储。
    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    # 使用check_password,进行密码校验，返回True False。
    def check_password(self, pasword):
        return check_password_hash(self.password_hash, pasword)


class Categorys(db.Model, BaseModel):
    """文章分类"""
    __tablename__ = "categorys"
    id = db.Column(db.Integer, primary_key=True)  # 分类编号
    category = db.Column(db.String(255), unique=True, nullable=False)  # 分类名称
    parent_id = db.Column(db.Integer, nullable=True)  # 父分类id
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间


class Roles(db.Model, BaseModel):
    """角色权限管理"""
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)  # 角色编号
    role = db.Column(db.String(255), unique=True, nullable=False)  # 角色名称
    authority = db.Column(db.ARRAY(db.String(255)), nullable=True)  # 角色权限


class Books(db.Model, BaseModel):
    """图书管理系统"""
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)  # 图书ID
    book_name = db.Column(db.String(255), unique=True, nullable=False)  # 图书名字
    author = db.Column(db.String(255), nullable=True)  # 作者
    publisher = db.Column(db.String(255), nullable=True)  # 出版社
