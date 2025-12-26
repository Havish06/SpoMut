!define APPNAME "SpotifyTrayApp"
!define VERSION "1.0"
!define COMPANY "YourCompany"
!define EXEFILE "SpotifyTray.exe"
!define SETTINGS_EXE "settings_tk.exe"
!define INSTALLDIR "$PROGRAMFILES\\${APPNAME}"

Name "${APPNAME} ${VERSION}"
OutFile "build\\${APPNAME}-installer-${VERSION}.exe"
InstallDir "${INSTALLDIR}"
RequestExecutionLevel admin

Page directory
Page instfiles
UninstPage uninstConfirm
UninstPage instfiles

Section "Install"
  SetOutPath "$INSTDIR"
  File /r "dist\\${EXEFILE}"
  File /r "dist\\${SETTINGS_EXE}"
  File /r "resources\\*.*"
  CreateShortCut "$SMPROGRAMS\\${APPNAME}.lnk" "$INSTDIR\\${EXEFILE}"
  CreateShortCut "$DESKTOP\\${APPNAME}.lnk" "$INSTDIR\\${EXEFILE}"
  WriteUninstaller "$INSTDIR\\Uninstall.exe"
  WriteRegStr HKCU "Software\\${COMPANY}\\${APPNAME}" "Install_Dir" "$INSTDIR"
SectionEnd

Section "InstallStartup"
  InitPluginsDir
  CreateDirectory "$SMPROGRAMS\\Startup"
  CreateShortCut "$SMPROGRAMS\\Startup\\${APPNAME}.lnk" "$INSTDIR\\${EXEFILE}"
SectionEnd

Section "Uninstall"
  Delete "$INSTDIR\\${EXEFILE}"
  Delete "$DESKTOP\\${APPNAME}.lnk"
  Delete "$SMPROGRAMS\\${APPNAME}.lnk"
  Delete "$SMPROGRAMS\\Startup\\${APPNAME}.lnk"
  Delete "$INSTDIR\\Uninstall.exe"
  RMDir /r "$INSTDIR"
  DeleteRegKey HKCU "Software\\${COMPANY}\\${APPNAME}"
SectionEnd
