import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config(object):
    '''工程配置信息'''
    DEBUG = True
    #数据库配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:wangjian@127.0.01:3306/information"
    SQLAICHEMY_TRACK_MODIFICATIONS = False

    # redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = redis.StrivtRedis(host=Config.REDSIS_HOST, post=Config.REDIS_PORT)


@app.route('/index')
def index():
    return 'index'

if __name__ == '__main__':
    app.run()
