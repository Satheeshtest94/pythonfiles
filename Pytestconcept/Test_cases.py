import time

import pytest
from selenium import  webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Pytestconcept.Pages.Test_loginpage import login
from Pytestconcept.Pages.Test_page2 import page2


@pytest.mark.usefixtures("open_launch_exit")
class Test_login():
    def test_Loginpage(self,multi_data):
        #web = webdriver.ChromeOptions()
        #self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.maximize_window()

        for iter in range(1,4):
            #Login page

            #username
            time.sleep(4)
            orangelogin = login(self.driver)
            orangelogin.username(multi_data["username"])
            orangelogin.password(multi_data["password"])
            orangelogin.login_button()
            time.sleep(4)
            message = self.driver.find_element(by=By.XPATH, value="(//*[text()='PIM'])[2]").text

            #logout
            time.sleep(5)
            #Logoutdropdown
            innerpage= page2(self.driver)
            time.sleep(5)
            innerpage.message()
            innerpage.select_dropdown()
            innerpage.logout_button()






















