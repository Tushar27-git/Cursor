@echo off
title Stop MONO Drag Enhancer
echo Stopping MONO Drag Enhancer background processes...
wmic process where "commandline like '%%drag_drop_enhancer.py%%'" call terminate >nul 2>&1
echo Done! MONO Drag Enhancer stopped.
pause
