@echo off

set /p NAME= What's your user name?: 
cls
del home\terminal.py
del home\%NAME%\terminal.py
copy update/delnis.py delnis.py
copy "update/terminal.py" home\%NAME%
py delnis.py
