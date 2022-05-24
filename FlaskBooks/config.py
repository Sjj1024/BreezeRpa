import logging

from redis import StrictRedis


class Config(object):
    """
    项目配置
    """

    DEBUG = True
    LOG_LEVEL = logging.DEBUG
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost:3306/infomation"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # session博阿村配置
    SESSION_TYPE = "redis"
    # 指定session保存的位置
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_KEY_PREFIX = "Session"
    SESSION_USE_SIGNER = True
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 86400 * 2
    SECRET_KEY = "rIucD1qEuL3/iLaV5+6MbMjzHjlhvJBwgvtZi/A2tCmVoLmGTLCQYQ=="


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
