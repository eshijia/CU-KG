# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, flash, redirect, request, url_for
from flask.ext.login import login_user, logout_user

from cu_kg.app import db
from cu_kg.app.forms.auth import LoginForm, RegisterForm
from cu_kg.app.models.user import User
from cu_kg.app import login_manager

auth = Blueprint('auth', __name__,
                 template_folder='../templates',
                 static_folder='../static')


# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     login_form = LoginForm()
#     user = User.query.filter_by(username=login_form.username.data).first()
#     if user is not None and user.verify_password(login_form.password.data):
#         login_user(user, login_form.remember_me.data)
#         return redirect(request.args.get('next') or url_for('home.index'))
#     return render_template('auth/login.html', login_form=login_form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if request.method == 'GET':
        return render_template('auth/login.html', login_form=login_form)
    username = login_form.username.data
    password = login_form.password.data
    registered_user = User.query.filter_by(username=username).first()
    if registered_user is None:
        flash(u'用户名无效', 'error')
        return redirect(url_for('auth.login'))
    if not registered_user.check_password(password):
        flash(u'密码不正确', 'error')
        return redirect(url_for('auth.login'))
    login_user(registered_user, remember=login_form.remember_me.data)
    flash(u'登录成功')
    return redirect(request.args.get('next') or url_for('home.index'))


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.index'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if request.method == 'GET':
        return render_template('auth/register.html', register_form=register_form)
    user = User(register_form.username.data, register_form.password.data, register_form.email.data)
    db.session.add(user)
    db.session.commit()
    flash('用户注册成功')
    return redirect(url_for('auth.login'))
