import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

class gridtry():
    def action(self,web=None):
        count = 0
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=web)
        self.driver.get("https://leafground.com/grid.xhtml")
        self.driver.maximize_window()
        #iterate over pages
        pages = self.driver.find_elements(by = By.XPATH,value="//*[contains(@class,'ui-paginator-page')]//a")
        for eachpages in range(1,len(pages)+1):
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

            self.driver.find_element(by = By.XPATH,value="//*[contains(@class,'ui-paginator-page')]//a["+str(eachpages)+"]").click()
            time.sleep(2)

            element = 1

            rows = self.driver.find_elements(by = By.XPATH,value="//*[contains(@id,'form:dt-products_data')]//tr")
            for eachrows in rows:

             Orderelement = self.driver.find_element(by=By.XPATH, value="//*[contains(@id,'form:dt-products_data')]//tr[" + str(element) + "]/td[3]").text
             print(Orderelement)


             if Orderelement == "Brown Purse":

                 eachrows.click()
                 break


             element = element + 1








obj = gridtry()
obj.action()