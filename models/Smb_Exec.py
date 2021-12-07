#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os
from app.dbset import Tasklist

workpath = os.getcwd() # 获取当前代码所在的目录

# windows，连接到服务器smb服务执行基线检查脚本
class SmbExec:
    def __init__(self, smbip, smbusername, smbpassword, theorder):
        self.psexec = workpath + '\\models\\Tools\\PsExec.exe' #获取Windows需要用到的工具路径
        self.bat = workpath + '\\models\\Script\\windowscheck.bat' #获取Windows基线检查脚本路径
        self.rawpath = workpath + '\\models\\Raw\\Windows\\' #获取存放Windows初始检查文本的结果路径，及命令执行结果
        self.smbip = smbip
        self.smbusername = smbusername
        self.smbpassword = smbpassword
        self.theorder = theorder

    def exec(self): # 连接smb、执行检查脚本的功能
        if not os.path.exists(self.rawpath + self.theorder):   # 判断带theorder的目录是否存在
            os.mkdir(self.rawpath + self.theorder)
        # 把ip、账号、密码、基线检查脚本、>符号输出命令执行结果到文件
        cmd = self.psexec + ' \\\\' + self.smbip + ' -n 15 -u "' + self.smbusername + '" -p "' + self.smbpassword + '" -c ' + self.bat + ' > ' + self.rawpath + self.theorder + '\\' + self.smbip
        # .\PsExec.exe \\192.168.0.102 -n 5 -u administrator -p ceshi1234@ -c C:\Users\Test\Desktop\bs\baseline\models\Script\windowscheck.bat > rawpath+theorder+ip
        # psexec.exe 是windows通过smb远程执行命令的工具。
        os.system(cmd)   # 调用os.system函数执行拼接起来的命令
        # try异常处理中是通过start check、end check两行判断极限检查结果是否都返回。
        try:
            with open(self.rawpath + self.theorder + '\\' + self.smbip,'r') as f:
                startflag = 0
                endflag = 0
                for i in f.readlines():
                    if 'start check' in i:
                        startflag = 1
                    if 'end check' in i:
                        endflag = 1
                if startflag*endflag == 1:
                    return True
                else:
                    Tasklist.update(status='-1').where(Tasklist.theorder == self.theorder).execute()
                    return False
        except Exception as e:
            print(e) # 12
            Tasklist.update(status='-1').where(Tasklist.theorder == self.theorder).execute()
            return False