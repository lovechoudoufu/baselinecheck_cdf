#!/usr/bin/python3
# -*- coding:utf-8 -*-
import math
import os
import random
import string
import threading
import time

from flask import url_for, render_template, request, flash, send_from_directory
from flask_login import login_required, current_user
from werkzeug.utils import redirect

from . import main
from app import utils

from models.Lin_exec_check import lin_execcheck, lin_only_check
from models.win_exec_check import win_execcheck, win_only_check
from app.main.forms import LinuxForm, WindowsForm, ResetpwdForm, UploadForm

from app.dbset import Tasklist, User
from app.utils import file_to_zip, zip_to_file


def online(checkdef, form, view):
    if request.method == 'POST':
        if form.validate_on_submit():
            ip = form.formip.raw_data[0]
            port = form.formport.raw_data[0]
            user = form.formuser.raw_data[0]
            passwd = form.formpwd.raw_data[0]
            note = form.formnote.raw_data[0]
            theorder = ''.join(random.sample(string.digits, 10))
            cr = Tasklist.create(theorder=theorder, time=str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
                                 status='0', note=note)
            th1 = threading.Thread(target=checkdef, args=(ip, port, user, passwd, theorder,))
            th1.start()
            flash('任务提交成功，任务编号：' + theorder)
        else:
            utils.flash_errors(form)
    return render_template(view, form=form)


def offline(checkdef, systemtype, form, view):
    if request.method == 'POST':
        theorder = ''.join(random.sample(string.digits, 10))
        note = form.formnote.raw_data[0]
        zipfile = request.files.get('formfile')
        workpath = os.getcwd()
        zip_src = workpath + '/models/temp/' + theorder + '.zip'
        zipfile.save(zip_src)
        Rawipdir = zip_to_file(theorder, zip_src, systemtype)
        if Rawipdir == 'notzip':
            flash('zip压缩包格式错误或有损')
            return render_template(view, form=form)
        cr = Tasklist.create(theorder=theorder, time=str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
                             status='0',
                             note=note)
        th1 = threading.Thread(target=checkdef, args=(Rawipdir, theorder,))
        th1.start()
        flash('任务提交成功，任务编号：' + theorder)
    return render_template(view, form=form)


def check_result(view):
    action = request.args.get('action')
    theorder = request.args.get('id')
    if action == 'delete':
        Tasklist.delete().where(Tasklist.theorder == theorder).execute()
    if action == 'down':
        (zipdir, zipbao) = file_to_zip(theorder)
        return send_from_directory(zipdir, zipbao, as_attachment=True)

    page = int(request.args.get('page')) if request.args.get('page') else 1
    length = int(request.args.get('length')) if request.args.get('length') else 10

    query = Tasklist.select().order_by(Tasklist.time.desc())
    total_count = query.count()

    if page: query = query.paginate(page, length)

    dict = {'content': utils.query_to_list(query), 'total_count': total_count,
            'total_page': math.ceil(total_count / length), 'page': page, 'length': length}

    return render_template(view, form=dict)


def reset_passwd(form, view):
    if request.method == 'POST':
        if form.validate_on_submit():
            oldpwd = form.oldpwd.raw_data[0]
            newpwd = form.newpwd.raw_data[0]
            user = User.get(User.username == current_user.username)
            if user.verify_password(oldpwd):
                user.update_password(current_user.username, newpwd)
                flash('管理员密码修改成功')
            else:
                flash('管理员原密码错误')
        else:
            utils.flash_errors(form)
    return render_template(view, form=form)


@main.route('/', methods=['GET'])
@login_required
def root():
    return redirect(url_for('main.index'))


@main.route('/index', methods=['GET'])
@login_required
def index():
    num1 = Tasklist.select().count()
    num2 = Tasklist.select().where(Tasklist.status == '0').count()
    return render_template('index.html', num1=num1, num2=num2, current_user=current_user)


@main.route('/onlinelinux', methods=['GET', 'POST'])
@login_required
def onlinelinux():
    checkdef = lin_execcheck
    return online(checkdef, LinuxForm(), 'onlinelinux.html')


@main.route('/onlinewindows', methods=['GET', 'POST'])
@login_required
def onlinewindows():
    checkdef = win_execcheck
    return online(checkdef, WindowsForm(), 'onlinewindows.html')


@main.route('/offlinelinux', methods=['GET', 'POST'])
@login_required
def offlinelinux():
    checkdef = lin_only_check
    systemtype = 'Linux'
    return offline(checkdef, systemtype, UploadForm(), 'offlinelinux.html')


@main.route('/offlinewindows', methods=['GET', 'POST'])
@login_required
def offlinewindows():
    checkdef = win_only_check
    systemtype = 'Windows'
    return offline(checkdef, systemtype, UploadForm(), 'offlinewindows.html')


@main.route('/result', methods=['GET', 'POST'])
@login_required
def result():
    return check_result('result.html')


@main.route('/resetpwd', methods=['GET', 'POST'])
@login_required
def resetpwd():
    return reset_passwd(ResetpwdForm(), 'resetpwd.html')
