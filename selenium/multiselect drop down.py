import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec

class multidrop():
    def action(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options = web)
        self.driver.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        #WebDriverWait(self.driver,10).until(ec.presence_of_element_located(By.CSS_SELECTOR,'select#second'))
        element = Select(self.driver.find_element(by = By.CSS_SELECTOR,value='select#second'))
        if element.is_multiple:
            element.select_by_value("bonda")
            element.select_by_index(2)
            element.select_by_visible_text("Pizza")
            element.deselect_by_index(2)
            element.deselect_all()




obj = multidrop()
obj.action()