@echo off
REM add texttest gui folder in path
set PATH=%PATH%;..\..\textTest
REM set TextTest executable
SET TEXTTESTPY=texttest.exe
REM specify <repository>/python/src as a python source
SET PYTHONPATH=..\src\
REM set python executable
SET PYTHON=python
REM init textest
start %TEXTTESTPY%

