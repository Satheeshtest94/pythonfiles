from selenium.webdriver.common.by import By


class login():

    username_path = (By.XPATH,"//*[@name = 'username']")
    password_path = (By.XPATH,"//*[@name = 'password']")
    button_path = (By.XPATH,"//*[contains(@class,'oxd-button')]")


    def __init__(self,driver):
        self.driver = driver
    def username(self,username):
        self.driver.find_element(*login.username_path).send_keys(username)
    def password(self,password):
        self.driver.find_element(*login.password_path).send_keys(password)
    def login_button(self):
        self.driver.find_element(*login.button_path).click()
