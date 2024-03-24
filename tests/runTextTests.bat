@echo off
REM set TextTest executable
SET TEXTTESTPY=texttest.exe
REM specify <repository>/src as a python source
SET PYTHONPATH=..\src\
REM set python executable
SET PYTHON=python
REM init textest
start %TEXTTESTPY%

