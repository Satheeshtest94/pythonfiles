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
        #table = self.driver.find_elements(by = By.XPATH,value="//*[contains(@id,'form:j_idt89_data')]//tr")
        scroller = self.driver.find_elements(by=By.XPATH, value="//*[contains(@class,'ui-paginator-pages')]//a")
        for eachpage in range(1,len(scroller)):

            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            #eachpage click()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value="//*[contains(@class,'ui-paginator-pages')]//a["+str(eachpage)+"]").click()
            time.sleep(5)
            #eachrow.click()
            table = self.driver.find_elements(by=By.XPATH, value="//*[contains(@id,'form:j_idt89_data')]//tr")
            for eachvalue in range(1,len(table)+1):
             time.sleep(2)
             countryname = self.driver.find_element(by = By.XPATH,value = "//*[contains(@id,'form:j_idt89_data')]//tr["+str(eachvalue)+"]//td[2]//span[3]").text

             if countryname == "India":
                 Representativename = self.driver.find_element(by=By.XPATH, value="//*[contains(@id,'form:j_idt89_data')]//tr["+str(eachvalue)+"]//td[3]//span[2]").text
                 status = self.driver.find_element(by=By.XPATH, value="//*[contains(@id,'form:j_idt89_data')]//tr["+str(eachvalue)+"]//td[5]//span[2]").text
                 print(countryname,Representativename,status)




obj = lis()
obj.action()