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


def online(checkdef,form, view):
    # 在线模式，linux、windows用的同一个
    # 传入的参数 checkedf:是要执行的函数，linux和windows是两个不同的函数

    if request.method == 'POST':   # request.method为请求方式，请求方式为post时候进行下面的代码
        if form.validate_on_submit():   # 判断是不是有提交表单的参数
            ip = form.formip.raw_data[0] # 获取ip
            port = form.formport.raw_data[0] # 获取端口
            user = form.formuser.raw_data[0] # 获取用户名
            passwd = form.formpwd.raw_data[0] # 获取密码
            note = form.formnote.raw_data[0] # 获取备注
            theorder = ''.join(random.sample(string.digits, 10))
            cr = Tasklist.create(theorder=theorder, time=str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
                                 status='0', note=note)
            th1 = threading.Thread(target=checkdef, args=(ip, port, user, passwd, theorder,))
            th1.start()
            flash('任务提交成功，任务编号：' + theorder)
        else:
            utils.flash_errors(form)
    return render_template(view, form=form)



def offline(checkdef, systemtype, form, view): # lin_only_check  Linux
    # 离线模式，linux、windows用的同一个
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


# 报告下载页面的函数
def check_result(view):
    action = request.args.get('action')
    theorder = request.args.get('id')
    if action == 'delete':
        Tasklist.delete().where(Tasklist.theorder == theorder).execute()
    if action == 'down':
        (zipdir, zipbao) = file_to_zip(theorder)
        return send_from_directory(zipdir, zipbao, as_attachment=True)

    # 从这往下
    page = int(request.args.get('page')) if request.args.get('page') else 1
    length = int(request.args.get('length')) if request.args.get('length') else 10
    # 获取列表
    query = Tasklist.select().order_by(Tasklist.time.desc())
    total_count = query.count()
    # 处理分页
    if page: query = query.paginate(page, length)

    dict = {'content': utils.query_to_list(query), 'total_count': total_count,
            'total_page': math.ceil(total_count / length), 'page': page, 'length': length}

    return render_template(view, form=dict)

# 重置密码功能，就是从web中把旧密码和新密码获取过来，然后对比下旧密码是否正确，正确的话就把新密码加密保存到数据库user表中
def reset_passwd(form, view):           # 修改密码
    if request.method == 'POST':
        if form.validate_on_submit(): # 同上
            oldpwd = form.oldpwd.raw_data[0] # 获取旧密码
            newpwd = form.newpwd.raw_data[0] # 获取新密码
            user = User.get(User.username == current_user.username)  # 判断下用户名
            if user.verify_password(oldpwd): # 对比下旧密码是否正确
                user.update_password(current_user.username, newpwd) # 正确的话就保存新密码
                flash('管理员密码修改成功')
            else:
                flash('管理员原密码错误')
        else:
            utils.flash_errors(form)
    return render_template(view, form=form)

# 带有 .route 的都是定义的url

# 定义根目录url
@main.route('/', methods=['GET'])
@login_required
def root():
    return redirect(url_for('main.index'))


# 定义首页url
@main.route('/index', methods=['GET'])
@login_required
def index():
    num1 = Tasklist.select().count()
    num2 = Tasklist.select().where(Tasklist.status == '0').count()
    return render_template('index.html', num1=num1, num2=num2, current_user=current_user)


# 定义linux在线检查的url
@main.route('/onlinelinux', methods=['GET', 'POST'])
@login_required
def onlinelinux():
    checkdef = lin_execcheck
    return online(checkdef,LinuxForm(), 'onlinelinux.html')


# 定义windows在线检查的url
@main.route('/onlinewindows', methods=['GET', 'POST'])
@login_required
def onlinewindows():
    checkdef = win_execcheck
    return online(checkdef,WindowsForm(), 'onlinewindows.html')


# 定义linux离线检查的url
@main.route('/offlinelinux', methods=['GET', 'POST'])
@login_required
def offlinelinux():
    checkdef = lin_only_check
    systemtype = 'Linux'
    return offline(checkdef, systemtype, UploadForm(), 'offlinelinux.html')


# 定义windows离线检查的url
@main.route('/offlinewindows', methods=['GET', 'POST'])
@login_required
def offlinewindows():
    checkdef = win_only_check
    systemtype = 'Windows'
    return offline(checkdef, systemtype, UploadForm(), 'offlinewindows.html')


# 定义下载检查结果的url
@main.route('/result', methods=['GET', 'POST'])
@login_required
def result():
    return check_result('result.html')


# 定义重置密码的url
@main.route('/resetpwd', methods=['GET', 'POST'])
@login_required
def resetpwd():
    return reset_passwd(ResetpwdForm(), 'resetpwd.html')
