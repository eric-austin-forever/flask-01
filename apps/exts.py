"""
@desc:
@author:
@contact:
@file:exts.py
@time:2020/8/24 16:11;
"""
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_uploads import UploadSet,IMAGES,configure_uploads,patch_request_class
from flask_moment import Moment


# 实例化对象
bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
migrate = Migrate(db=db)
login_manager = LoginManager()
photos = UploadSet('photos',IMAGES,)
moment = Moment()




# 封装函数 完成初始化

def config_extensions(app):
    bootstrap.init_app(app)
    # 跟实例完成绑定
    mail.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    # 当我们发表博客，发现没有登录，跳转到登录界面
    login_manager.login_view = 'users.login'
    # 给没有登陆的用户发送提示信息
    login_manager.login_message = '请先登录'
    # session保护级别
    login_manager.session_protection = 'basic'

    # 完成上传文件的初始化
    configure_uploads(app,photos)
    patch_request_class(app,size=None)



