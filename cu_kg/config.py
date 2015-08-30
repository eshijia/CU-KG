
import os


class AppConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'jiu bu gao su ni'

    @staticmethod
    def init_app(app):
        pass


class CayleyConfig(AppConfig):
    pass


class MongoDBConfig(AppConfig):
    pass


class TestingConfig(AppConfig):
    pass
