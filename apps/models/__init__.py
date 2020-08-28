"""
@desc:
@author:
@contact:
@file:__init__.py.py
@time:2020/8/24 16:13;
"""
from .users import User
from .posts import Posts

from apps.exts import db

collections = db.Table('collections',
                       db.Column('user_id',db.Integer,db.ForeignKey('users.id')),
                       db.Column('posts_id',db.Integer,db.ForeignKey('posts.id'))
                       )


