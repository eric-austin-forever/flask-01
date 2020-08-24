"""
@desc:
@author:
@contact:
@file:posts.py
@time:2020/8/24 16:24;
"""
from flask import Blueprint,render_template


posts = Blueprint('posts',__name__)

@posts.route('/posts/')
def index():
    return 'hello world'