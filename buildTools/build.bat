@echo off
REM filepath: buildTools/build.bat

chcp 65001 >nul

echo 开始构建项目...
echo.

echo 1. 构建 registerMenu...
python -m PyInstaller ./buildTools/spec/registerMenu.spec
if %errorlevel% neq 0 (
    echo registerMenu 构建失败！
    pause
    exit /b 1
)
echo registerMenu 构建完成
echo.

echo 2. 构建 layoutImage...
python -m PyInstaller ./buildTools/spec/layoutImage.spec
if %errorlevel% neq 0 (
    echo layoutImage 构建失败！
    pause
    exit /b 1
)
echo layoutImage 构建完成
echo.

echo 3. 构建资源文件...
python ./buildTools/buildRes.py
if %errorlevel% neq 0 (
    echo 资源文件构建失败！
    pause
    exit /b 1
)
echo 资源文件构建完成
echo.

echo 4. 构建主程序 安建排图...
python -m PyInstaller ./buildTools/spec/安建排图.spec
if %errorlevel% neq 0 (
    echo 安建排图 构建失败！
    pause
    exit /b 1
)
echo 安建排图 构建完成
echo.

echo 所有构建任务完成！
pause