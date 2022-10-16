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
    def test_Loginpage(self,multi_data):
        #web = webdriver.ChromeOptions()
        #self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        for iter in range(1,4):
            #Login page

            #username
            time.sleep(4)
            self.driver.find_element(by=By.XPATH, value="//*[@name = 'username']").send_keys(multi_data["username"])
            #password
            self.driver.find_element(by=By.XPATH, value="//*[@name = 'password']").send_keys(multi_data["password"])
            #login button
            self.driver.find_element(by=By.XPATH, value="//*[contains(@class,'oxd-button')]").click()
            time.sleep(4)
            #WebDriverWait(self.driver,60).until(ec.presence_of_element_located((By.XPATH,'//*[@id="nameofuser"]')))
            message = self.driver.find_element(by=By.XPATH, value="(//*[text()='PIM'])[2]").text
            assert message == "PIM"
            #logout
            #time.sleep(2)
            #Logoutdropdown
            self.driver.find_element(by=By.XPATH, value="//*[text()='Paul Collings']").click()
            #Logoutbutton
            WebDriverWait(self.driver,60).until(ec.element_to_be_clickable((By.XPATH,"//*[text()='Logout']")))
            self.driver.find_element(by=By.XPATH, value="//*[text()='Logout']").click()





















