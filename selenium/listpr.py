from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class check2():
    """
    def func(self, web=None):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options = web)
        self.driver.get("https://leafground.com/select.xhtml")
        self.driver.find_element(by = By.XPATH,value = "//*[contains(@id,'country')]//div[contains(@class,'ui-selectonemenu-trigger')]").click()
        group = self.driver.find_elements(by = By.XPATH,
                                          value='//*[contains(@id,"country_items")]//li')
        for each in group:
            if each.text == "Brazil":
               each.click()
               break

obj = check()
obj.func()


    """

class check1():
    def start(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.get("https://www.makemytrip.com/")
        self.driver.maximize_window()
        self.driver.find_element(by = By.XPATH,value="//*[text()='From']").click()
        group = self.driver.find_elements(by = By.XPATH ,value ="//*[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]")
        for each in group:
            if each.text == "Mumbai, India":
               each.click()





obj = check1()
obj.start()



