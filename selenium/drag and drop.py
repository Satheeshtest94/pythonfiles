from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class keyb():
    def start(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/drag.xhtml")
        self.driver.maximize_window()
        element = ActionChains(self.driver)
        element.move_to_element(self.driver.find_element(by = By.ID,value="form:drag")).\
            drag_and_drop(self.driver.find_element(by = By.ID,value="form:drag"),self.driver.find_element(by = By.ID,value="form:drop_content")).perform()


obj = keyb()
obj.start()
