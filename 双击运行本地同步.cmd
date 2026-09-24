@echo off
setlocal
cd /d "%~dp0"
chcp 65001 >nul

echo [INFO] Launching local official documentation synchronizer...
powershell -NoProfile -ExecutionPolicy Bypass -File "tools\Sync-OasisDocs.ps1"
set "EXIT_CODE=%ERRORLEVEL%"

if "%EXIT_CODE%"=="0" (
    echo [DONE] Sync completed successfully.
) else (
    echo [FAIL] Sync failed with exit code: %EXIT_CODE%
)

echo Press any key to exit...
pause >nul
exit /b %EXIT_CODE%
