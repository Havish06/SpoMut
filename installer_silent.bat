@echo off
SET EXE=dist\SpotifyTray.exe
SET SETTINGS=dist\settings_tk.exe
SET DEST=%ProgramFiles%\SpotifyTrayApp
echo Installing SpotifyTrayApp silently...
if not exist "%DEST%" mkdir "%DEST%"
xcopy "%EXE%" "%DEST%\" /Y
xcopy "%SETTINGS%" "%DEST%\" /Y
xcopy "resources" "%DEST%\resources" /E /I /Y
powershell -Command "$s=(New-Object -COM WScript.Shell).CreateShortcut('$env:APPDATA\\Microsoft\\Windows\\Start Menu\\Programs\\SpotifyTrayApp.lnk'); $s.TargetPath='%DEST%\\SpotifyTray.exe'; $s.Save()"
powershell -Command "$s=(New-Object -COM WScript.Shell).CreateShortcut('$env:APPDATA\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\SpotifyTrayApp.lnk'); $s.TargetPath='%DEST%\\SpotifyTray.exe'; $s.Save()"
echo Done.
pause
