"""
@desc:
@author:
@contact:
@file:users.py
@time:2020/8/24 16:24;
"""
from flask import Blueprint,render_template


users = Blueprint('users',__name__)


@users.route('/login/')
def login():
    return render_template('users/login.html')

@users.route('/register/')
def register():
    return render_template('users/register.html')