from selenium.webdriver.common.by import By


class login():
    def __init__(self,driver):
        self.driver = driver
    def username(self,username):
        self.driver.find_element(by=By.XPATH, value="//*[@name = 'username']").send_keys(username)
    def password(self,password):
        self.driver.find_element(by=By.XPATH, value="//*[@name = 'password']").send_keys(password)
    def login_button(self):
        self.driver.find_element(by=By.XPATH, value="//*[contains(@class,'oxd-button')]").click()
