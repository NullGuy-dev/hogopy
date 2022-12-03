import os
import sys
def foundMainFile():
    allFiles = os.listdir()
    for obj in allFiles:
        if (obj == "main.py"):
            return True
    return False
while True:
    if foundMainFile():
        os.system("del delete.py")
        break
sys.exit()