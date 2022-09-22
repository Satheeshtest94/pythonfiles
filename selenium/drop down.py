from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec

class day():
    def action(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options = web)
        self.driver.get("https://leafground.com/waits.xhtml")
        self.driver.implicitly_wait(1)
        WebDriverWait(self.driver,10).until(ec.visibility_of_element_located())
        self.driver.find_element(by = By.XPATH,value='//*[text()="Click"]').click()

obj = day()
obj.action()


