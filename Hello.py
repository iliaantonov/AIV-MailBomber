import time as t
from colorama import Fore, init


def Red_Text(Text, i):
    while i < len(Text):
        print(Fore.RED + Text[i], end='', flush=True)
        t.sleep(0.05)
        i = i + 1


def Yellow_Text(Text, i):
    while i < len(Text):
        print(Fore.YELLOW + Text[i], end='', flush=True)
        t.sleep(0.05)
        i = i + 1


def Green_Text(Text, i):
    while i < len(Text):
        print(Fore.GREEN + Text[i], end='', flush=True)
        t.sleep(0.05)
        i = i + 1


def Blue_Text(Text, i):
    while i < len(Text):
        print(Fore.YELLOW + Text[i], end='', flush=True)
        t.sleep(0.05)
        i = i + 1