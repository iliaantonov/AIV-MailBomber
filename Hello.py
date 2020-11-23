import time as t
from colorama import Fore, init

init()


def Red_Text(text, i, tp):
    while i < len(text):
        print(Fore.RED + text[i], end='', flush=True)
        if tp == 'A':
            t.sleep(0.05)
        if tp == 'B':
            t.sleep(0.01)
        i = i + 1


def Yellow_Text(text, i, tp):
    while i < len(text):
        print(Fore.YELLOW + text[i], end='', flush=True)
        if tp == 'A':
            t.sleep(0.05)
        if tp == 'B':
            t.sleep(0.01)
        i = i + 1


def Green_Text(text, i, tp):
    while i < len(text):
        print(Fore.GREEN + text[i], end='', flush=True)
        if tp == 'A':
            t.sleep(0.05)
        if tp == 'B':
            t.sleep(0.01)
        i = i + 1


def Blue_Text(text, i, tp):
    while i < len(text):
        print(Fore.BLUE + text[i], end='', flush=True)
        if tp == 'A':
            t.sleep(0.05)
        if tp == 'B':
            t.sleep(0.01)
        i = i + 1
