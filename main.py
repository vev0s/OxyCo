import sys, time, random

from colorama import Fore, Back, Style
from core.encodeUTF8 import *
from core.decodeUTF8 import *
from core.headers import *
from lib.functions import *

mainOption = """

 [1] Encode
 [2] Decode
 
 [e] Exit script	[c] Clear screen    [h] Help Message

"""
encodeOption = """

 [1] UTF-8
 [2] ASCII

"""
decodeOption = """

 [1] UTF-8
 [2] ASCII

"""

checkVersion()

print(header1)
print(mainOption)

try:
	while True:
		choice = input("")

		if choice.lower() == 'c':
			clear()
			print(header1)
			print(mainOption)
		elif choice.lower() == "e" or choice.lower() == "exit":
			sys.exit(Fore.RED + "\nHave a good day ! :)")
			print(Style.RESET_ALL)
		elif choice.lower() == '1':
			encode()
			print(header1)
			print(mainOption)
		elif choice.lower() == '2':
			decode()
			print(header1)
			print(mainOption)

except KeyboardInterrupt:
    sys.exit(Fore.RED + "\nHave a good day ! :)")
    print(Style.RESET_ALL)
