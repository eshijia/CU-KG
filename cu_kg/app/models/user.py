# -*- coding: utf-8 -*-

from werkzeug.security import generate_password_hash, check_password_hash

from cu_kg.app import db

from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(64), unique=True, index=True)
    password = db.Column('password', db.String(128))
    email = db.Column('email', db.String(50), unique=True, index=True)
    registered_on = db.Column('registered_on', db.DateTime)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __init__(self, username, password, email):
        self.username = username
        self.set_password(password)
        self.email = email
        self.registered_on = datetime.utcnow()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def is_admin(self):
        return self.role_id == 1

    def __repr__(self):
        return '<User %r>' % self.username


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    users = db.relationship('User', backref='role', lazy='dynamic')


