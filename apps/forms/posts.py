"""
@desc:
@author:
@contact:
@file:posts.py
@time:2020/8/26 14:33;
"""
from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField
from wtforms.validators import DataRequired,Length






class PostsFrom(FlaskForm):
    content = TextAreaField('',render_kw={"placeholder":"这一刻不想说点什么"}, validators=[DataRequired(), Length(10, 140, message='太多啦！')])
    submit = SubmitField('即刻发表',render_kw={"class":"btn btn-primary"})
