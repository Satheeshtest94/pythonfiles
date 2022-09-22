from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class day4():
    def action(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=web)
        self.driver.get("https://www.facebook.com")
        #identify the element
        username = self.driver.find_element(by = By.XPATH ,value="/html/body/div/div/div/div/div/div/div/div/div/form/div/div/input")
        username.send_keys("Satheeshhkumarr@gmail.com")
obj = day4()
obj.action()

