import logging

from redis import StrictRedis


class Config(object):
    """
    项目配置
    """
    DEBUG = True
    LOG_LEVEL = logging.DEBUG
    # 数据库配置
    USERNAME = "postgres"
    PASSWORD = "postgres"
    DATA_IP = "localhost"
    DATA_PORT = 5432
    DATABASE_NAME = "book_info"
    # SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost:3306/infomation"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{USERNAME}:{PASSWORD}@{DATA_IP}:{DATA_PORT}/{DATABASE_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    # Session配置
    SESSION_TYPE = "redis"
    # 指定session保存的位置
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_KEY_PREFIX = "Session"
    SESSION_USE_SIGNER = True
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 86400 * 2
    SECRET_KEY = "rIucD1qEuL3/iLaV5+6MbMjzHjlhvJBwgvtZi/A2tCmVoLmGTLCQYQ=="

    # 163邮箱服务器地址
    MAIL_HOST = 'smtp.163.com'
    # 163用户名
    MAIL_USER = 'sjjhub@163.com'
    # 密码(部分邮箱为授权码)
    MAIL_PASS = '521xiaoshen'


class DevelopMentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    DEBUG = True


config = {
    "dev": DevelopMentConfig,
    "pro": ProductionConfig,
    "test": TestingConfig
}
