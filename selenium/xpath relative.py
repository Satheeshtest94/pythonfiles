import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class day4():
    def las(self, web=None):
        self.driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()),options=web)
        self.driver.get("https://www.facebook.com")
        """#Basic path
        self.driver.find_element(by = By.XPATH,value='//input[@data-testid = "royal_email"]').send_keys("satheeshhkumarr@gmail.co")
        time.sleep(5)
        #contains class att
        self.driver.find_element(by = By.XPATH ,value="//*[contains(@class,'inputtext _55r1')]").send_keys("satheeshhkumarr@gmail.co")
        #contains
        self.driver.find_element(by=By.XPATH, value='//*[@id = "pass"]').send_keys("1234")
        time.sleep(5)
        """
        """
        # contains
        self.driver.find_element(by=By.XPATH, value='//button[contains(@id,"u_0_")]').click()
        time.sleep(5)
        """
        # startswith
        #self.driver.find_element(by=By.XPATH, value='//button[starts-with(@id,"u_0_")]').click()
        #time.sleep(5)
        # text
        self.driver.find_element(by=By.XPATH, value='//*[text()="Create New Account"]').click()
        time.sleep(5)
        #self.driver.quit()

        #and & or - Relative x path

        #self.driver.find_element(by = By.XPATH ,value="//*[@id='email' and contains(@class,'inputtext _55r1 _')]").send_keys("satheeshhkumarr@gmail.")



obj = day4()
obj.las()
