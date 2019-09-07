import os, time, random

from colorama import Fore, Back, Style
from core.dict import *

encodeTitle = """

  _____                     _         ___        _   _                 
 | ____|_ __   ___ ___   __| | ___   / _ \ _ __ | |_(_) ___  _ __  ___ 
 |  _| | '_ \ / __/ _ \ / _` |/ _ \ | | | | '_ \| __| |/ _ \| '_ \/ __|
 | |___| | | | (_| (_) | (_| |  __/ | |_| | |_) | |_| | (_) | | | \__ \
 |_____|_| |_|\___\___/ \__,_|\___|  \___/| .__/ \__|_|\___/|_| |_|___/
                                          |_|                          

"""

encodeOption = """

 [1] UTF-8
 [2] ASCII

"""

def encodeUTF8():
	inputO = input("Your message : ")
	print()

	slicedInput = list(inputO)

	for i in slicedInput:
	    value = valuesUTF8[i]

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
		encodeUTF8()