"""
@desc:
@author:
@contact:
@file:decorators.py
@time:2020/8/27 11:22;
"""
from functools import wraps
from flask_login import current_user
from flask import session,redirect,url_for


# func是个方法
def login_requireds(func):
    @wraps(func)
    def inner(*args,**kwargs):
        user = session.get('username')
        if user:
            return func(*args,**kwargs)
        else:
            return redirect(url_for('users.login'))
    return inner
