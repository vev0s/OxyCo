import os, time, random

from colorama import Fore, Back, Style
from core.dictReverse import *

decodeTitle = """

  ____                     _         ___        _   _                 
 |  _ \  ___  ___ ___   __| | ___   / _ \ _ __ | |_(_) ___  _ __  ___ 
 | | | |/ _ \/ __/ _ \ / _` |/ _ \ | | | | '_ \| __| |/ _ \| '_ \/ __|
 | |_| |  __/ (_| (_) | (_| |  __/ | |_| | |_) | |_| | (_) | | | \__ \
 |____/ \___|\___\___/ \__,_|\___|  \___/| .__/ \__|_|\___/|_| |_|___/
                                         |_|                          

"""

decodeOption = """

 [1] UTF-8
 [2] ASCII

"""


def decodeUTF8():
	inputO = input("You message : ")
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