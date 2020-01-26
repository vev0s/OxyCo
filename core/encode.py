import os, time, random

from colorama import Fore, Back, Style
from core.dict import *

encodeTitle = """
    ______                     __        ____        __  _                 
   / ____/___  _________  ____/ /__     / __ \\____  / /_(_)___  ____  _____
  / __/ / __ \\/ ___/ __ \\/ __  / _ \\   / / / / __ \\/ __/ / __ \\/ __ \\/ ___/
 / /___/ / / / /__/ /_/ / /_/ /  __/  / /_/ / /_/ / /_/ / /_/ / / / (__  ) 
/_____/_/ /_/\\___/\\____/\\____/\\___/   \\____/ .___/\\__/_/\\____/_/ /_/____/  
                                          /_/                              
"""

encodeOption = """

 [1] Personnal static encode
 [2] Cesar encode

"""

def encodeUTF8():
	inputO = input("Type your message : ")
	print()

	slicedInput = list(inputO)

	for i in slicedInput:
	    value = valuesUTF8[i]

	    print(Fore.BLUE + value, end="")
	print("\n")
	print(Fore.RED + 'Conversion finished !')
	print(Style.RESET_ALL)

def encodeCesar():
	inputC = input("Entrer votre message : ")

	slicedCesarInput = list(inputC)

	for i in slicedCesarInput:
		    value = valuesCesar[i]

		    print(Fore.BLUE + value, end="")
	print("\n")
	print(Fore.RED + 'Conversion finished !')
	print(Style.RESET_ALL)


def encode():
	print(encodeTitle)
	print(encodeOption)
	choiceO = input("")
	if choiceO.lower() == '1':
		encodeUTF8()
	elif choiceO.lower() == '2':
		encodeCesar()