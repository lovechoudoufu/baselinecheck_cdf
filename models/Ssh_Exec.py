#!/usr/bin/python3
# -*- coding:utf-8 -*-

import paramiko
import os

workpath = os.getcwd()  # 获取当前代码所在的目录

# linux连接到服务器ssh服务执行基线检查脚本
class SshExec:
    # init是类的初始化函数
    def __init__(self, sship, sshport, sshusername, sshpasswd, theorder):
        self.sship = sship
        self.sshport = sshport
        self.sshusername = sshusername
        self.sshpasswd = sshpasswd
        self.theorder = theorder
        self.rawpath = workpath + '\\models\\Raw\\Linux\\'    # 检查脚本执行后的原始结果的存放目录，
        self.sh = workpath + '\\models\\Script\\linuxcheck.sh'   # linux基线检查脚本的地址

    def exec(self):     # 连接ssh、执行检查脚本的功能
        if not os.path.exists(self.rawpath + self.theorder):   # 判断带theorder的目录是否存在
            os.mkdir(self.rawpath + self.theorder)
        # 定义一个SSHClient的参数
        client = paramiko.SSHClient()
        # 自动添加策略，保存服务器的主机名和密钥信息
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接SSH服务，以用户名和密码进行认证
        client.connect(hostname=self.sship, port=self.sshport, username=self.sshusername, password=self.sshpasswd,timeout=15)
        with open(self.sh, 'r', encoding='UTF-8') as shfile:   # 以读取的形式utf-8编码打开linux基线检查脚本
            for cmd in shfile.readlines():  # readlines读取所有行，for cmd in xxxx从多行中一行行拿出来
                if cmd[0] != "#":  # 判断这行开头是不是#号，#号那行是注释，不是#时候执行后面的代码
                    stdin, stdout, stderr = client.exec_command(cmd) # 调用第三方库中exec_command函数执行这行命令，命令执行结果保存在stdout中
                    with open(self.rawpath + self.theorder + '\\' + self.sship, 'a') as g:  # 以追加写入的方式打开C:\Users\test\Desktop\baseline\baselinev5\models\Raw\Linux\6425379801\192.168.0.107
                        g.write(stdout.read().decode('utf-8'))   # stdout.read()获取命令执行结果保存到文件中
