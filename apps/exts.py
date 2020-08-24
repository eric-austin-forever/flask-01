"""
@desc:
@author:
@contact:
@file:exts.py
@time:2020/8/24 16:11;
"""
from flask_bootstrap import Bootstrap


# 实例化对象
bootstrap = Bootstrap()


# 封装函数 完成初始化

def config_extensions(app):
    bootstrap = Bootstrap(app)


