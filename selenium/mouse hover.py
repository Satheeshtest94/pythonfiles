from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class mousehovimplementation():
    def action(self,web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=web)
        self.driver.get("https://www.ebay.com/")
        element = ActionChains(self.driver)
        element.move_to_element(self.driver.find_element(by = By.XPATH,value="//*[@class='hl-cat-nav__container']//a[text()='Electronics'][1]")).perform()
        element.move_to_element(self.driver.find_element(by=By.XPATH,
                                                         value="//*[@class='hl-cat-nav__container']//a[text()='Computers and tablets']")).click().perform()
obj = mousehovimplementation()
obj.action()
