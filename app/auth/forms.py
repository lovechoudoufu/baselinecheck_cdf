#!/usr/bin/python3
# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

# 定义web的表单（表单就是web页面上要填写的框框）登录的表单。
class LoginForm(FlaskForm):
    username = StringField('账户', validators=[DataRequired(), Length(1, 64), ])   # 账号的表单，限制了长度最大为64位
    password = PasswordField('密码', validators=[DataRequired()])
    rememberme = BooleanField('记住我')
    submit = SubmitField('登录')     # 提交按钮

