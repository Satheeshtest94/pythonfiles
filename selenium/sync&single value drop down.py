import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

class day5():
    def wait(self,gender, web=None, ):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options=web)
        self.driver.get("https://www.facebook.com")
        #implicit wait
        self.driver.implicitly_wait(1)
        self.driver.find_element(by = By.LINK_TEXT,value="Create New Account").click()
        self.driver.find_element(by = By.NAME,value="firstname").send_keys("Satheesh")
        self.driver.find_element(by=By.NAME, value="lastname").send_keys("kumar")
        self.driver.find_element(by=By.NAME,value="reg_email__").send_keys("Satheeshhkumarr@gmail.com")
        #explicit wait
        WebDriverWait(self.driver,10).until(ec.presence_of_element_located((By.NAME,"reg_email_confirmation__")))
        self.driver.find_element(by = By.NAME,value='reg_email_confirmation__').send_keys("Satheeshhkumarr@gmail")
        self.driver.find_element(by=By.NAME, value='reg_passwd__').send_keys("1234")
        #Single value drop down
        Select(self.driver.find_element(by = By.ID,value="day")).select_by_value("2")
        Select(self.driver.find_element(by = By.ID,value="month")).select_by_index("3")
        Select(self.driver.find_element(by = By.ID,value="year")).select_by_visible_text("2005")
        #radio button
        if gender == "male":

            self.driver.find_element(by = By.XPATH,value='//*[text()="Male"]').click()
        elif gender =="female":
            self.driver.find_element(by=By.XPATH, value='//*[text()="Female"]').click()
        elif gender =="custom":
            self.driver.find_element(by=By.XPATH, value='//*[text()="Custom"]').click()
            #Select(self.driver.find_element(by = By.NAME,value="preferred_pronoun")).select_by_value(("1"))
            #Select(self.driver.find_element(by=By.NAME, value="preferred_pronoun")).select_by_index(("1"))
            Select(self.driver.find_element(by=By.NAME, value="preferred_pronoun")).select_by_visible_text(('They: "Wish them a happy birthday!"'))


        #Click submit button
        self.driver.find_element(by=By.NAME, value="websubmit").click()





        #self.driver.quit()

obj = day5()
obj.wait("custom")

