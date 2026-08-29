@echo off
title MONO Drag Enhancer Launcher
cd /d "%~dp0"

echo Starting MONO System-Wide Drag Enhancer in background...
start /b pythonw src\drag_drop_enhancer.py

echo.
echo MONO Drag Enhancer is now active in Windows background!
echo Whenever you drag text or files in any application, your custom MONO Drag cursor will appear.
echo To stop it anytime, double-click 'stop_drag_enhancer.bat'.
pause
