import os
from time import sleep
print("camera-security,version,default\n")
n = input("are you sure to upgrade pankages? y/n: ")
if n == "y":
  os.system("""git clone https://github.com/Yeahboi12356/update""") 
  os.system("update.bat")
elif n == "n":
  print("restarting terminal")
  os.system("start-terminal.exe")
else:
    print("number not valid")
    os.system("py nisupgrade.py")
