from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time #essentially only for the sleep() feature
import os
import getpass
# the following is deprecated and not needed
# from selenium.webdriver.common.by import By 

if (os.path.isfile('Username-data/data2.txt')):
    f = open('Username-data/data.txt', "r")
    username = f.readline()
    password = f.readline()
else:
    username = input("Please insert your username:")
    print("Please insert your password:")
    password = getpass.getpass()

driver = webdriver.Firefox()
driver.implicitly_wait(1)

driver.get("http://www.instagram.com")

time.sleep(1)

element = driver.find_element_by_link_text("Log in");
element.click()

time.sleep(1)

to_insert_user = driver.find_element_by_name("username")
to_insert_user.send_keys(username)
to_insert_password = driver.find_element_by_name("password")
to_insert_password.send_keys(password)

time.sleep(1)

to_insert_password.send_keys(Keys.RETURN)

# driver.find_element_by_css_selector(".button_main").click()
# element = driver.find_element_by_link_text("Log in");
# element.click()


