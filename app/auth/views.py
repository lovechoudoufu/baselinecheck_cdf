#!/usr/bin/python3
# -*- coding:utf-8 -*-


from flask import render_template, redirect, request, url_for, flash
from . import auth
from app.auth.forms import LoginForm
from app.dbset import User
from flask_login import login_user, logout_user, login_required


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = User.get(User.username == str(form.username.data))
            if user.verify_password(form.password.data):
                login_user(user, form.rememberme.data)
                return redirect(request.args.get('next') or url_for('main.index'))
            else:
                flash('用户名或密码错误')
        except Exception as e:

            flash('用户名或密码错误')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('已退出登录')
    return redirect(url_for('auth.login'))
