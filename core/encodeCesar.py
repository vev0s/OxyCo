import os, time, random

from colorama import Fore, Back, Style
from core.dictCesar import *

inputE = input("Entrer votre message : ")

slicedInput = list(inputE)

for i in slicedInput:
	    value = valuesUTF8[i]

	    print(Fore.BLUE + value, end="")
print("\n")
print(Fore.RED + 'Conversion finished !')
print(Style.RESET_ALL)