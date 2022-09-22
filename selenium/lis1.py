import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

class lis():
    def action(self, jk,web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=web)
        self.driver.get("https://leafground.com/select.xhtml")
        #Left to arrow of list select
        self.driver.find_element(by = By.XPATH,value = '//*[@class="ui-selectonemenu-label ui-inputfield ui-corner-all"]').click()
        # whole list
        group = self.driver.find_elements(by = By.XPATH,value = "//*[contains(@role,'listbox')]")
        #group = self.driver.find_elements(by=By.XPATH, value="//*[contains(@id,'country_items')]//li")
        for each in group:
            if each.text == jk:
                each.click()
                break




obj = lis()
obj.action("Brazil")

