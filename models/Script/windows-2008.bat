@echo off
cd %USERPROFILE%
echo "start check" > baseline.txt
echo 1.系统信息(IsCheckLine) >> baseline.txt
	systeminfo >>　baseline.txt
echo 2.网卡信息(IsCheckLine) >> baseline.txt
	ipconfig >>　baseline.txt
echo 3.本地策略(IsCheckLine) >> baseline.txt
    secedit /export /cfg .\\temp.txt
    echo ---密码策略--- >> baseline.txt
    echo "0表示禁用，1表示启用" >> baseline.txt
    echo *密码必须符合复杂性要求* >> baseline.txt
    find "PasswordComplexity" .\\temp.txt |find "PasswordComplexity = ">> baseline.txt
    echo *密码长度最小值* >> baseline.txt
    find "MinimumPasswordLength" .\\temp.txt|find "MinimumPasswordLength = " >> baseline.txt
    echo *密码最短使用期限* >> baseline.txt
    find "MinimumPasswordAge" .\\temp.txt|find "MinimumPasswordAge = " >> baseline.txt
    echo *密码最长使用期限* >> baseline.txt
    find "MaximumPasswordAge" .\\temp.txt|find "MaximumPasswordAge = " >> baseline.txt
    echo *强制密码历史* >> baseline.txt
    find "PasswordHistorySize" .\\temp.txt|find "PasswordHistorySize = " >> baseline.txt
    echo *用可还原的加密来存储密码* >> baseline.txt
    find "ClearTextPassword" .\\temp.txt|find "ClearTextPassword = " >> baseline.txt
    echo ---账户锁定策略（无结果表示未开启）--- >> baseline.txt
    echo *账户锁定时间* >> baseline.txt
    find "LockoutDuration" .\\temp.txt |find "LockoutDuration" >> baseline.txt
    echo *复位账户锁定计时器* >> baseline.txt
    find "ResetLockoutCount" .\\temp.txt |find "ResetLockoutCount">> baseline.txt
    echo *账户锁定阈值* >> baseline.txt
    find "LockoutBadCount" .\\temp.txt |find "LockoutBadCount" >> baseline.txt
    echo ---审核策略--- >> baseline.txt
    echo ---0表示无审核，1表示成功审核，2表示失败审核，3表示成功和失败审核--- >> baseline.txt
    echo *审核帐户管理* >> baseline.txt
    find "AuditAccountManage" .\\temp.txt | find "AuditAccountManage" >> baseline.txt
    echo *审核帐户登录事件* >> baseline.txt
    find "AuditAccountLogon" .\\temp.txt | find "AuditAccountLogon" >> baseline.txt
    echo *审核系统事件* >> baseline.txt
    find "AuditSystemEvents" .\\temp.txt | find "AuditSystemEvents" >> baseline.txt
    echo *审核目录服务访问* >> baseline.txt
    find "AuditDSAccess" .\\temp.txt | find "AuditDSAccess" >> baseline.txt
    echo *审核过程跟踪* >> baseline.txt
    find "AuditProcessTracking" .\\temp.txt | find "AuditProcessTracking" >> baseline.txt
    echo *审核特权使用* >> baseline.txt
    find "AuditPrivilegeUse" .\\temp.txt | find "AuditPrivilegeUse" >> baseline.txt
    echo *审核对象访问* >> baseline.txt
    find "AuditObjectAccess" .\\temp.txt | find "AuditObjectAccess" >> baseline.txt
    echo *审核登录事件* >> baseline.txt
    find "AuditLogonEvents" .\\temp.txt | find "AuditLogonEvents" >> baseline.txt
    echo *审核策略更改* >> baseline.txt
    find "AuditPolicyChange" .\\temp.txt | find "AuditPolicyChange" >> baseline.txt
    echo ---安全选项--- >> baseline.txt
    echo *0表示已停用，1表示已启用* >> baseline.txt
    echo *在挂起会话之前所需的空闲时间* >> baseline.txt
    find "AutoDisconnect" .\\temp.txt | find "AutoDisconnect" >> baseline.txt
    echo *不显示上次登录的用户名* >> baseline.txt
    find "DontDisplayLastUserName" .\\temp.txt | find "DontDisplayLastUserName" >> baseline.txt
    echo *关机前清理虚拟内存页面* >> baseline.txt
    find "ClearPageFileAtShutdown" .\\temp.txt | find "ClearPageFileAtShutdown" >> baseline.txt
    echo *允许在未登录前关机* >> baseline.txt
    find "ShutdownWithoutLogon" .\\temp.txt | find "ShutdownWithoutLogon" >> baseline.txt
    echo ---用户权利分配---  >> baseline.txt
    echo (Everyone:*S-1-1-0  Administrators:*S-1-5-32-544  Users:*S-1-5-32-545  Power Users:*S-1-5-32-547  Backup Operators:*S-1-5-32-551) >> baseline.txt
    echo *从远程系统强制关机* >> baseline.txt
    find "SeRemoteShutdownPrivilege" .\\temp.txt | find "SeRemoteShutdownPrivilege" >> baseline.txt
    echo *取得文件或其他对象所有权* >> baseline.txt
    find "SeTakeOwnershipPrivilege" .\\temp.txt | find "SeTakeOwnershipPrivilege" >> baseline.txt
	echo *从本地登录此计算机* >> baseline.txt
    find "SeInteractiveLogonRight" .\\temp.txt | find "SeInteractiveLogonRight" >> baseline.txt
    echo *允许通过远程桌面服务登录* >> baseline.txt
    find "SeRemoteInteractiveLogonRight" .\\temp.txt | find "SeRemoteInteractiveLogonRight" >> baseline.txt
	echo *调试程序* >> baseline.txt
    find "SeDebugPrivilege" .\\temp.txt | find "SeDebugPrivilege" >> baseline.txt
	echo *更改系统时间* >> baseline.txt
    find "SeSystemtimePrivilege" .\\temp.txt | find "SeSystemtimePrivilege" >> baseline.txt
	echo *管理审核和安全日志* >> baseline.txt
    find "SeSecurityPrivilege" .\\temp.txt | find "SeSecurityPrivilege" >> baseline.txt
    del .\\temp.txt
