#encoding: UTF-8

# Version 1.0.0 - CP3 Automatic Quantic's Telecom Captive Portal login for command-line only interfaces
# Nothing is stored on this computer after logging
# Developped by 4idenP - © 2021

import requests
import argparse
import time
import os
import ping3
from selenium import webdriver

# DON'T FORGET TO FILL PhantomJS_path WITH THE PATH TO THE phantomjs EXECUTABLE!
PhantomJS_path = ""

parser = argparse.ArgumentParser(description='Captive Portal login automation for Quantic Telecom')
parser.add_argument('-l', metavar='email', dest='email',help='provide email', required=True)
parser.add_argument('-p', metavar='password', dest='passwd',help='provide password', required=True)

args = parser.parse_args()

emailArg = format(args.email)
passwordArg = format(args.passwd)

url = "https://www.quantic-telecom.net/connexion-reseau"

os_name = os.name
if os_name == 'nt':
    clear=lambda:os.system('cls')
else: clear=lambda:os.system('clear')

computer_name = os.environ['COMPUTERNAME']
user_name = os.environ['USERNAME']

clear()
print('\n[CP3] Operating system : '+os_name+' - Clearing terminal...\n')
print("\n \033[1;31m██████╗\033[0;32m██████╗ \033[1;34m██████╗\n\033[1;31m██╔════╝\033[0;32m██╔══██╗\033[1;34m╚════██╗\n\033[1;31m██║     \033[0;32m██████╔╝ \033[1;34m█████╔╝       \033[0;0mAutomatic Quantic Telecom's Captive Portal login\033[1;34m\n\033[1;31m██║     \033[0;32m██╔═══╝  \033[1;34m╚═══██╗\n\033[1;31m╚██████╗\033[0;32m██║     \033[1;34m██████╔╝\n\033[1;31m ╚═════╝\033[0;32m╚═╝     \033[1;34m╚═════╝\n")

try:
    result = requests.get(url, 'html.parser', allow_redirects=True)
    time.sleep(0.5)
except Exception:
    print('\n\033[0;0m[\033[1;31m-\033[0;0m]\033[0;31m Connexion réseau impossible: Unable to access captive portal, network seems down.\n     Exiting program.\n\033[0;0m')
    exit()

code = str(requests.get(url)).split('[')[1].split(']')[0]
error_code = str(result.content)
error_code01 = "Connexion r\\xc3\\xa9seau impossible"

if str(ping3.ping('8.8.8.8')) != 'None' and str(ping3.ping('8.8.8.8')) != 'False':
    print('\033[0;0m[\033[1;31m-\033[0;0m]\033[0;31m Unable to connect to Captive Portal:\033[1;31m You are already connected to internet!\033[0;0m\n')
    exit()

if code != '200': 
    print('\033[0;0m[\033[1;31m-\033[0;0m]\033[0;31m ERROR! Status code : %s - "%s"\033[0;0m\n' % (code, url))
    exit()
elif error_code01 in str(result.content):
        print('\033[0;0m[\033[1;31m-\033[0;0m]\033[0;31m Connexion réseau impossible: You are not connected to Quantic Telecom\'s network.\n     Exiting program.\n\033[0;0m')
        exit()
else: 
    print(f'\033[0;0m[\033[1;32m+\033[0;0m] Connection established! (%s) - Status : %s\n\033[1;30m' % (url, code))
    time.sleep(0.2)

def tryConnection(email, password):
    driver = webdriver.PhantomJS(PhantomJS_path)
    driver.get(url)

    try:
        driver.execute_script("document.getElementById('email').value=\'"+email+"\'")
        print('\n\033[0;0m[\033[1;32m+\033[0;0m] Successfully injected email...')
    except Exception:
        print('\n\033[0;0m[\033[1;31m-\033[0;0m]\033[0;31m Email injection failed: This may be due to an invalid character.\n     Exiting program.\033[0;0m\n')
        exit()


    try:
        driver.execute_script("document.getElementById('password').value=\'"+password+"\'")
        print('\033[0;0m[\033[1;32m+\033[0;0m] Successfully injected password...')
    except Exception:
        print('\033[0;0m[\033[1;31m-\033[0;0m]\033[0;31m Password injection failed: This may be due to an invalid character.\n     Exiting program.\033[0;0m\n')
        exit()


    try:
        driver.execute_script("document.getElementById('form-continue').click()")
        print('\033[0;0m[\033[1;32m+\033[0;0m] Successfully submitted credentials...')
    except Exception:
        print('\033[0;0m[\033[1;31m-\033[0;0m]\033[0;31m Submission failed: This may be due to an invalid element name in the js query.\n     Exiting program.\033[0;0m\n')
        exit()

    print('[\033[1;33m*\033[0;0m] Waiting for portal to accept connection...\n')
    for i in range(30):
        p = ping3.ping('8.8.8.8')
        if str(p) == 'None' or str(p) == 'False':
            time.sleep(1)
        else:
            print('\033[1;32m[CP3] Successfully connected! Enjoy surfing!\033[0;0m\n')
            driver.quit()
            exit()
    print('\n\033[0;0m[\033[1;31m-\033[0;0m]\033[0;31m Failed to connect: Unknown error.\n     Exiting program.\033[0;0m\n')
    driver.quit()
    exit()

def main():
    tryConnection(emailArg, passwordArg)

if __name__ == '__main__':
    main()