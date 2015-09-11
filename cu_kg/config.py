# -*- coding:utf-8 -*-

import os


class AppConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'jiu bu gao su ni'


class CayleyConfig(object):
    CAYLEY_HOST = os.environ.get('CAYLEY_HOST') or 'localhost'
    CAYLEY_PORT = 64210


class MongoDBConfig(object):
    MONGODB_HOST = os.environ.get('MONGODB_HOST') or 'localhost'
    MONGODB_PORT = 27017

    DATABASE_NAME = 'cayley'
    COLLECTION_QUADS = 'quads'
    COLLECTION_NODES = 'nodes'


class SQLAlchemyConfig(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3306/cukg'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


class DevelopmentConfig(object):
    DEBUG = True


class TestingConfig(object):
    TESTING = True


def init_app_config(app):
    app.config['SECRET_KEY'] = AppConfig.SECRET_KEY
    app.config['DEBUG'] = DevelopmentConfig.DEBUG

    app.config['SQLALCHEMY_DATABASE_URI'] = \
        SQLAlchemyConfig.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = \
        SQLAlchemyConfig.SQLALCHEMY_COMMIT_ON_TEARDOWN