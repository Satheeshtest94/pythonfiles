import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class day3():
    def action(self, web=None):
        self.driver = webdriver.Chrome(service  = Service(ChromeDriverManager().install()),options = web)
        self.driver.get("https://www.facebook.com")
        time.sleep(5)
        #CSS Selector with Tag & Class
        print(self.driver.find_element(by = By.CSS_SELECTOR,value ="h2._8eso" ).text)
        #css selector with  TAG & id
        username = self.driver.find_element(by=By.CSS_SELECTOR, value="input#email")  # web element identification
        username.send_keys("satheeshhkumarr@gmail.com")
        time.sleep(5)
        # Css selector with TAG with  attribute name and its value
        password = self.driver.find_element(by=By.CSS_SELECTOR, value="input[name=pass]")
        password.send_keys("1234")
        time.sleep(5)
        # Css selector with TAG with class value  [attribute name and its value]
        """
        
        username = self.driver.find_element(by = By.ID ,value="email")#web element identification
        username.send_keys("satheeshhkumarr@gmail.com")
        time.sleep(5)
        password = self.driver.find_element(by = By.ID ,value="pass")
        password.send_keys("1234")
        button = self.driver.find_element(by = By.NAME,value ="login")
        button.click()
        #self.driver.quit()
        
        username = self.driver.find_element(by=By.CSS_SELECTOR, value="email")  # web element identification
        username.send_keys("satheeshhkumarr@gmail.com")
        time.sleep(5)
        password = self.driver.find_element(by=By.CSS_SELECTOR, value="pass")
        password.send_keys("1234")
        button = self.driver.find_element(by=By.CSS_SELECTOR, value="login")
        button.click()
        """





obj = day3()
obj.action()
