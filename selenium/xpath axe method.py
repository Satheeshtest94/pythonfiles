import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class day41():
    def add(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options = web)
        self.driver.get("https://www.facebook.com")
        self.driver.find_element(by = By.XPATH,value='//*[text()="Create New Account"]').click()
        #using following axes method
        #self.driver.find_element(by=By.XPATH, value='// *[ @ id = "day"] // following::option[2]').click()
        #using child axes method
        #self.driver.find_element(by=By.XPATH, value='// *[ @ id = "day"]').click()
        #time.sleep(5)
        #self.driver.find_element(by=By.XPATH, value='// *[ @ id = "day"] // child::option[2]').click()
        #using following sibling method
        #self.driver.find_element(by=By.XPATH, value='//*[@id="day"]//following-sibling::option[2]').click()
        # using following preceding method
        # self.driver.find_element(by=By.XPATH, value='//*[@id="day"]////*[@id="day"]//preceding::span').click()
        # using following parent with ancestor method
        #// *[ @ id = "day"] // parent::span
        #// *[ @ id = "day"] // ancestor::span
        # using following parent with descendant method
        #//*[@class="_5k_4"]//descendant::option

        time.sleep(5)

        #self.driver.find_element(by = By.XPATH,value="").send_keys("satheeshhkumarr@gmail.")
        self.driver.quit()

obj = day41()
obj.add()

