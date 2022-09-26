import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class act():
    def act1(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/select.xhtml")
        self.driver.maximize_window()
        self.driver.find_element(by = By.XPATH,value="//*[contains(@id,'j_idt87:lang_label')]").click()
        time.sleep(3)
        group = self.driver.find_elements(by=By.XPATH, value="//*[contains(@class,'ui-selectonemenu-items')]//li")
        for each in group:
            if each.text == "English":

             each.click()

            break



obj = act()
obj.act1()
