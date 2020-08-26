"""
@desc:
@author:
@contact:
@file:users.py
@time:2020/8/25 11:19;
"""
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,PasswordField,BooleanField,FileField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from apps.models import User
from flask_wtf.file import FileField,FileRequired,FileAllowed
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from apps.exts import photos


# 用户注册表单
class RegisterFrom(FlaskForm):
    username = StringField('用户名',validators=[DataRequired(),Length(6,20,message='用户名必须6-20位')],render_kw={"placeholder":"请输入用户名!"})
    password = PasswordField('密码',validators=[DataRequired(),Length(6,30,message='密码必须6-30位')],render_kw={"placeholder":"请输入密码!"})
    confirm = PasswordField('确认密码',validators=[EqualTo('password',message='两次密码必须一致')],render_kw={"placeholder":"请确认密码!"})
    email = StringField('邮箱',validators=[Email(message='邮箱格式错误')],render_kw={"placeholder":"请输入邮箱!"})

    submit = SubmitField('立即注册',render_kw={"class":"btn btn-primary input-group-btn"})

    # 用户名 邮箱 必须是数据库里没有的，否则返回用户名/邮箱已存在
    def validate_username(self,field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('该用户名已存在，请重新输入！')

    def validate_email(self,field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('该邮箱已存在，请重新输入！')


class LoginFrom(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(6, 20, message='用户名必须6-20位')],render_kw={"placeholder":"请输入用户名!"})
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 30, message='密码必须6-30位')],render_kw={"placeholder":"请输入密码!"})
    remember = BooleanField('记住我')
    submit = SubmitField('立即登录',render_kw={"class":"btn btn-primary"})


class UploadsForm(FlaskForm):
    icon = FileField('头像', validators=[FileRequired('请选择图片'),FileAllowed(photos,message='只能上传图片')], render_kw={"class": " btn btn-primary"})
    submit = SubmitField('立即提交')