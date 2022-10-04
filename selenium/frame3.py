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
        hoving = ActionChains(self.driver)
        self.driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
        self.driver.maximize_window()
        frames = self.driver.find_elements(by=By.TAG_NAME, value="iframe")
        for eachframe in frames:
            self.driver.switch_to.frame(eachframe)
            framegroup = self.driver.find_elements(by = By.XPATH,value="(//*[contains(@class,'portfolio_icon')])[2]")
            if len(framegroup)>0:
             self.driver.find_element(by = By.XPATH,value="(//*[contains(@class,'portfolio_icon')])[2]").click()
             time.sleep(5)
             self.driver.quit()
        else:
            print("Elment not in frame")

obj = lis()
obj.frameconce()
