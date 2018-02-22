import os

class Config(object):
    SECRET_KEY = os.environ.get('APP_SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass
