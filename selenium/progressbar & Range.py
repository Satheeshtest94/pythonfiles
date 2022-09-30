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
    def progressbar(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/drag.xhtml")
        self.driver.maximize_window()
        #self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        #page middle
        self.driver.execute_script("document.querySelector('.ui-state-default').style.left ='0%'")
        time.sleep(5)
        #page down
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        self.driver.find_element(by = By.XPATH, value = "//*[text()='Start']").click()
        WebDriverWait(self.driver,60).\
            until(ec.text_to_be_present_in_element(
             (By.XPATH,"//*[contains(@class,'ui-progressbar-label')]"),"100%"))
        print(self.driver.find_element(by=By.XPATH, value="//*[text()='Progress Completed']").text)
        time.sleep(3)
        self.driver.quit()


    def range(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/drag.xhtml")
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        element = ActionChains(self.driver)
        #Entire line between 2 node
        fromvalue = self.driver.find_element(by = By.XPATH,value="//*[contains(@id,'form:j_idt125')]//span[2]")
        #Hold and move to respective position from residing place
        element.move_to_element\
            (self.driver.find_element(by = By.XPATH,value="//*[contains(@id,'form:j_idt125')]//div[1]")).drag_and_drop_by_offset(fromvalue,-100,5).perform()



obj = lis()
obj.range()