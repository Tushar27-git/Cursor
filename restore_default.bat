@echo off
title Restore Default Windows Cursors
cd /d "%~dp0"

echo ===================================================
echo   Restore Default Windows Cursors
echo ===================================================
echo.

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0restore_default.ps1"

echo.
pause
