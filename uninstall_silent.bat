@echo off
echo Uninstalling Spotify Tray App (silent)...

set APPDIR=%LOCALAPPDATA%\SpotifyTrayApp

call unregister_startup.bat

if exist "%APPDIR%" (
    rmdir /S /Q "%APPDIR%"
    echo Removed app directory.
)

echo Done.
