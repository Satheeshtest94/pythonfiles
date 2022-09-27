import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


class lis():
    def action(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.get("https://leafground.com/window.xhtml")
        obj.screenshot("Go to window")
        self.driver.find_element(by = By.XPATH,value="//*[text()='Open Multiple']").click()
        obj.screenshot("Go to window")
        currentwindow = self.driver.current_window_handle
        allwindow = self.driver.window_handles
        for eachwindow in allwindow:
            if eachwindow!=currentwindow:
                self.driver.switch_to.window(eachwindow)
                obj.screenshot("Go to window")
                checkelement = self.driver.find_elements(by=By.XPATH, value="//*[text()='Browser']//ancestor::a")

                if len(checkelement) > 0:
                    self.driver.maximize_window()
                    obj.screenshot("large")
                    time.sleep(3)
                    self.driver.find_element(by=By.XPATH, value="(//*[text()='Browser']//ancestor::a)").click()
                    obj.screenshot("clicking")
                    self.driver.find_element(by=By.XPATH, value="(//*[text()='Alert'])[1]").click()
                    obj.screenshot("finding")

                    WebDriverWait(self.driver, 60).until(ec.element_to_be_clickable(
                        self.driver.find_element(by=By.XPATH, value="(//*[text()='Show'])[1]")))
                    obj.screenshot("waiting")
                    # verfication

                    print(self.driver.title)
                    print(self.driver.current_url)
                    print(self.driver.find_element(by=By.XPATH, value="(//*[text()='Show'])[1]").get_attribute("class"))
                    obj.screenshot("get atrr")
                    print(self.driver.current_window_handle)
                    print(self.driver.window_handles)

                    # validation
                    print(self.driver.find_element(by=By.XPATH, value="(//*[text()='Show'])[1]").is_displayed())
                    print(self.driver.find_element(by=By.XPATH, value="(//*[text()='Show'])[1]").is_enabled())
                    print(self.driver.find_element(by=By.XPATH, value="(//*[text()='Show'])[1]").is_selected())
                    self.driver.close()
                    obj.screenshot("close")
                    self.driver.switch_to.window(currentwindow)

    def screenshot(self,filename):
         self.driver.save_screenshot("C:\\Users\\Sathe\\PycharmProjects\\pythonProject1\\Pythonclass\\screenshots\\"+filename+".png")



obj = lis()
obj.action()