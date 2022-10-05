import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

class demoautosuggest():
    def autosuggestdrop(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.yatra.com/")
        self.driver.maximize_window()
        depart_from = self.driver.find_element(by = By.XPATH,value="(//input[contains(@id,'BE_flight_origin_city')])[1]")

        time.sleep(2)
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys("New Delhi")
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)

        going_to =self.driver.find_element(by = By.XPATH,value="//*[@id='BE_flight_arrival_city']")
        time.sleep(1)
        going_to.click()
        time.sleep(1)
        going_to.send_keys("New")
        searchresults = self.driver.find_elements(by = By.XPATH,value="//*[@class='ac_results dest_ac']//div[1]//li")
        for results in searchresults:
            if "New York (JFK)" in results.text:
                results.click()
                break




obj = demoautosuggest()
obj.autosuggestdrop()