# -*- coding: utf-8 -*-

from flask.ext.login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
