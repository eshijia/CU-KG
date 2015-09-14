# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

from cu_kg.config import init_app_config

bootstrap = Bootstrap()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__)
    init_app_config(app)

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from views.home import home
    app.register_blueprint(home, url_prefix='/cukg')

    from views.auth import auth, load_user
    login_manager.user_loader(load_user)
    app.register_blueprint(auth, url_prefix='/cukg/auth')

    from views.entity_base import entity_base
    app.register_blueprint(entity_base, url_prefix='/cukg/entity_base')

    from views.control_board import control_board
    app.register_blueprint(control_board, url_prefix='/cukg/control_board')

    from views.relation_search import relation_search
    app.register_blueprint(relation_search, url_predix='/cukg/relation_search')

    from views.about import about
    app.register_blueprint(about, url_prefix='/cukg/about')

    return app
