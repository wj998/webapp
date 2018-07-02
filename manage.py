from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config(object):
    '''工程配置信息'''
    DEBUG = True
    #数据库配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:wangjian@127.0.01:3306/info5"
    SQLAICHEMY_TRACK_MODIFICATIONS = False


app.config.from_object(Config)
db = SQLAlchemy(app)


@app.route('/index')
def index():
    return 'index'

if __name__ == '__main__':
    app.run()