echo 4.系统用户(IsCheckLine) >> baseline.txt
    net user >> baseline.txt
    for /f "skip=4 delims=" %%a in ('net user^|findstr /vx "命令成功完成。"') do for %%i in (%%a) do net user %%i >> baseline.txt
    net localgroup >> baseline.txt
    net localgroup Administrators >> baseline.txt	
	net localgroup Guests >> baseline.txt	
echo 5.其它选项(IsCheckLine) >> baseline.txt	
	echo *自动播放* （oxff为关闭全部自动播放，无结果则开启） >> baseline.txt
    reg query HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoDriveTypeAutoRun |find "NoDriveTypeAutoRun" >> baseline.txt
	echo *防火墙状态*（1开，0关）>> baseline.txt
    reg query HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\SharedAccess\Parameters\FirewallPolicy\StandardProfile /v EnableFirewall |find "EnableFirewall" >> baseline.txt
	echo *远程桌面* (0开，1关) >> baseline.txt
    reg query "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections |find "fDenyTSConnections" >> baseline.txt
    echo *3389端口* (d3d:3389) >> baseline.txt
    reg query "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v PortNumber |find "PortNumber" >> baseline.txt
	echo *日志文件大小*  >> baseline.txt
	echo *应用日志文件大小*（0x2800000以上为合规）  >> baseline.txt
	reg query "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\Eventlog\Application" /v MaxSize |find "MaxSize" >> baseline.txt
	echo *达到事件日志最大大小时*（不存在或0均合规）  >> baseline.txt
	reg query "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\Eventlog\Application" /v Retention |find "Retention" >> baseline.txt
	echo *安全日志文件大小*（0x2800000以上为合规）  >> baseline.txt
	reg query "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\Eventlog\Security" /v MaxSize |find "MaxSize" >> baseline.txt
	echo *达到事件日志最大大小时*（不存在或0均合规）  >> baseline.txt
	reg query "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\Eventlog\Security" /v Retention |find "Retention" >> baseline.txt
	echo *系统日志文件大小*（0x2800000以上为合规）  >> baseline.txt
	reg query "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\Eventlog\System" /v MaxSize |find "MaxSize" >> baseline.txt
	echo *达到事件日志最大大小时*（不存在或0均合规）  >> baseline.txt
	reg query "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\Eventlog\System" /v Retention |find "Retention" >> baseline.txt
	echo *默认共享*（注册表 + net share查看）  >> baseline.txt
	echo *分区共享*（存在且为0，为合规）  >> baseline.txt
	reg query "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\lanmanserver\parameters" /v AutoShareServer |find "AutoShareServer" >> baseline.txt
	echo *ADMIN共享*（存在且为0，为合规） >> baseline.txt
	reg query "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\lanmanserver\parameters" /v AutoShareWks |find "AutoShareWks" >> baseline.txt
	echo *IPC共享* （存在且为1，为合规） >> baseline.txt
	reg query "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa" /v restrictanonymous |find "restrictanonymous" >> baseline.txt
	echo *共享列表*  >> baseline.txt
	reg query "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\lanmanserver\shares" >> baseline.txt
	echo *默认共享*  >> baseline.txt
	net share >> baseline.txt
	copy C:\Windows\WindowsUpdate.log .\
	set filePath=.\\WindowsUpdate.log
 	for /f  %%i in (%filePath%) do (
		set lastLine=%%i
	)
 	echo WindowsUpdate:%lastLine%>> baseline.txt
 	del .\\WindowsUpdate.log
 	echo "end check" >> baseline.txt
type baseline.txt
del baseline.txt