import os

os.system("cls")
print("welcome to terminal like linux")
print("make your new account for this terminal")
print("usernames without number")
p = input("new username: ")
h = input("hostname custm is recomended default/custom: ")
i = input("password: ")

if h == "custom":
    yeah = input("hostname: ")
elif h == "default":
    print("hostname default")
else:
    print("sorry we got error in hostname make sure you make again account")

os.system("cd home && mkdir " + p )
files = open("user/share/jasp/username.txt",'w')
files.write(p)
filess = open("user/share/jasp/password.txt",'w')
filess.write(i)
filesss = open("user/share/jasp/hostname-custom.txt",'w')
filesss.write(yeah)
filessss = open("user/share/jasp/hostname.txt",'w')
filessss.write("nise")
print("you need install git and dont forget to choose windows terminal")
print("used chrome")
u = input ("64bit/32bit/NO: ")
if u == "64bit":
    os.system("start chrome https://github.com/git-for-windows/git/releases/download/v2.33.1.windows.1/Git-2.33.1-64-bit.exe")
    print("type this to finish all installation'python cleaning.py'")
elif u == "32bit":
    os.system("start chrome https://github.com/git-for-windows/git/releases/download/v2.33.1.windows.1/Git-2.33.1-32-bit.exe")
    print("type this to finish all installation'python cleaning.py'")
elif u == "NO":
   print("type this to finish all installation'python cleaning.py'")
elif u == "no":
    print("type this to finish all installation'python cleaning.py'")