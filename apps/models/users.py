"""
@desc:
@author:
@contact:
@file:users.py
@time:2020/8/25 10:13;
"""
from apps.exts import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from .posts import Posts



class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(32),unique=True)
    password_hash = db.Column(db.String(256))
    email = db.Column(db.String(64),unique=True)
    # 是否激活
    confirmed = db.Column(db.Boolean,default=False)
    icon = db.Column(db.String(128),default='default.jpg')

    # 添加收藏功能
    favorite = db.relationship('Posts',secondary='collections',backref=db.backref('usered',lazy='dynamic'),lazy='dynamic')

    @property   # 把方法当成属性调用
    def password(self):
        raise AttributeError('密码不可读属性')

# password  对外
# password_hash     对内，加密后
# 密码永不返回
# 密码不可读

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    # 密码校验
    # 对提交的密码加密，再与数据库中比较
    # 正确返回True，错误返回Flase
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    # 生成token的方法
    # 设置过期时间
    def generate_token(self,expires_in=3600):
        s = Serializer(current_app.config['SECRET_KEY'],expires_in=expires_in)
        return s.dumps({'id': self.id})  #

    # 校验
    @staticmethod
    def check_activate_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        u = User.query.get(data.get('id'))
        if not u:
            return False
        if not u.confirmed:
            u.confirmed = True

            db.session.commit()
        return True

    #判断是否收藏
    def is_favorite(self,pid):
        favorites = self.favorite.all()
        posts = list(filter(lambda p: p.id == pid, favorites))
        print(len(posts))
        if len(posts) > 0:
            return True
        else:
            return False


    def add_favorite(self,pid):
        p = Posts.query.get(pid)
        self.favorite.append(p)
        db.session.commit()




    def del_favorite(self,pid):
        p = Posts.query.get(pid)
        self.favorite.remove(p)
        db.session.commit()
# 登录认证的回调
# 登录成功以后存的是用的id
# 需要一个方法根据用户的id 取出用户的详细信息
@login_manager.user_loader
def load_user(uid):
    return User.query.get(uid)
