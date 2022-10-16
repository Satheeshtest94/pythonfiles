from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



class page2():

    def __init__(self,driver):
        self.driver = driver
    def message(self):
          self.message = self.driver.find_element(by=By.XPATH, value="(//*[text()='PIM'])[2]").text
          assert self.message == "PIM"

    def select_dropdown(self):
        self.driver.find_element(by=By.XPATH, value="//*[contains(@class,'oxd-userdropdown-tab')]//i").click()
    def logout_button(self):
        WebDriverWait(self.driver, 60).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Logout']")))
        self.driver.find_element(by=By.XPATH, value="//*[text()='Logout']").click()

