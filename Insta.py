from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time #essentially only for the sleep() feature
import os # navigating through the paths
import getpass # asking password without echoing to the shell

class Insta_bot:
    def __init__(self):
        username = None
        password = None
        self.driver = webdriver.Firefox()
    
    # emergency stop
    def shutDown(self): 
        self.drive.close()
    
    # get credentials    
    def import_user_and_password(self):
        if (os.path.isfile('Username-data/data.txt')):
            f = open('Username-data/data.txt', "r")
            self.username = f.readline()
            self.password = f.readline()
        else:
            self.username = input("Please insert your username:")
            print("Please insert your password:")
            self.password = getpass.getpass()
    
    # login through the browser
    def login(self):
        driver = self.driver
        driver.get("http://www.instagram.com")
        time.sleep(1)
        element = driver.find_element_by_link_text("Log in");
        element.click()
        time.sleep(1)
        to_insert_user = driver.find_element_by_name("username")
        to_insert_user.send_keys(self.username)
        to_insert_password = driver.find_element_by_name("password")
        to_insert_password.send_keys(self.password)
        time.sleep(1)
        to_insert_password.send_keys(Keys.RETURN)
        time.sleep(2)
        
    def not_now(self):
        driver = self.driver
#        driver.find_element_by_css_selector("aOOlW HoLwm ").click()
        driver.find_element_by_xpath("//button[text()='Not Now']").click();    

    def like_photo(self, hashtag):
        driver = self.driver
        Search_bar = driver.find_element_by_xpath("//input[@placeholder='Search']");
        #Search_bar.send_keys(hashtag)
        #time.sleep(1)
        #Search_bar.send_keys(Keys.RETURN)
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        
        time.sleep(3)
        for i in range(1,3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

def main():
    Phi_Erik = Insta_bot()
    Phi_Erik.import_user_and_password()
    Phi_Erik.login()
    Phi_Erik.not_now()
    Phi_Erik.like_photo('F1')
    
if __name__ == "__main__":
    main()

# driver.find_element_by_css_selector(".button_main").click()
# element = driver.find_element_by_link_text("Log in");
# element.click()


