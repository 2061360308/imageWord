@echo off
REM filepath: e:\imageWord\buildTools\nuitka.bat

chcp 65001 >nul

echo 开始使用 Nuitka 构建项目...
echo.

echo 1. 构建 registerMenu.py...
python -m nuitka --onefile --windows-console-mode=attach --output-dir=dist --output-filename=registerMenu.exe registerMenu.py
if %errorlevel% neq 0 (
    echo registerMenu 构建失败！
    pause
    exit /b 1
)
echo registerMenu 构建完成
echo.

echo 2. 构建 layoutImage.py...
python -m nuitka --onefile --windows-console-mode=attach --output-dir=dist --output-filename=layoutImage.exe layoutImage.py
if %errorlevel% neq 0 (
    echo layoutImage 构建失败！
    pause
    exit /b 1
)
echo layoutImage 构建完成
echo.


echo 3. 构建 resources_rc.py...
python ./buildTools/buildRes.py
if %errorlevel% neq 0 (
    echo 资源文件构建失败！
    pause
    exit /b 1
)
echo 资源文件构建完成
echo.

echo 4. 构建 main.py...
python -m nuitka --onefile --windows-console-mode=attach --enable-plugin=pyside6 --windows-icon-from-ico=logo.ico --output-dir=dist --output-filename=安建排图.exe main.py
if %errorlevel% neq 0 (
    echo main.py 构建失败！
    pause
    exit /b 1
)
echo main.py 构建完成
echo.

echo 所有 Nuitka 构建任务完成！
echo 构建文件位于 dist 目录下
pause