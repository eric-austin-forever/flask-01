# flask-01
flask项目



## 目录结构

```
python
-apps #python包
--  __init__.py     #项目实例文件
--  exts.py         #存放所有的扩展  
--     config.py    #存放项目的配置 配置数据库 配置上传文件 
--     email.py     #多个地方可能都用到邮件单独拿出来写 
--     models       #python包 存放模型
--     forms        #python包 存放表单  
--     views        #python包 存放蓝本文件的目录
--    templates     #存放页面的  
--     static       #存放静态文件 
---     css         # 存放css文件
---     js          # 存放js文件
---     images      # 存放图片
---     favicon.ico # 存放图标
-- manage.py        #项目的入口文件  

```