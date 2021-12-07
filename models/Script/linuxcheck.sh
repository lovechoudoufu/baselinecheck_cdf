#删除原有baseline_check.txt
rm -f /tmp/baseline_check.txt
echo 'start check' > /tmp/baseline_check.txt
#网卡ip信息
echo '1.ip(IsCheckLine)' >> /tmp/baseline_check.txt
ip addr | grep brd | grep inet >> /tmp/baseline_check.txt
#系统内核版本
echo '2.system(IsCheckLine)' >> /tmp/baseline_check.txt
uname -a >> /tmp/baseline_check.txt
echo '3.user(IsCheckLine)' >> /tmp/baseline_check.txt
#可登录的账户
awk -F[:] 'NR!=0{print $1,$3,$4,$7}' /etc/passwd >> /tmp/baseline_check.txt
echo '4.group(IsCheckLine)' >> /tmp/baseline_check.txt
#root组账户
awk -F[:] '$1=="root" {print "rootgroup:" $4}' /etc/group >> /tmp/baseline_check.txt
#可使用sudo su提升权限为root权限的用户
cat /etc/sudoers | grep 'ALL=' | grep -v ^# | grep -v ^% >> /tmp/baseline_check.txt
echo '5.password(IsCheckLine)' >> /tmp/baseline_check.txt
#密码强制更改周期
cat /etc/login.defs | grep PASS_MAX_DAYS | grep -v ^# >> /tmp/baseline_check.txt
#密码更改最小时间间隔
cat /etc/login.defs | grep PASS_MIN_DAYS | grep -v ^# >> /tmp/baseline_check.txt
#密码过期警告时间天数
cat /etc/login.defs | grep PASS_WARN_AGE | grep -v ^# >> /tmp/baseline_check.txt
#密码最小长度
cat /etc/login.defs | grep PASS_MIN_LEN | grep -v ^# >> /tmp/baseline_check.txt
#密码错误次数和锁定时间
cat /etc/pam.d/sshd | grep -i -E "unlock_time|deny" | grep -v ^# >> /tmp/baseline_check.txt
#umask数值：指定在建立文件时预设的权限
echo '6.umask(IsCheckLine)' >> /tmp/baseline_check.txt
printf umask:`umask`\\n >> /tmp/baseline_check.txt
echo '7.log(IsCheckLine)' >> /tmp/baseline_check.txt
#是否开启rsyslog或syslog日志服务
ps -ef | grep -i -E 'rsyslog|syslog' >> /tmp/baseline_check.txt
#是否开启auditd日志审计服务
ps -ef | grep auditd >> /tmp/baseline_check.txt
#是否有登录错误日志（btmp）、登录日志（wtmp）、安全日志（secure）、最近一次登录信息（lastlog）
ls /var/log/ | grep -i -E "btmp|wtmp|secure|lastlog" >> /tmp/baseline_check.txt
echo '8.login(IsCheckLine)' >> /tmp/baseline_check.txt
#是否禁用root远程登录
echo 'if not is null' >> /tmp/baseline_check.txt
cat /etc/ssh/sshd_config | grep PermitRootLogin | grep -v ^# >> /tmp/baseline_check.txt
echo '9.telnet(IsCheckLine)' >> /tmp/baseline_check.txt
#是否关闭telnet服务
ps -ef |grep telnet >> /tmp/baseline_check.txt
echo '10.rsalogin(IsCheckLine)' >> /tmp/baseline_check.txt
#是否配置ssh免密登录
echo 'if not is null' >> /tmp/baseline_check.txt
find /root/ -name authorized_keys >> /tmp/baseline_check.txt
find /home/ -name authorized_keys >> /tmp/baseline_check.txt
echo '11.webuser(IsCheckLine)' >> /tmp/baseline_check.txt
#web服务运行权限
echo 'if not is null' >> /tmp/baseline_check.txt
ps -aux | grep -i -E "tomcat|weblogic|httpd|jboss|nginx|apache" >> /tmp/baseline_check.txt
echo '12.distused(IsCheckLine)' >> /tmp/baseline_check.txt
#linux硬盘使用有没有超过80%
df -h >> /tmp/baseline_check.txt
#重要文件的文件权限
echo '13.filepermission(IsCheckLine)' >> /tmp/baseline_check.txt
ls -l /etc/passwd | awk '{print "/etc/passwd " $1}' >> /tmp/baseline_check.txt
ls -l /etc/shadow | awk '{print "/etc/shadow " $1}' >> /tmp/baseline_check.txt
ls -l /etc/sudoers | awk '{print "/etc/sudoers " $1}' >> /tmp/baseline_check.txt
ls -l /etc/group | awk '{print "/etc/group " $1}' >> /tmp/baseline_check.txt
ls -l /etc/profile | awk '{print "/etc/profile " $1}' >> /tmp/baseline_check.txt
#查看结果
echo 'end check' >> /tmp/baseline_check.txt
cat /tmp/baseline_check.txt