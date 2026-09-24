@echo off
setlocal

set "ROOT=%~dp0"
cd /d "%ROOT%"

where node >nul 2>nul
if errorlevel 1 goto node_not_found

echo [INFO] Syncing Oasis community...
node "oasis-community-mcp-skill\scripts\sync-community.mjs" --project-root "%ROOT%." --pages all --per-page 50
set "EXIT_CODE=%ERRORLEVEL%"
echo.

if "%EXIT_CODE%"=="0" goto sync_success

echo [FAILED] Sync failed. Exit code: %EXIT_CODE%.
goto script_end

:node_not_found
echo [ERROR] Node.js was not found in PATH.
echo Please install Node.js or run this script from a terminal where node is available.
set "EXIT_CODE=1"
goto script_end

:sync_success
echo [DONE] Sync completed.

:script_end
if /i not "%~1"=="--no-pause" (
  echo Press any key to continue...
  pause >nul
)
exit /b %EXIT_CODE%
