import os

files = open("user/share/jasp/username.txt",'r')
os.system("cd home && copy terminal.py " + files.readline())
print("start terminal with command 'python start-terminal.py' ")