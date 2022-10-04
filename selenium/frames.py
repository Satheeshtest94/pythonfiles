import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

class frames():
    def singleframe(self,web=None):

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=web)
        self.driver.get("https://leafground.com/frame.xhtml")
        self.driver.maximize_window()
        frames = self.driver.find_elements(by = By.TAG_NAME,value="iframe")
        for eachframe in frames:
            if len(frames) > 0:
                self.driver.switch_to.frame(eachframe)
                self.driver.find_element(by = By.XPATH,value="(//*[text()='Click Me'])[1]").click()
                print("Frame found and Switched")
                break

    def multiframe(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/frame.xhtml")
        self.driver.maximize_window()
        frames = self.driver.find_elements(by=By.TAG_NAME, value="iframe")
        for eachframe in frames:
            self.driver.switch_to.frame(eachframe)
            element = self.driver.find_elements(by=By.XPATH, value="(//*[text()='Click Me'])[2]")
            if len(element) >0:
                element = self.driver.find_element(by=By.XPATH, value="(//*[text()='Click Me'])[2]").click()
            else:
                self.driver.switch_to.default_content()








obj = frames()
obj.multiframe()
