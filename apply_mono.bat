@echo off
title MONO Cursor Pack Installer
cd /d "%~dp0"

echo ===================================================
echo   MONO Cursor Pack - Windows 11 One-Click Setup
echo ===================================================
echo.

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0apply_mono.ps1"

echo.
pause
