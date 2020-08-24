"""
@desc:
@author:
@contact:
@file:__init__.py.py
@time:2020/8/24 16:13;
"""
from .main import mains
from .users import users
from .posts import posts

DEFAUL_BLUEPRINT = (
    (mains, ''),
    (users, '/users'),
    (posts, '/posts')

)


# app.register_blueprint(main,url_profix='')

# 封装函数 完成蓝本的注册
def config_blueprint(app):
    for blueprint, url_prefix in DEFAUL_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=url_prefix)
