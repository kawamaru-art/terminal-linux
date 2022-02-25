@echo off

set /p NAME= What's your user name?: 
cls
del home\%NAME%\terminal.py
copy "update\terminal.py" home\%NAME%
python uipdate.py
