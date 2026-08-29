@echo off
title MONO Cursor Live Tester
cd /d "%~dp0"

echo Launching MONO Cursor Tester...
py test_busy.py
