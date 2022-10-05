import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

class calender():
    def calenconce(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/table.xhtml")
        self.driver.maximize_window()
        #select table option
        self.driver.find_element(by = By.XPATH,value="(//*[contains(@class,'pi-table layout-menuitem-icon')])[1]").click()
        time.sleep(1)
        #Select the calender option
        self.driver.find_element(by=By.XPATH,value="(//*[contains(@class,'pi-fw pi-calendar')])[2]").click()
        #total calender container
        elements = self.driver.find_elements(by = By.XPATH,value="//*[contains(@class,'fc-scrollgrid-sync-table')]//tbody//td")
        for eachvalue in elements:
            date = eachvalue.get_attribute("data-date")
            if date == "2022-10-18":
                eachvalue.click()
                time.sleep(1)
                #Adding title to pop up
                check = self.driver.find_elements(by=By.ID, value="//*[contains(@name,'j_idt87:title')]")
                print(len(check))
                time.sleep(3)
                #self.driver.find_element(by=By.ID, value="//*[contains(@id,'j_idt87:title')]").send_keys("Hello")

                # click save button
                self.driver.find_element(by = By.ID,value="//*[text()='Save']").click()
            else:
                print("Cant find the element")




obj = calender()
obj.calenconce()