#!/usr/bin/python3
# -*- coding:utf-8 -*-

from flask import Flask
from flask_login import LoginManager
from conf.config import config

global fapp

fapp = Flask(__name__)  # 调用Flask框架，整个web的功能都是基于flask框架的。

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'    # 设置login的验证地址  auth文件夹login的url


def create_app():
    fapp.config.from_object(config['default'])
    login_manager.init_app(fapp)
    from .main import main as main_blueprint
    fapp.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    fapp.register_blueprint(auth_blueprint)

    return fapp
