@echo off
set "exePath=%~dp0\app.exe"

REM 检查是否以管理员权限运行脚本
>nul 2>&1 "%SYSTEMROOT%\System32\cacls.exe" "%SYSTEMROOT%\System32\config\system"

REM 如果上一条命令的返回值不为0，说明不是以管理员权限运行的，则重新启动脚本以申请管理员权限
if %errorlevel% neq 0 (
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\GetAdmin.vbs"
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\GetAdmin.vbs"
    "%temp%\GetAdmin.vbs"
    del "%temp%\GetAdmin.vbs"
    exit /b
)

REM 注册mangaAIRepairerBackend协议
reg add HKEY_CLASSES_ROOT\mangaAIRepairerBackend /ve /d "Manga AI Repairer Backend" /f
reg add HKEY_CLASSES_ROOT\mangaAIRepairerBackend /v "URL Protocol" /d "" /f

REM 设置默认图标
reg add HKEY_CLASSES_ROOT\mangaAIRepairerBackend\DefaultIcon /ve /d "%exePath%,1" /f

REM 配置打开命令
reg add HKEY_CLASSES_ROOT\mangaAIRepairerBackend\shell\open\command /ve /d "%exePath% \"%%1\"" /f


REM 添加成功，等待用户按下任意键退出脚本
echo Done. Press any key to exit
pause >nul