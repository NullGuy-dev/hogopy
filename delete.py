import os
import sys
def foundMainFile():
    allFiles = os.listdir()
    for obj in allFiles:
        #If you compiled this code in EXE, remove the line below, and insert: if (obj == "your_main_file(exe)_name.exe"):")
        if (obj == "main.py"):
            return True
    return False
while True:
    if foundMainFile():
        #If you compiled this code in EXE, remove the line below, and insert: os.system("del your_main_file(exe)_name.exe")
        os.system("del main.py")
        break
sys.exit()
