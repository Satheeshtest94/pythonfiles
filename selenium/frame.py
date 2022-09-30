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
        #self.driver.find_element(by = By.XPATH,value="(//button[@id='Click' and text()='Click Me'])[1]").click()
        #By using TAG locator
        # 1.Get the number of frames
        frames = self.driver.find_elements(by = By.TAG_NAME,value="iframe")
        for eachframe in range(0,len(frames)):#iterate through eachframes
            self.driver.switch_to.frame(eachframe)#iterate through eachframes and check element in there if there return >0
            clicker = self.driver.find_elements(by=By.XPATH, value="(//button[@id='Click' and text()='Click Me'])[1]")
            if len(clicker)>0:
                #element found going to click
                self.driver.find_element(by=By.XPATH, value="(//button[@id='Click' and text()='Click Me'])[1]").click()
                #Returning back to parent frame
                self.driver.switch_to.default_content()
                break#Process fininshed
            else:
                self.driver.switch_to.default_content()

    def multiframe(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/frame.xhtml")
        self.driver.maximize_window()
        frames = self.driver.find_elements(by=By.TAG_NAME, value="iframe")
        for eachframe in range(0, len(frames)):  # iterate through eachframes
            self.driver.switch_to.frame(eachframe) # iterate through eachframe
            insideframes = self.driver.find_elements(by=By.TAG_NAME, value="iframe")
            if len(insideframes)>0:
                self.driver.switch_to.frame("frame2")
            clicker = self.driver.find_elements(by=By.XPATH, value="(//button[@id='Click' and text()='Click Me'])[1]")
            if len(clicker) > 0:
                # element found going to click
                self.driver.find_element(by=By.XPATH, value="(//button[@id='Click' and text()='Click Me'])[1]").click()
                # Returning back to parent frame
                self.driver.switch_to.default_content()
                break  # Process fininshed
            else:
                self.driver.switch_to.default_content()

        else:
         self.driver.switch_to.default_content()



obj =  lis()
obj.multiframe()