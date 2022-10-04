import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

class lis():
    def frameconce(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/frame.xhtml")
        self.driver.maximize_window()
        groups = self.driver.find_elements(by = By.TAG_NAME,value="iframe")
        #self.driver.find_element(by = By.XPATH,value="(//*[text()='Click Me'])[1]").click()
        for eachframe in groups:

            self.driver.switch_to.frame(eachframe)
            finder = self.driver.find_elements(by=By.XPATH, value="(//button[@id='Click' and text()='Click Me'])[1]")
            if len(finder)>0:
                self.driver.find_element(by=By.XPATH, value="(//*[text()='Click Me'])[1]").click()
        else:
            self.driver.switch_to.default_content()

    def multiframes(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/frame.xhtml")
        self.driver.maximize_window()
        groups = self.driver.find_elements(by=By.TAG_NAME, value="iframe")
        for eachframe in groups:
            self.driver.switch_to.frame(eachframe)
            insideframe = self.driver.find_elements(by = By.TAG_NAME,value="iframe")
            if len(insideframe) > 0:
                self.driver.switch_to.frame("frame2")
            finder = self.driver.find_elements(by=By.XPATH, value="(//button[@id='Click' and text()='Click Me'])[2]")
            if len(finder)>0:
                    self.driver.find_element(by=By.XPATH, value="(//*[text()='Click Me'])[2]").click()
            else:
                self.driver.switch_to.default_content()

















obj = lis()
obj.multiframes()