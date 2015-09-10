# -*- coding:utf-8 -*-

import os


class AppConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'jiu bu gao su ni'

    @staticmethod
    def init_app(app):
        pass


class CayleyConfig(AppConfig):
    CAYLEY_HOST = os.environ.get('CAYLEY_HOST') or 'localhost'
    CAYLEY_PORT = 64210


class MongoDBConfig(AppConfig):
    MONGODB_HOST = os.environ.get('MONGODB_HOST') or 'localhost'
    MONGODB_PORT = 27017

    DATABASE_NAME = 'cayley'
    COLLECTION_QUADS = 'quads'
    COLLECTION_NODES = 'nodes'


class SQLAlchemyConfig(AppConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3306/cukg'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


class DevelopmentConfig(AppConfig):
    DEBUG = True


class TestingConfig(AppConfig):
    TESTING = True
