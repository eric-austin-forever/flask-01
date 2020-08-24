"""
@desc:
@author:
@contact:
@file:config.py
@time:2020/8/24 16:11;
"""


class Config:
    # bootstrap使用本地的静态文件
    BOOTSTRAP_SERVE_LOCAL = True


# 开发环境
class DevelopmentConfig(Config):
    pass


# 测试环境
class TestingConfig(Config):
    pass


# 生产环境
class ProductionConfig(Config):
    pass


config = {
    'default': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
