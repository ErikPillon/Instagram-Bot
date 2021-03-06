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
        self.driver.close()
    
    # get credentials    
    def import_user_and_password(self):
        if (os.path.isfile('Username-data/data.txt')):
            f = open('Username-data/data.txt', "r")
            self.username = f.readline()
            self.password = f.readline()
        else:
            f = open('Username-data/data.txt', "w")
            self.username = input("Please insert your username:")
            f.write(self.username +'\n')
            print("Please insert your password:")
            self.password = getpass.getpass()
            f.write(self.password)
            
    
    # login through the browser
    def login(self):
        driver = self.driver
        driver.get("http://www.instagram.com")
        time.sleep(1)
        element = driver.find_element_by_link_text("Log in")
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
        driver.find_element_by_xpath("//button[text()='Not Now']").click()    

    def collect_photo_to_like(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        for i in range(1,3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            # now I only collect the link for the images
        link_to_exploit = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in link_to_exploit]
        # pic_hrefs = [elem.find('https://www.instagram.com/p/') for elem in pic_hrefs]
        f = open('Username-data/to_like.txt', "a+")
        for href in pic_hrefs:
            if not href in f:
                f.write(href+'\n')
                # please note that not all the links are needed! 
                # All the pictures have the form of https://www.instagram.com/p/something

    def like_photo(self, link):
        print(link)
        if link.find('https://www.instagram.com/p/'):
            driver = self.driver
            print(link)
            driver.get(link)
            Heart= driver.find_element_by_css_selector('.coreSpriteHeartOpen')
            Heart.click() 
        else:
            return
    
    def sequential_like_photo(self, max = 200):
        to_wait = int(3600/max)
        links_file = 'Username-data/to_like.txt'
        if not (os.path.isfile(links_file)):
            print('No picture to like found!')
        else:
            f = open(links_file, 'r')
            for line in f:
                self.like_photo(line)
                time.sleep(to_wait)


def main():
    Phi_Erik = Insta_bot()
    Phi_Erik.import_user_and_password()
    Phi_Erik.login()
#    Phi_Erik.not_now()
    Phi_Erik.collect_photo_to_like('F1')
    Phi_Erik.sequential_like_photo()

if __name__ == "__main__":
    main()

# driver.find_element_by_css_selector(".button_main").click()
# element = driver.find_element_by_link_text("Log in");
# element.click()


