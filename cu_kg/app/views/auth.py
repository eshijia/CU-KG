# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

auth = Blueprint('auth', __name__,
                 template_folder='../templates',
                 static_folder='../static')


@auth.route('/login')
def login():
    return render_template('auth/login.html')