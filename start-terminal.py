import os
from time import sleep
import signal
import sys
def main():
    files = open("user/share/jasp/username.txt",'r')
    y = input("continue or exit y/n: ")
    if y == "y":
        p = input("did you install git? y/n: ")
        if p == "y":
            print("starting terminal")
            sleep(3)
            os.system("python home/" + files.readline() + "/terminal.py")
        elif p == "n":
            print("install git in folder install-pankages")
    elif y == "n":
        sys.exit()

def signal_handler(signal, frame):
    print("\nyou clik ctrl + c if you want exit type exit\n")
    main()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()