@echo off
SET EXEPATH=%~dp0dist\SpotifyTray.exe
SET SHORTCUT=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\SpotifyTrayApp.lnk
powershell -Command "$s=(New-Object -COM WScript.Shell).CreateShortcut('%SHORTCUT%'); $s.TargetPath='%EXEPATH%'; $s.Save()"
echo Startup shortcut created.
pause
