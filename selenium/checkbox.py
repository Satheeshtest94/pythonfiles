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
        self.driver.get("https://leafground.com/checkbox.xhtml")
        self.driver.maximize_window()
        """
        self.driver.find_element(by = By.XPATH,value="//*[text()='Basic']").click()
        self.driver.find_element(by=By.XPATH, value="//*[text()='Ajax']").click()
        time.sleep(2)
        print(self.driver.find_element(by=By.XPATH, value="//*[text()='Checked']").text)
        """

        checkelements = self.driver.find_elements(by = By.XPATH,value="//*[contains(@class,'col-12')]//tbody//tr[1]//td")
        time.sleep(3)

        for eachvalue in checkelements:

            print(eachvalue.text)

            if eachvalue.text == "Java":
                time.sleep(2)
                eachvalue.click()
                time.sleep(2)

    def checklist(self, web=None):
        count = 0
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.get("https://leafground.com/checkbox.xhtml")
        self.driver.maximize_window()
        """
        self.driver.find_element(by = By.XPATH,value="//*[text()='Basic']").click()
        self.driver.find_element(by=By.XPATH, value="//*[text()='Ajax']").click()
        time.sleep(2)
        print(self.driver.find_element(by=By.XPATH, value="//*[text()='Checked']").text)
        """

        self.driver.find_element(by=By.XPATH, value="//*[contains(@class,'ui-selectcheckboxmenu-trigger')]").click()
        checkelements = self.driver.find_elements(by=By.XPATH,
                                                  value="//*[contains(@class,'ui-selectcheckboxmenu-items')]//*[contains(@role,'group')]//li//label")

        time.sleep(5)
        for eachvalue in checkelements:
            count+=1
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")



            if eachvalue.text == "London":



                time.sleep(2)
                print(eachvalue.text)
                self.driver.find_element(by=By.XPATH,
                                         value="//*[contains(@class,'ui-selectcheckboxmenu-items')]//*[contains(@role,'group')]//li[" + str(
                                             count) + "]//div//div[2]").click()

                break
        else:
                print("NA")





obj = lis()
obj.checklist()