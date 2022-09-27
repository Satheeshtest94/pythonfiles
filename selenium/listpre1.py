import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec

class act():
    def act1(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/select.xhtml")
        self.driver.maximize_window()
        self.driver.find_element(by = By.XPATH,value="//*[contains(@id,'j_idt87:lang_label')]").click()
        time.sleep(3)
        group = self.driver.find_elements(by=By.XPATH, value="//*[contains(@id,'j_idt87:lang_items')]//li")
        time.sleep(3)

        for each in group:
            if each.text == "English":

             each.click()


             break

        time.sleep(5)
        self.driver.find_element(by = By.XPATH,value = "(//*[contains(@class,'ui-selectonemenu-trigger')])[4]").click()
        last1 = self.driver.find_elements(by=By.XPATH, value="//*[contains(@id,'j_idt87:value_items')]//li")
        for eachvalue in last1:
            if eachvalue.text == "One":
                eachvalue.click()

                break




obj = act()
obj.act1()
