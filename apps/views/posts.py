"""
@desc:
@author:
@contact:
@file:posts.py
@time:2020/8/24 16:24;
"""
from flask import Blueprint,render_template,jsonify
from flask_login import login_user,logout_user,login_required,current_user
from .decorators import login_requireds


posts = Blueprint('posts',__name__)

@posts.route('/posts/<pid>/')
@login_required
def collect(pid):
    # 原来收藏，点击变成取消收藏
    if current_user.is_favorite(pid):
        current_user.del_favorite(pid)
    else:
        current_user.add_favorite(pid)
    return jsonify({'result':'ok'})


