"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class test():
    def day2(self,web = None):

        self.driver.get("https://www.facebook.com")
        username = self.driver.find_element(by = By.ID ,value = "email") #Webelement
        username.send_keys("satheeshhkumarr@gmail.com")
        #username.clear()

        #time.sleep(3)
        #self.driver.maximize_window()
        #time.sleep(3)
        #self.driver.minimize_window()
        time.sleep(2)
        self.driver.close()

obj = test()
obj.day2()


"""
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class facebook():
    def login(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options = web)
        self.driver.get("http://www.facebook.com")
        #time.sleep(5)
        username = self.driver.find_element(by = By.ID,value="email")# Web element identification
        time.sleep(5)
        username.send_keys("Satheeshhkumarr@gmail.com")
        time.sleep(5)
        password = self.driver.find_element(by=By.ID, value="pass")  # Web element identification
        time.sleep(5)
        password.send_keys("1234")
        time.sleep(5)
        loginbutton = self.driver.find_element(by = By.NAME,value="login")#Web element identification
        #time.sleep(5)
        #loginbutton = self.driver.find_element(by=By.CLASS_NAME, value="_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy")  # Web element identification
        # time.sleep(5)
        loginbutton.click()
        time.sleep(10)
        #self.driver.maximize_window()
        #time.sleep(5)
        #self.driver.minimize_window()
        #time.sleep(5)

        self.driver.quit()


obj = facebook()
obj.login()






















