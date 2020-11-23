import smtplib as smtp
import time as t
import Hello as Txt
from validate_email import validate_email
from colorama import Fore, init
import random as rand

# Для Colorama
init()

# Данные майла
email = ''
password = ''
login_str = ''
dest_email = ''

sent = open('sentences', 'r')

i = 0
i1 = 0
spam_type = 'single'
enter = False
random = False
log_pass = False

login_arr = []
sent_arr = []

email_arr = ['', '', '', '', '']
password_arr = ['', '', '', '', '']

for line in sent:
    sent_arr.append(line)

# Логотип
Txt.Red_Text('Mail-Bomber v2.0 by ', 0, 'A')
Txt.Green_Text('AIV', 0, 'A')
print()
Txt.Yellow_Text('All data must be entered in ', 0, 'A')
Txt.Green_Text('English!', 0, 'A')
print()

# Настройка майла пользователя

Txt.Blue_Text('E-mail Service - mail.ru', 0, 'B')
print(end='\n\n')

# Тип подключения

Txt.Blue_Text('Connection type (single - s, multiple(2-5) - m): ', 0, 'B')
spam_type = input()

while spam_type != 'single' and spam_type != 'multiple':
    if spam_type == 's':
        spam_type = 'single'
    if spam_type == 'm':
        spam_type = 'multiple'
    if spam_type != 'single' and spam_type != 'multiple':
        Txt.Red_Text('Wrong symbol!', 0, 'B')
        print()
        Txt.Yellow_Text('Try again (s/m): ', 0, 'B')
        spam_type = input()

# Режим одного майла

server = smtp.SMTP_SSL('smtp.mail.ru', 465)

mailCheck = False

if spam_type == 'single':
    while not mailCheck:
        Txt.Yellow_Text('Login:Password : ', 0, 'B')
        login_str = input()
        for i in login_str:
            if not log_pass and i != ':':
                email = email + i
            if log_pass:
                password = password + i
            if not log_pass and i == ':':
                log_pass = True

        try:
            server.ehlo()
            server.login(email, password)
            Txt.Green_Text('Successful Login: ', 0, 'B')
            Txt.Green_Text(email, 0, 'B')
            mailCheck = True
            print(end='\n')

        except OSError:
            Txt.Red_Text('Error: Failed to connect, try again!', 0, 'B')
            print(end='\n')

# Режим мульти майла

i = 0

if spam_type == 'multiple':
    while i < 5:
        Txt.Yellow_Text('Login:Password ', 0, 'B')
        print('(', i+1, '): ', end='', sep='')
        login_arr.append(input())
        i += 1

# Настройка списка аккаунтов

i = 0
i1 = 0
log_pass = False

if spam_type == 'multiple':

    while i < 5:

        if (login_arr[i]) != '':
            while i1 < len(login_arr[i]):

                if not log_pass and ((login_arr[i])[i1]) != ':':
                    email_arr[i] = email_arr[i] + ((login_arr[i])[i1])

                if log_pass and ((login_arr[i])[i1]) != ':':
                    password_arr[i] = password_arr[i] + ((login_arr[i])[i1])

                if ((login_arr[i])[i1]) == ':':
                    log_pass = True

                i1 += 1

        i += 1
        i1 = 0
        log_pass = False

# Сортировка списка аккаунтов
i = 0

if spam_type == 'multiple':
    while i < len(email_arr):
        if email_arr[i] == '':
            password_arr[i] = ''
            email_arr.remove('')
            password_arr.remove('')
            i -= 1
        if password_arr[i] == '':
            email_arr[i] = ''
            email_arr.remove('')
            password_arr.remove('')
            i -= 1
        i += 1

# Подключение к серверу
server = smtp.SMTP_SSL('smtp.mail.ru', 465)

# Проверка мульти-майлов

i = 0

print()

while i < len(email_arr):
    if spam_type == 'multiple':
        try:
            server.ehlo()
            server.login(email_arr[i], password_arr[i])
            Txt.Green_Text('Successful Login: ', 0, 'B')
            Txt.Green_Text(email_arr[i], 0, 'B')
            print()

        except OSError:
            Txt.Red_Text('Login Error: ', 0, 'B')
            Txt.Red_Text(email_arr[i], 0, 'B')
            email_arr[i] = ''
            password_arr[i] = ''
            email_arr.remove('')
            password_arr.remove('')
            i -= 1
            print()
    i += 1

