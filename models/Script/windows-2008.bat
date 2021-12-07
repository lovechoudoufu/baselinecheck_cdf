@echo off
cd %USERPROFILE%
echo "start check" > baseline.txt
echo 1.ϵͳ��Ϣ(IsCheckLine) >> baseline.txt
	systeminfo >>��baseline.txt
echo 2.������Ϣ(IsCheckLine) >> baseline.txt
	ipconfig >>��baseline.txt
echo 3.���ز���(IsCheckLine) >> baseline.txt
    secedit /export /cfg .\\temp.txt
    echo ---�������--- >> baseline.txt
    echo "0��ʾ���ã�1��ʾ����" >> baseline.txt
    echo *���������ϸ�����Ҫ��* >> baseline.txt
    find "PasswordComplexity" .\\temp.txt |find "PasswordComplexity = ">> baseline.txt
    echo *���볤����Сֵ* >> baseline.txt
    find "MinimumPasswordLength" .\\temp.txt|find "MinimumPasswordLength = " >> baseline.txt
    echo *�������ʹ������* >> baseline.txt
    find "MinimumPasswordAge" .\\temp.txt|find "MinimumPasswordAge = " >> baseline.txt
    echo *�����ʹ������* >> baseline.txt
    find "MaximumPasswordAge" .\\temp.txt|find "MaximumPasswordAge = " >> baseline.txt
    echo *ǿ��������ʷ* >> baseline.txt
    find "PasswordHistorySize" .\\temp.txt|find "PasswordHistorySize = " >> baseline.txt
    echo *�ÿɻ�ԭ�ļ������洢����* >> baseline.txt
    find "ClearTextPassword" .\\temp.txt|find "ClearTextPassword = " >> baseline.txt
    echo ---�˻��������ԣ��޽����ʾδ������--- >> baseline.txt
    echo *�˻�����ʱ��* >> baseline.txt
    find "LockoutDuration" .\\temp.txt |find "LockoutDuration" >> baseline.txt
    echo *��λ�˻�������ʱ��* >> baseline.txt
    find "ResetLockoutCount" .\\temp.txt |find "ResetLockoutCount">> baseline.txt
    echo *�˻�������ֵ* >> baseline.txt
    find "LockoutBadCount" .\\temp.txt |find "LockoutBadCount" >> baseline.txt
    echo ---��˲���--- >> baseline.txt
    echo ---0��ʾ����ˣ�1��ʾ�ɹ���ˣ�2��ʾʧ����ˣ�3��ʾ�ɹ���ʧ�����--- >> baseline.txt
    echo *����ʻ�����* >> baseline.txt
    find "AuditAccountManage" .\\temp.txt | find "AuditAccountManage" >> baseline.txt
    echo *����ʻ���¼�¼�* >> baseline.txt
    find "AuditAccountLogon" .\\temp.txt | find "AuditAccountLogon" >> baseline.txt
    echo *���ϵͳ�¼�* >> baseline.txt
    find "AuditSystemEvents" .\\temp.txt | find "AuditSystemEvents" >> baseline.txt
    echo *���Ŀ¼�������* >> baseline.txt
    find "AuditDSAccess" .\\temp.txt | find "AuditDSAccess" >> baseline.txt
    echo *��˹��̸���* >> baseline.txt
    find "AuditProcessTracking" .\\temp.txt | find "AuditProcessTracking" >> baseline.txt
    echo *�����Ȩʹ��* >> baseline.txt
    find "AuditPrivilegeUse" .\\temp.txt | find "AuditPrivilegeUse" >> baseline.txt
    echo *��˶������* >> baseline.txt
    find "AuditObjectAccess" .\\temp.txt | find "AuditObjectAccess" >> baseline.txt
    echo *��˵�¼�¼�* >> baseline.txt
    find "AuditLogonEvents" .\\temp.txt | find "AuditLogonEvents" >> baseline.txt
    echo *��˲��Ը���* >> baseline.txt
    find "AuditPolicyChange" .\\temp.txt | find "AuditPolicyChange" >> baseline.txt
    echo ---��ȫѡ��--- >> baseline.txt
    echo *0��ʾ��ͣ�ã�1��ʾ������* >> baseline.txt
    echo *�ڹ���Ự֮ǰ����Ŀ���ʱ��* >> baseline.txt
    find "AutoDisconnect" .\\temp.txt | find "AutoDisconnect" >> baseline.txt
    echo *����ʾ�ϴε�¼���û���* >> baseline.txt
    find "DontDisplayLastUserName" .\\temp.txt | find "DontDisplayLastUserName" >> baseline.txt
    echo *�ػ�ǰ���������ڴ�ҳ��* >> baseline.txt
    find "ClearPageFileAtShutdown" .\\temp.txt | find "ClearPageFileAtShutdown" >> baseline.txt
    echo *������δ��¼ǰ�ػ�* >> baseline.txt
    find "ShutdownWithoutLogon" .\\temp.txt | find "ShutdownWithoutLogon" >> baseline.txt
    echo ---�û�Ȩ������---  >> baseline.txt
    echo (Everyone:*S-1-1-0  Administrators:*S-1-5-32-544  Users:*S-1-5-32-545  Power Users:*S-1-5-32-547  Backup Operators:*S-1-5-32-551) >> baseline.txt
    echo *��Զ��ϵͳǿ�ƹػ�* >> baseline.txt
    find "SeRemoteShutdownPrivilege" .\\temp.txt | find "SeRemoteShutdownPrivilege" >> baseline.txt
    echo *ȡ���ļ���������������Ȩ* >> baseline.txt
    find "SeTakeOwnershipPrivilege" .\\temp.txt | find "SeTakeOwnershipPrivilege" >> baseline.txt
	echo *�ӱ��ص�¼�˼����* >> baseline.txt
    find "SeInteractiveLogonRight" .\\temp.txt | find "SeInteractiveLogonRight" >> baseline.txt
    echo *����ͨ��Զ����������¼* >> baseline.txt
    find "SeRemoteInteractiveLogonRight" .\\temp.txt | find "SeRemoteInteractiveLogonRight" >> baseline.txt
	echo *���Գ���* >> baseline.txt
    find "SeDebugPrivilege" .\\temp.txt | find "SeDebugPrivilege" >> baseline.txt
	echo *����ϵͳʱ��* >> baseline.txt
    find "SeSystemtimePrivilege" .\\temp.txt | find "SeSystemtimePrivilege" >> baseline.txt
	echo *������˺Ͱ�ȫ��־* >> baseline.txt
    find "SeSecurityPrivilege" .\\temp.txt | find "SeSecurityPrivilege" >> baseline.txt
    del .\\temp.txt
