import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class day4():
    def action(self,web = None):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options = web)
        self.driver.get("https://www.facebook.com")
        time.sleep(5)
        """
        self.driver.find_element(by = By.LINK_TEXT ,value="Forgotten password?").click()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value="Forgotten account?").click()
        time.sleep(5)
        """
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="password?").click()
        time.sleep(5)



obj = day4()
obj.action()