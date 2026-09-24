@echo off
rem Background-only launcher for the ccglass collector/proxy (ports 9911/9912).
rem Used by the "CodexTokenGlass" logon task so Codex keeps being captured
rem even when the desktop dashboard window is closed.
setlocal
set "ROOT=%~dp0"
set "DATADIR=%USERPROFILE%\.ccglass\codex-desktop"
if not exist "%DATADIR%" mkdir "%DATADIR%"
"%ROOT%runtime\node.exe" "%ROOT%ccglass\bin\ccglass.js" proxy --provider codex --upstream http://127.0.0.1:8787 --proxy-port 9911 --port 9912 --dir "%DATADIR%" --no-open
endlocal
