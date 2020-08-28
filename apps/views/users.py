"""
@desc:
@author:
@contact:
@file:users.py
@time:2020/8/24 16:24;
"""
import os

from flask import Blueprint, render_template, redirect, url_for,flash,request,current_app
from apps.models import User
from apps.forms import RegisterFrom,LoginFrom,UploadsForm
from apps.exts import db,photos
from apps.email import send_mail
from flask_login import login_user,logout_user,login_required,current_user
from PIL import Image




users = Blueprint('users',__name__)


@users.route('/login/',methods=['GET','POST'])
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        u = User.query.filter_by(username = form.username.data).first()
        if not u:
            flash('用户名不存在')

        elif not u.confirmed:
            flash('该用户还没激活')

        elif u.verify_password(form.password.data):
            login_user(u,remember=form.remember.data)
            flash('登录成功')
            # 如果链接中有next参数，就跳到这个地址，没有就跳到首页

            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            flash('无效密码')

    return render_template('users/login.html',form=form)

@users.route('/logout/')
def logout_demo():
    logout_user()
    flash('退出登录成功')
    return redirect(url_for('main.index'))




@users.route('/profile/',methods=['GET','POST'])
@login_required     # 装饰器必须写在路由的下面
def profile():
    # form = RegisterFrom
    # form = ChangeNameForm()
    img_url = photos.url(current_user.icon)

    if request.method == 'POST':
        change_username(request.form['new_name'])
    return render_template('users/profile.html',img_url=img_url)






@users.route('/register/',methods=['GET','POST'])
def register():
    form = RegisterFrom()
    if form.validate_on_submit():
        u = User(
            username=form.username.data,
            password=form.password.data,
            email=form.email.data,

        )
        db.session.add(u)
        db.session.commit()

        # 生产一个加密字符串，保存该用户注册成功后的信息
        token = u.generate_token()
        # 发送一封邮箱
        send_mail(u.email,subject='账户激活',template='email/activate',username=u.username,token=token)
        # print(u.email)
        return redirect(url_for('users.login'))
    return render_template('users/register.html',form=form)


@users.route('/activate/<token>/')
def activate_user(token):
    if User.check_activate_token(token):
        flash('账号已激活')
        return redirect(url_for('users.login'))
    else:
        flash('激活失败')
        return redirect(url_for('main.index'))


@users.route('/change_icon/', methods=['GET', 'POST'])
@login_required
def change_icon():
    form = UploadsForm()
    img_url = 'http://127.0.0.1:5056/_uploads/photos/default.jpg'
    if form.validate_on_submit():
        # 随机文件名
        suffix = os.path.splitext(form.icon.data.filename)[1]
        filename = random_string()+suffix
        photos.save(form.icon.data,name=filename)
        # 文件缩略图
        path_name = os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'],filename)
        img = Image.open(path_name)
        img.thumbnail((128,128))
        img.save(path_name)

        # 文件上传后文件地址，返回到页面上

        if current_user.icon != 'default.jpg':
            os.remove(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'],current_user.icon))
        current_user.icon = filename
        db.session.commit()
        flash('头像上传完毕')
        return redirect(url_for('users.change_icon'))
        # 新地址保存到数据库中
    img_url = photos.url(current_user.icon)
    return render_template('users/change_icon.html',form=form,img_url=img_url)


def random_string(length=20):
    import random
    base_dir = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    return ''.join(random.choice(base_dir) for i in range(length))



@users.route('/myblog/')
def my_blog():
    return '我的博客'



def change_username(new_name):

    user = User.query.get(current_user.id)
    user.username = new_name

    db.session.commit()

    return render_template('users/profile.html')


