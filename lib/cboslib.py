from lib import cboslib
import time
import requests
import colorama
import random
import ctypes
import sys
import os
import base64

def clear_console():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def randomcolor():
    color_choices = [
        colorama.Fore.RED,
        colorama.Fore.GREEN,
        colorama.Fore.YELLOW,
        colorama.Fore.BLUE,
        colorama.Fore.MAGENTA,
        colorama.Fore.CYAN,
        colorama.Fore.LIGHTBLUE_EX,
        colorama.Fore.LIGHTCYAN_EX,
        colorama.Fore.LIGHTGREEN_EX,
        colorama.Fore.LIGHTMAGENTA_EX,
        colorama.Fore.LIGHTRED_EX,
        colorama.Fore.LIGHTYELLOW_EX
    ]
    return random.choice(color_choices)

def randomstringcolor(string):
    return randomcolor() + string + colorama.Fore.RESET

def cprint(string):
    print(randomstringcolor(string))

def versioncheck(version):
    url = "https://thepuppet57.141412.xyz/tps/cbos/backend/versioncheck.php"
    
    response = requests.get(url)
    latestversion = float(response.text)

    if(latestversion > version):
        cprint("Update available!")
    elif(latestversion < version):
        cprint("This is a beta!")
    else:
        cprint("No updates available!")

def base64encode(string):
    encoded_bytes = base64.b64encode(string.encode("utf-8"))
    encoded_str = encoded_bytes.decode("utf-8")
    return encoded_str

def base64decode(encoded_str):
    decoded_bytes = base64.b64decode(encoded_str.encode("utf-8"))
    decoded_str = decoded_bytes.decode("utf-8")
    return decoded_str