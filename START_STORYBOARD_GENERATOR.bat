@echo off
title INVOICE Storyboard Prompt Generator
cd /d "%~dp0"
echo ================================================================
echo INVOICE Storyboard Prompt Generator
echo Ollama-only local version
echo Opens: http://127.0.0.1:8777
echo ================================================================
set "INVOICE_AI_PORT=8777"
if not exist ".env" (
  copy ".env.example" ".env" >nul
  echo A new .env file was created. Check the Ollama model name if needed.
  notepad ".env"
  pause
  exit /b
)
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 invoice_ai_server.py
) else (
  set "BUNDLED_PY=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
  if exist "%BUNDLED_PY%" (
    "%BUNDLED_PY%" invoice_ai_server.py
  ) else (
    python invoice_ai_server.py
  )
)
if errorlevel 1 pause
