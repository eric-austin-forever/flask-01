"""
@desc:
@author:
@contact:
@file:posts.py
@time:2020/8/24 16:24;
"""
from flask import Blueprint,render_template
from flask_login import login_user,logout_user,login_required


posts = Blueprint('posts',__name__)

@posts.route('/posts/')
@login_required
def index():
    return 'hello world'