# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

from app.views.control_board import control_board
from app.views.entity_base import entity_base
from app.views.about import about

app = Flask(__name__)

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

app.register_blueprint()
app.register_blueprint(control_board, url_prefix='/cukg/control_board')
app.register_blueprint(about, url_prefix='/cukg/about')


if __name__ == '__main__':
    app.run(debug=True)
