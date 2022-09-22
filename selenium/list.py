import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

class lis():
    def action(self,expectedelement, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=web)
        self.driver.get("https://leafground.com/select.xhtml")
        #WebDriverWait(self.driver,10).until(ec.presence_of_element_located())
        #drop down first line
        element1 = Select(self.driver.find_element(by = By.CLASS_NAME,value="ui-selectonemenu"))
        #drop down values
        element1.select_by_visible_text("Selenium")
        time.sleep(2)
        #List box right side arrow button
        self.driver.find_element(by = By.XPATH,value="//*[contains(@id,'country')]//div[contains(@class,'ui-selectonemenu')]").click()
        #list box all element
        group = self.driver.find_elements(by=By.XPATH,
                                 value="//*[contains(@id,'country_items')]//li")

        for each in group:
            if each.text == expectedelement:
                each.click()
                break


        groupnext = 0




        time.sleep(2)
        self.driver.quit()


obj = lis()
obj.action("Germany")

