"""
@desc:
@author:
@contact:
@file:config.py
@time:2020/8/24 16:11;
"""
import os


base_dir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ADADSF1212'
    # bootstrap使用本地的静态文件
    BOOTSTRAP_SERVE_LOCAL = True

    PAGE_COUNT = 10

    # 邮箱服务器
    MAIL_SERVER = 'smtp.qq.com'

    # 用户名
    MAIL_USERNAME = '1519398277@qq.com'

    # 授权码
    MAIL_PASSWORD = 'vdjlwbmynkrggigb'

    # 上传文件设置
    MAX_CONTENT_LENGTH = 1024*1024*8

    # 位置
    UPLOADED_PHOTOS_DEST = os.path.join(base_dir,'static/uploads')




# 开发环境
class DevelopmentConfig(Config):
    # 数据库
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'blog'
    USERNAME = 'root'
    PASSWORD = '123456'
    # 用户名:密码@数据库地址:端口号/数据库名字
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 测试环境
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(base_dir,'testing_sqlite')


# 生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'production_sqlite')


config = {
    'default': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

