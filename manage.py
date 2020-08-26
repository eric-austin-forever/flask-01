"""
@desc:
@author:
@contact:
@file:manage.py
@time:2020/8/24 16:08;
"""
from flask_script import Manager
from apps import create_app
from flask_migrate import MigrateCommand
from apps.models import Posts
from apps.models import User
from apps.exts import db
import time


app = create_app('default')
manager = Manager(app)
manager.add_command('db',MigrateCommand)


@manager.command
def create_test_post():
    # 内容 作者
    for x in range(1,200):
        content = '内容：%s' % x
        author = User.query.first()
        post = Posts(content=content,author=author)
        time.sleep(0.2)
        db.session.add(post)
        db.session.commit()



if __name__ == '__main__':
    manager.run()

