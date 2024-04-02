@echo off
REM set TextTest executable
SET TEXTTESTPY=%~dp0..\utils\textTest\texttest.exe
REM specify <repository>\src\foodWebsAnalyzer as a python source
SET PYTHONPATH=%~dp0..\src
REM set python executable
SET PYTHON=%~dp0..\src\.venv\Scripts\python.exe
REM init textest
start %TEXTTESTPY%

