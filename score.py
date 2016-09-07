#!/usr/bin/python
from colorama import *
import os
import subprocess


global score
score = 0

def info(string):
    print Fore.WHITE + str(string) + Fore.RESET
def easy(string):
    print Fore.GREEN + str(string) + Fore.RESET
def med(string):
    print Fore.YELLOW + str(string) + Fore.RESET
def hard(string):
    print Fore.RED + str(string) + Fore.RESET
def cmd(string):
    proc = subprocess.Popen([str(string)], stdout=subprocess.PIPE, shell=True)
    return proc.stdout.read()[:-1]
def v0():
    global score
    if(cmd("cat /etc/shadow | grep archer | wc -l") == str(1)):
	score +=1
	easy("Congratulations! You have successfully added the user archer.")
    else:
	info("Please add the user archer.")
def v1():
    global score
    if(cmd("cat /etc/shadow | grep sadie | wc -l") == str(0)):
	score +=1
	easy("Congratulations! You have successfully removed the user sadie.")
    else:
	info("Please remove the user sadie.")
def v2():
    global score
    if(cmd("getent shadow meriel | cut -d: -f2") != ''):
	score +=1
	easy("Congratulations! You have added a password for meriel.")
    else:
	info("Please add a password to meriel.")
def v3():
    global score
    if(cmd("cat /var/log/auth.log | grep \"apt-get update\" | grep -v grep | wc -l") != str(0)):
	score +=1
	easy("Congratulations! You have updated the system.")
    else:
	info("Please update the system.")
	score +=1
def v4():
    global score
    if(cmd("cat /etc/group | grep sudo | grep meriel | wc -l") != str(1)):
	score +=1
	easy("Congratulations! You have removed meriel from sudoers.")
    else:
	info("Please remove meriel from sudoers.")
def v5():
    global score
    if(cmd("cat /etc/login.defs | grep PASS_MAX_DAYS | grep 90 | wc -l") == str(1)):
	score +=1
	med("Congratulations! You have changed the maximum password age to 90.")
    else:
	info("Please change the maximum password age to 90.")
def v6():
    global score
    if(cmd("cat /etc/lightdm/users.conf | grep \'allow-guest=false\' | wc -l") == str(1)):
	score +=1
	med("Congratulations! You have disabled the guest account.")
    else:
	info("Please disable the guest account.")
def v7():
    global score
    if(cmd("dpkg --list | grep nmap | wc -l") == str(0)):
	score +=1
	med("Congratulations! You have removed nmap.")
    else:
	info("Please remove nmap from your system.")
def v8():
    global score
    if(raw_input("What does FTP stand for?").lower() == "File Transfer Protocol".lower()):
	score +=1
	med("Congratulations! You got the question right.")
    else:
	info("You got the question wrong ;(")
def v9():
    global score
    if(raw_input("What is Ubuntu 14.04's codename?").lower() == "Trusty Tahr".lower()):
	score +=1
	med("Congratulations! You got the question right.")
    else:
	info("You got the question wrong ;(")
def v10():
    global score
    if(raw_input("What language does the shellshock vulnerability affect?").lower() == "Bash".lower()):
	score +=1
	med("Congratulations! You got the question right.")
    else:
	info("You got the question wrong ;(")
def v11():
    global score
    if((int(cmd("cat /var/spool/cron/crontabs/george | grep bash | wc -l ")) != 1)):
	score +=1
	med("Congratulations! You removed the backdoor in George's crontab.")
    else:
	info("Please remove the backdoor in George's crontab.")
def v12():
    global score
    if((int(cmd("cat /var/spool/cron/crontabs/root | grep bash | wc -l ")) != 1)):
	score +=1
	med("Congratulations! You removed the backdoor in root's crontab.")
    else:
	info("Please remove the backdoor in root's crontab.")
def v13():
    global score
    if(cmd("cat /etc/rc.local | grep nc | grep -v \# | wc -l") == str(0)):
	score +=1
	med("Congratulations! You have successfully removed the backdoor from startup.")
    else:
	info("A backdoor is being run on startup. Please remove it.")
def v14():
    global score
    if(raw_input("What is the file run whenever someone opens a shell?").lower() == ".bashrc".lower()):
	score +=1
	med("Congratulations! You got the question right.")
    else:
	info("You got the question wrong ;(")
def v15():
    global score
    if(raw_input("How many times did root fail to connect over ssh?") == str(2)):
	score +=1
	med("Congratulations! You got the question right.")
    else:
	info("You got the question wrong ;(")
def v16():
    global score
    if(raw_input("What port did ssh accept a connection from when it accepted a password for george on March 3rd at 21:51:42?") == str(44625)):
	score +=1
	hard("Congratulations!! You got the question right.")
    else:
	info("You got the question wrong.")
def v17():
    global score
    if(raw_input("A password was found on this system. We know the encryption used was md5, but we don't know what the password is. Can you find it? The password is d107d09f5bbe40cade3de5c71e9e9b7").lower() == "letmein".lower()):
	score +=1
	med("Congratulations! You got the question right.")
    else:
	info("You got the question wrong ;(")

score = int(cmd("cat /bin/loc.txt"))
info("Old score: " + str(score))

print ""

if(score == 0):
    v0()

if(score == 1):
    v1()

if(score == 2):
    v2()

if(score == 3):
    v3()

if(score == 4):
    v4()

if(score == 5):
    v5()

if(score == 6):
    v6()

if(score == 7):
    v7()

if(score == 8):
    v8()

if(score == 9):
    v9()

if(score == 10):
    v10()

if(score == 11):
    v11()

if(score == 12):
    v12()

if(score == 13):
    v13()

if(score == 14):
    v14()

if(score == 15):
    v15()

if(score == 16):
    v16()

if(score == 17):
    v17()

if(score == 18):
    hard("You got every vulnerability!! Congratulations!!!!")

print ""

os.system("echo " + str(score) + " > /bin/loc.txt")

info("New score: " + str(score))
