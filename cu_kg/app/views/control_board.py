# -*- coding:utf-8 -*-

from flask import Blueprint, render_template

control_board = Blueprint('control_board', __name__,
                          template_folder='../templates',
                          static_folder='../static')


@control_board.route('/')
def cb_base():
    print '123'
    return render_template('control_board/cb_base.html')

