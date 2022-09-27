import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

class lis():
    def action(self,web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=web)
        self.driver.get("https://leafground.com/alert.xhtml")
        #Normal alert cant inspect
        """
        self.driver.find_element(by = By.XPATH,value="(//*[text()='Show'])[1]").click()
        time.sleep(1)
        element1 = self.driver.switch_to.alert
        time.sleep(1)
        element1.accept()


        self.driver.find_element(by=By.XPATH, value="(//*[text()='Show'])[2]").click()
        time.sleep(1)
        element2 = self.driver.switch_to.alert
        time.sleep(1)
        element2.dismiss()


        self.driver.find_element(by=By.XPATH, value="(//*[text()='Show'])[5]").click()
        time.sleep(1)
        element3 = self.driver.switch_to.alert
        time.sleep(1)
        element3.send_keys("Satheesh")
        element3.accept()

        #Sweet alert
        self.driver.find_element(by=By.XPATH, value="(//*[text()='Show'])[3]").click()
        self.driver.find_element(by=By.XPATH, value="//*[text()='Dismiss']").click()
        
        self.driver.find_element(by=By.XPATH, value="(//*[text()='Show'])[4]").click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="(//*[contains(@class,'ui-dialog-titlebar-icon')])[2]").click()
        
        """
        self.driver.find_element(by=By.XPATH, value="(//*[text()='Show'])[6]").click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="(//*[contains(@class,'ui-dialog-titlebar-icon')])[4]").click()

obj = lis()
obj.action()
