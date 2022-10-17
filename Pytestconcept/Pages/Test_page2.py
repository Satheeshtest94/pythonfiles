from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



class page2():

    message_path = (By.XPATH,"(//*[text()='PIM'])[2]")
    dropdown_path = (By.XPATH,"//*[contains(@class,'oxd-userdropdown-tab')]//i")
    logout_path = (By.XPATH,"//*[text()='Logout']")

    def __init__(self,driver):
        self.driver = driver
    def message(self):
          message = self.driver.find_element(*page2.message_path).text
          assert message == "PIM"
    def select_dropdown(self):
        self.driver.find_element(*page2.dropdown_path).click()
    def logout_button(self):
        WebDriverWait(self.driver, 60).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Logout']")))
        self.driver.find_element(*page2.logout_path).click()

