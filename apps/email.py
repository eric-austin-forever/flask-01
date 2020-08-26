"""
@desc:
@author:
@contact:
@file:email.py
@time:2020/8/24 16:11;
"""
from apps.exts import mail
from flask_mail import Message
from flask import current_app,render_template
from threading import Thread

# 异步发送文件
def async_send__mail(app,msg):
    with app.app_context():
        mail.send(message=msg)


# 封装邮件发送函数
def send_mail(to,subject,template,**kwargs):
    # 获取当前实例
    app = current_app._get_current_object()
    # message对象
    msg = Message(subject=subject,recipients=[to],sender=app.config['MAIL_USERNAME'])

    # 浏览器打开显示内容
    msg.html = render_template(template+'.html',**kwargs)

    # 客户端打开
    msg.body = render_template(template+'.txt',**kwargs)

    # 创建线程
    th = Thread(target=async_send__mail,args=[app,msg])

    # 启动线程
    th.start()

    return th

