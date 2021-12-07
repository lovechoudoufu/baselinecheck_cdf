import os

from app.dbset import Tasklist
from models.Check_Win import CheckWin
from models.Smb_Exec import SmbExec

# 在线模式：执行+检查
def win_execcheck(ip, port, user, passwd, theorder):
    # port不去使用，因为windows的smb默认445，直接使用默认的
    workpath = os.getcwd()  # 获取当前根目录：xxxx/xxx/xxxx/baseline/
    se = SmbExec(ip, user, passwd, theorder)
    flag = se.exec()
    if flag == False:
        return False

    Rawipdir = workpath + '/models/Raw/Windows/' + theorder  # 存放windows基线检查脚本执行结果的目录
    for rawroot, rawdirs, ipfiles in os.walk(Rawipdir):
        for ipfile in ipfiles:
            ipfilepath = Rawipdir + '/' + ipfile
            # print(ipfilepath)
            cwin = CheckWin(ipfilepath, theorder, ipfile)
            cwin.check()
    Tasklist.update(status='1').where(Tasklist.theorder == theorder).execute()
    return True

# 离线模式：只检查
def win_only_check(Rawipdir,theorder):
    try:
        for rawroot, rawdirs, ipfiles in os.walk(Rawipdir):
            for ipfile in ipfiles:
                ipfilepath = rawroot + '\\' + ipfile
                clin = CheckWin(ipfilepath, theorder, ipfile)
                clin.check()
    except Exception as e:
        print(e)
        Tasklist.update(status='-1').where(Tasklist.theorder == theorder).execute()
        return False

    Tasklist.update(status='1').where(Tasklist.theorder == theorder).execute()
    return True