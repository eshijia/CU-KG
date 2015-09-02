# -*- coding:utf-8 -*-

from flask import Flask
from app.views.control_board import control_board
from app.views.about import about

app = Flask(__name__)
app.register_blueprint(control_board)
app.register_blueprint(about)


if __name__ == '__main__':
    app.run()
