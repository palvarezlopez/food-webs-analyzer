REM specify <repository>/python/src as a python source
SET PYTHONPATH=..\src\

:mypyCommand
python -m mypy ..\src\foodwebDynamics.py --disallow-untyped-defs --extra-checks
pause
cls
goto mypyCommand