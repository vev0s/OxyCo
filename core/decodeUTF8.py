import os, time, random

from colorama import Fore, Back, Style
from core.dictReverse import *

decodeTitle = """
    ____                      __        ____        __  _                 
   / __ \\___  _________  ____/ /__     / __ \\____  / /_(_)___  ____  _____
  / / / / _ \\/ ___/ __ \\/ __  / _ \\   / / / / __ \\/ __/ / __ \\/ __ \\/ ___/
 / /_/ /  __/ /__/ /_/ / /_/ /  __/  / /_/ / /_/ / /_/ / /_/ / / / (__  ) 
/_____/\\___/\\___/\\____/\\__,_/\\___/   \\____/ .___/\\__/_/\\____/_/ /_/____/  
                                         /_/                              
"""

decodeOption = """

 [1] UTF-8
 [2] ASCII

"""


def decodeUTF8():‡
	inputO = input("Type your message : ")
	print()

	slicedInput = [inputO[i:i+2] for i in range(0, len(inputO), 2)]

	for i in slicedInput:
	    value = valuesReverseUTF8[i]

	    print(Fore.BLUE + value, end="")
	print("\n")
	print(Fore.RED + 'Conversion finished !')
	print(Style.RESET_ALL)


def decode():
	print(decodeTitle)
	print(decodeOption)
	choiceT = input("")
	if choiceT.lower() == '1':
		decodeUTF8()
	elif choiceT.lower() == '2':
		decodeUTF8()