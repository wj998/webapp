import redis


class Config(object):
    '''工程配置信息'''
    DEBUG = True
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    #数据库配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:wangjian@127.0.01:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask_session的配置信息
    SESSION_TYPE = "redis"
    SESSION_USE_SIGHER = True
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 86400

    # 定义配置字典
    config = {
        "developement": DevelopementConfig,
        "prodution": ProdutionConfig

    }


class DevelopementConfig(Config):
    '''开发模式显得配置'''
    DEBUG = True



class ProdutionConfig(Config):
    '''生产模式下的配置'''
    pass
