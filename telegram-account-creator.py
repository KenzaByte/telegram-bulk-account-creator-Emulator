import configparser
import sys
import csv
import colorama
import subprocess, requests, time, os
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

bluec = Style.BRIGHT + Fore.BLUE
redc = Style.BRIGHT + Fore.RED
greenc = Style.BRIGHT + Fore.GREEN
yellowc = Style.BRIGHT + Fore.YELLOW
whitec = Style.BRIGHT + Fore.WHITE
magentac = Style.BRIGHT + Fore.MAGENTA
cyanc = Style.BRIGHT + Fore.CYAN


print("")
print(f"{magentac}[*] Telegram bulk account creator [PREMIUM VERSION]")
print()
print(f"{greenc}[*] www.KenzaByte.com")
print()
print(f"{cyanc}[*] Contact : https://www.kenzabyte.com/contact-us/")
print()
a=input("[*] Press any key to exit...")
