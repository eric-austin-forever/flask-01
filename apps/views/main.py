"""
@desc:主页
@author:
@contact:
@file:main.py
@time:2020/8/24 16:23;
"""
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app,abort
from apps.models import Posts
from apps.forms import PostsFrom
from flask_login import current_user, login_required
from apps.exts import db

mains = Blueprint('main', __name__)


@mains.route('/', methods=['GET', 'POST'])
def index():
    form = PostsFrom()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            # 获取当前登录用户
            u = current_user._get_current_object()
            p = Posts(content=form.content.data, author=u)
            db.session.add(p)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('登录之后才能发表')
            return redirect(url_for('users.login'))

        # 读取所有的博客
    # posts = Posts.query.filter_by(rid = 0).all()
    # return render_template('main/index.html',form=form,posts=posts)
    # 接收用户查看第几页
    # http://www.baidu.com/?p=1
    page = request.args.get('p', 1, type=int)

    # 拿到分页对象
    pagination = Posts.query.filter_by(rid=0).order_by(Posts.pub_time.desc()).paginate(page=page,per_page=current_app.config['PAGE_COUNT'],error_out=False)
    posts = pagination.items
    return render_template('main/index.html', form=form, posts=posts, pagination=pagination)


@mains.route('/details/<postid>/', methods=['GET', 'POST'])
@login_required
def details(postid):
    post = Posts.query.get(postid)
    # 如果没有帖子详情，那么就抛出404错误
    if not post:
        abort(404)
    comments = Posts.query.filter_by(rid=postid).order_by(Posts.pub_time.desc()).all()
    return render_template('main/details.html',post=post,comments=comments)