echo 4.ϵͳ�û�(IsCheckLine) >> baseline.txt
    net user >> baseline.txt
    for /f "skip=4 delims=" %%a in ('net user^|findstr /vx "����ɹ���ɡ�"') do for %%i in (%%a) do net user %%i >> baseline.txt
    net localgroup >> baseline.txt
    net localgroup Administrators >> baseline.txt	
	net localgroup Guests >> baseline.txt	
echo 5.����ѡ��(IsCheckLine) >> baseline.txt	
	echo *�Զ�����* ��oxffΪ�ر�ȫ���Զ����ţ��޽�������� >> baseline.txt
    reg query HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoDriveTypeAutoRun |find "NoDriveTypeAutoRun" >> baseline.txt
	echo *����ǽ״̬*��1����0�أ�>> baseline.txt
    reg query HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\SharedAccess\Parameters\FirewallPolicy\StandardProfile /v EnableFirewall |find "EnableFirewall" >> baseline.txt
	echo *Զ������* (0����1��) >> baseline.txt
    reg query "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections |find "fDenyTSConnections" >> baseline.txt
    echo *3389�˿�* (d3d:3389) >> baseline.txt
    reg query "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v PortNumber |find "PortNumber" >> baseline.txt
	echo *��־�ļ���С*  >> baseline.txt
	echo *Ӧ����־�ļ���С*��0x2800000����Ϊ�Ϲ棩  >> baseline.txt
	reg query "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\Eventlog\Application" /v MaxSize |find "MaxSize" >> baseline.txt
	echo *�ﵽ�¼���־����Сʱ*�������ڻ�0���Ϲ棩  >> baseline.txt
	reg query "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\Eventlog\Application" /v Retention |find "Retention" >> baseline.txt
	echo *��ȫ��־�ļ���С*��0x2800000����Ϊ�Ϲ棩  >> baseline.txt
	reg query "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\Eventlog\Security" /v MaxSize |find "MaxSize" >> baseline.txt
	echo *�ﵽ�¼���־����Сʱ*�������ڻ�0���Ϲ棩  >> baseline.txt
	reg query "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\Eventlog\Security" /v Retention |find "Retention" >> baseline.txt
	echo *ϵͳ��־�ļ���С*��0x2800000����Ϊ�Ϲ棩  >> baseline.txt
	reg query "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\Eventlog\System" /v MaxSize |find "MaxSize" >> baseline.txt
	echo *�ﵽ�¼���־����Сʱ*�������ڻ�0���Ϲ棩  >> baseline.txt
	reg query "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\Eventlog\System" /v Retention |find "Retention" >> baseline.txt
	echo *Ĭ�Ϲ���*��ע��� + net share�鿴��  >> baseline.txt
	echo *��������*��������Ϊ0��Ϊ�Ϲ棩  >> baseline.txt
	reg query "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\lanmanserver\parameters" /v AutoShareServer |find "AutoShareServer" >> baseline.txt
	echo *ADMIN����*��������Ϊ0��Ϊ�Ϲ棩 >> baseline.txt
	reg query "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\lanmanserver\parameters" /v AutoShareWks |find "AutoShareWks" >> baseline.txt
	echo *IPC����* ��������Ϊ1��Ϊ�Ϲ棩 >> baseline.txt
	reg query "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa" /v restrictanonymous |find "restrictanonymous" >> baseline.txt
	echo *�����б�*  >> baseline.txt
	reg query "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\lanmanserver\shares" >> baseline.txt
	echo *Ĭ�Ϲ���*  >> baseline.txt
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