if len(email_arr) == 1:
    spam_type = 'single'
    email = email_arr[0]
    password = password_arr[0]

if len(email_arr) == 0:
    Txt.Red_Text('Error: Number of working accounts = 0. The program is stopped.', 0, 'B')
    exit()

# Сбор данных

print()

mailCheck = False

while not mailCheck:
    Txt.Blue_Text('E-mail address for the attack: ', 0, 'B')
    dest_email = input()
    if validate_email(dest_email):
        mailCheck = True
        print(Fore.GREEN + dest_email, ' - is valid!')
        print()
    if not validate_email(dest_email):
        Txt.Red_Text('Error: Invalid Email. Try again', 0, 'B')
        print()

Txt.Yellow_Text('Text (max 100) | (rand_msg - random messages): ', 0, 'B')
email_text = input()
if email_text == 'rand_msg':
    random = True
    Txt.Green_Text('Random-Mode: On', 0, 'B')
    print(end='\n\n')

if spam_type == 'single':
    message = 'From: {}\nTo: {}\n\n{}'.format(email, dest_email, email_text)

while len(email_text) == 0 or len(email_text) > 100:
    Txt.Red_Text('Try again: max 100 or rand_msg: ', 0, 'B')
    email_text = input()

Txt.Yellow_Text('Amount (1-100): ', 0, 'B')
amount = input()

while int(amount) == 0 or int(amount) > 100:
    Txt.Red_Text('Try again (1-100): ', 0, 'B')
    amount = input()

# Подключение к майлу
print()
print(Fore.RED + 'Loading..')

# Отправка сообщений
i = 0
if spam_type == 'single':

    server = smtp.SMTP_SSL('smtp.mail.ru', 465)
    server.ehlo()
    server.login(email, password)

    while i < int(amount):
        if random:
            email_text = sent_arr[rand.randint(0, len(sent_arr) - 1)]
            message = 'From: {}\nTo: {}\n\n{}'.format(email, dest_email, email_text)

        try:
            if not random:
                message = 'From: {}\nTo: {}\n\n{}'.format(email, dest_email, email_text)

            server.sendmail(email, dest_email, message)
            print(Fore.GREEN + '[+] Successfully sent to the: ', Fore.RED + dest_email)
            i = i + 1
            print(Fore.YELLOW + '[!] Mails left: ', int(amount) - i)
        except OSError:
            print(Fore.RED + '[-] Error! Failed to send email. Stopping the program..', 0, 'B')
            exit()

        if i < int(amount):
            t.sleep(3)
    server.quit()

if spam_type == 'multiple':
    i1 = 0
    i = 0
    while i1 < int(amount) and i < len(email_arr):
        if random:
            email_text = sent_arr[rand.randint(0, len(sent_arr) - 1)]
            message = 'From: {}\nTo: {}\n\n{}'.format(email_arr[i], dest_email, email_text)

        server = smtp.SMTP_SSL('smtp.mail.ru', 465)
        server.ehlo()
        try:
            server.login(email_arr[i], password_arr[i])
        except OSError:
            print(Fore.RED + '[-] Error! Failed to log in: ', Fore.RED + email_arr[i])
            i = i + 1
            continue

        try:
            if not random:
                message = 'From: {}\nTo: {}\n\n{}'.format(email_arr[i], dest_email, email_text)
            server.sendmail(email_arr[i], dest_email, message)
            print(Fore.GREEN + '[+] Successfully sent from: ', Fore.BLUE + email_arr[i])
            i1 += 1
            i += 1
            print(Fore.YELLOW + '[!] Mails left: ', int(amount) - i1)
        except OSError:
            print(Fore.RED + '[-] Error! Failed to send email from: ', Fore.RED + email_arr[i])
            print(Fore.YELLOW + '[!] Mails left: ', int(amount) - i1)
            i += 1
        if i1 == int(amount):
            break
        if i == len(email_arr):
            i = 0
        server.quit()

        t.sleep(3)

Txt.Green_Text('All mails were sent. The program is turned off!', 0, 'B')
