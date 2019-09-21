import os, sys

def clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

def checkVersion():
	version = sys.version[:1]
	if int(version) == 3:
		pass
	else:
		sys.exit(warning+" Veuillez lancer la version 3 de python.")
		