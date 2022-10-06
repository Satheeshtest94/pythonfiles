import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

class frames():
    def frameconce(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://demoqa.com/frames")
        self.driver.maximize_window()
        # 1st frame
        self.driver.switch_to.frame(self.driver.find_element(by = By.ID,value="frame1"))
        element = self.driver.find_element(by=By.XPATH, value="//*[@id='sampleHeading']").text
        print("First frame:",element)
        #2nd frame
        #self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        self.driver.execute_script("window.scrollTo(0, document.querySelector('.scrollingContainer').scrollHeight);")
        time.sleep(2)
        self.driver.switch_to.frame("frame2")
        element2 = self.driver.find_element(by=By.XPATH, value="//*[@id='sampleHeading']").text
        print("Second frame:",element2)

    def multiframe(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://demoqa.com/nestedframes")
        self.driver.maximize_window()
        framescount = self.driver.find_elements(by=By.TAG_NAME, value="iframe")

        if len(framescount) > 0:
            time.sleep(5)
            self.driver.switch_to.frame(self.driver.find_element(by=By.ID, value="frame1"))
            element1 = self.driver.find_element(by=By.XPATH, value="//*[text()='Parent frame']").text
            print("First frame:", element1)
            insideframe = self.driver.find_elements(by=By.TAG_NAME, value="iframe")
            if len(insideframe) > 0:
                self.driver.switch_to.frame(self.driver.find_element(by=By.TAG_NAME, value="iframe"))
                element2 = self.driver.find_element(by=By.XPATH, value="//*[text()='Child Iframe']").text
                print("Nested second frame:", element2)
            time.sleep(5)
            self.driver.quit()



obj =  frames()
obj.frameconce()