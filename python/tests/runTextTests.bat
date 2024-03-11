@echo off
REM add texttest gui folder in path
set PATH=%PATH%;%~dp0..\..\textTest
REM set TextTest enviroment variable
SET TEXTTEST_HOME=%~dp0
REM set TextTest executable
SET TEXTTESTPY=texttest.exe
REM specify <repository>/python/src as a python source
SET PYTHONPATH=%~dp0..\src\
REM set python executable
SET PYTHON=python
REM init textest
start %TEXTTESTPY%

