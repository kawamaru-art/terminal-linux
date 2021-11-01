import os
from time import sleep
os.system("cls")
files = open("user/share/jasp/username.txt",'r')
os.system("git clone https://github.com/Yeahboi12356/update && cp update/terminal.py home/" + files)
print("clik y to continue")
os.system("rd /s update")
print("restarting terminal..")
sleep(5)
os.system("py start-terminal.py")