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
        self.driver.get("https://leafground.com/table.xhtml")
        self.driver.maximize_window()
        time.sleep(2)
        table = self.driver.find_elements(by = By.XPATH,value="//*[contains(@id,'form:j_idt89_data')]//tr")
        for eachvalue in range(1,len(table)):
            coloumn1 = self.driver.find_element(by = By.XPATH,value = "")

obj = lis()
obj.action()