"""
@desc:
@author:
@contact:
@file:posts.py
@time:2020/8/26 14:22;
"""
from apps.exts import db
from datetime import datetime



class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    rid = db.Column(db.Integer,index=True,default=0)
    content = db.Column(db.Text)
    pub_time = db.Column(db.DateTime,default=datetime.utcnow)
    uid = db.Column(db.Integer,db.ForeignKey('users.id'))
    author = db.relationship('User',backref="postes")











