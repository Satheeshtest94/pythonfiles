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
        for eachframe in range(1, len(frames)):  # iterate through eachframes
            self.driver.switch_to.frame(eachframe)
            framesgroup = self.driver.find_elements(by=By.TAG_NAME, value="iframe")
            if len(framesgroup)>0:
             self.driver.switch_to.frame(eachframe)  # iterate through eachframes and check element in there if there return >0
             time.sleep(5)
             cheker=self.driver.find_elements(by=By.XPATH,value="//*[text()='Selenium 3.0 Training']")
             print(len(cheker))
             if len(cheker)>0:
              self.driver.find_element(by=By.XPATH,value="//*[text()='Selenium 3.0 Training']").click()
             """
             print(len(dropgroups))
             if len(dropgroups)>0:

                 time.sleep(3)
                 hoving.move_to_element(self.driver.find_element(by = By.XPATH,value="//*[contains(@id,'portfolio_filter')]")).perform()
                 #headoflist = self.driver.find_element(by = By.XPATH,value="//*[contains(@id,'portfolio_filter')]").click()
                 #dropgroups = self.driver.find_elements(by=By.XPATH, value="//*[contains(@id,'portfolio_filter')]//li//div")
                 time.sleep(3)
                 self.driver.quit()



            
            for eachitem in range(1,len(dropgroups)):
                if len(dropgroups) > 0:
                    dropclick = self.driver.find_element(by=By.XPATH,
                                                         value="//*[contains(@id,'portfolio_filter')]").click()
                if eachitem == "Automation":
                    eachitem.click()
                else:
                    print("item not there")
            """




obj = lis()
obj.frameconce()