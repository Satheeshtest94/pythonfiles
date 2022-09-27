import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

class lis():
    def action(self,web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=web)
        self.driver.get("https://leafground.com/dashboard.xhtml")
        self.driver.maximize_window()
        """
        time.sleep(5)
        #Vertical bottom scroll
        self.driver.execute_script("window.scrollTo(0,700)","")
        # Vertical Top scroll
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,-700)", "")
        #Horizontal top scroll
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(-700,0)", "")
        #Horizontal bottom scroll
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(800,0)", "")
        """
        time.sleep(2)
        #Scroll downward
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        obj.screenshot("Scrolldown")
        #scroll upward
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,-0);")
        obj.screenshot("Scrollup")
        #going near by element

        elementtill = self.driver.find_element(by = By.XPATH,value = "(//*[text()='Events'])[2]")
        obj.screenshot("nearbyelement")
        #element identifying
        time.sleep(2)
        element = self.driver.find_element(by = By.XPATH,value = "//*[text()='Previous']")
        obj.screenshot("Target")

        self.driver.execute_script("arguments[0].scrollIntoView();",elementtill)
        element.click()
        obj.screenshot("Targetclicked")

#Screenshot

    def screenshot(self,filename):
        self.driver.save_screenshot("C:\\Users\\Sathe\\PycharmProjects\\pythonProject1\\Pythonclass\\screenshots\\" +filename+".png")





obj = lis()
obj.action()