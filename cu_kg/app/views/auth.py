# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, redirect, request, url_for
from flask.ext.login import login_user, logout_user, login_required

from cu_kg.app.forms.auth import LoginForm
from cu_kg.app.models.user import User
from cu_kg.app import login_manager

auth = Blueprint('auth', __name__,
                 template_folder='../templates',
                 static_folder='../static')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    user = User.query.filter_by(username=login_form.username.data).first()
    if user is not None and user.verify_password(login_form.password.data):
        login_user(user, login_form.remember_me.data)
        return redirect(request.args.get('next') or url_for('home.index'))
    return render_template('auth/login.html', login_form=login_form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.index'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))