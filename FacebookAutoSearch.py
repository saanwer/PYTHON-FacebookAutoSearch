import os, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pykeyboard import PyKeyboard
from clint.textui import colored
#Facebook People Search
#Coded by | WarLord
#https://github.com/saanwer
os.system('title Facebook Search')
os.system('cls')#'Clear' if in Linux Terminal
def Main():
    email = raw_input("Enter email : ")
    print
    password = raw_input("Enter password : ")
    print
    name = raw_input("Enter name to search : ")
    browser = webdriver.Firefox()
    browser.get("https://www.facebook.com/login.php")
    emailElement = browser.find_element_by_id("email")
    emailElement.send_keys(email)
    passElement = browser.find_element_by_id("pass")
    passElement.send_keys(password)
    passElement.submit()
    time.sleep(3)
    browser.get("https://www.facebook.com")
    nameElement = browser.find_element_by_name("q")
    nameElement.send_keys(name)
    keyboard = PyKeyboard()
    keyboard.press_key(keyboard.enter_key)#Keyboard press 'ENTER'

    os.system('cls')#os.system('clear') if Linux
    print colored.yellow("[+] Person search success!")
    browser.close()

if __name__ == "__main__":
    Main()
