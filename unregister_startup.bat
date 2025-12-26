@echo off
SET SHORTCUT=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\SpotifyTrayApp.lnk
if exist "%SHORTCUT%" del "%SHORTCUT%"
echo Startup shortcut removed.
pause
