import time

import pytest
from selenium import  webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



@pytest.mark.usefixtures("open_launch_exit")
class Test_login():
    def test_action(self,user_name):
        #web = webdriver.ChromeOptions()
        #self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        #Login page
        self.driver.find_element(by = By.XPATH,value='//*[@id="login2"]').click()
        time.sleep(3)
        #username
        self.driver.find_element(by=By.XPATH, value='//*[@id="loginusername"]').send_keys(user_name[0])
        #password
        self.driver.find_element(by=By.XPATH, value='//*[@id="loginpassword"]').send_keys(user_name[1])
        #login button
        self.driver.find_element(by=By.XPATH, value='(//*[text()="Log in"])[2]').click()
        time.sleep(2)
        message = self.driver.find_element(by=By.XPATH, value='//*[@id="nameofuser"]').text
        assert message == "Welcome 123"
        #logout
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//*[@id="logout2"]').click()

















