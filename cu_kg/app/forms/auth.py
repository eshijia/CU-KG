# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(Form):
    username = StringField(u'用户名', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField(u'密码', validators=[DataRequired()])
    remember_me = BooleanField(u'记住我')
    submit = SubmitField(u'登录')


class RegisterForm(Form):
    username = StringField(u'用户名', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField(u'密码', validators=[DataRequired()])
    email = EmailField(u'电子邮箱', validators=[DataRequired(), Email()])
    submit = SubmitField(u'注册')
