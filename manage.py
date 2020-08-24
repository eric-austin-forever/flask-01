"""
@desc:
@author:
@contact:
@file:manage.py
@time:2020/8/24 16:08;
"""
from flask_script import Manager
from apps import create_app

app = create_app('default')
manager = Manager(app)

if __name__ == '__main__':
    manager.run()

