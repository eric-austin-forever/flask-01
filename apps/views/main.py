"""
@desc:主页
@author:
@contact:
@file:main.py
@time:2020/8/24 16:23;
"""
from flask import Blueprint,render_template


mains = Blueprint('main',__name__)


@mains.route('/')
def index():
    return render_template('main/index.html')
