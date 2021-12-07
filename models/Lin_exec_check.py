#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os

from app.dbset import Tasklist
from models.Check_Lin import CheckLin
from models.Ssh_Exec import SshExec

# 在线模式：执行+检查
def lin_execcheck(ip, port, user, passwd, theorder):
    # 远程连接到服务器执行基线检查脚本的命令
    try:
        sshe = SshExec(ip, port, user, passwd, theorder)
        sshe.exec()
    except Exception as e:
        print(e)
        Tasklist.update(status='-1').where(Tasklist.theorder==theorder).execute()
        return False

    # 根据脚本执行结果整理成报告
    workpath = os.getcwd()
    Rawipdir = workpath + '/models/Raw/Linux/' + theorder
    for rawroot, rawdirs, ipfiles in os.walk(Rawipdir):
        for ipfile in ipfiles:
            ipfilepath = Rawipdir + '/' + ipfile
            clin = CheckLin(ipfilepath, theorder, ipfile)
            clin.check()
    Tasklist.update(status='1').where(Tasklist.theorder == theorder).execute()
    return True

# 离线模式：检查
def lin_only_check(Rawipdir,theorder):
    try:
        for rawroot, rawdirs, ipfiles in os.walk(Rawipdir):
            for ipfile in ipfiles:
                ipfilepath = rawroot + '\\' + ipfile
                clin = CheckLin(ipfilepath, theorder, ipfile)
                clin.check()
    except Exception as e:
        print('lin_only_check error : '+str(e))
        Tasklist.update(status='-1').where(Tasklist.theorder == theorder).execute()  # 任务失败
        return False
    Tasklist.update(status='1').where(Tasklist.theorder == theorder).execute()   # 任务成功
    return True