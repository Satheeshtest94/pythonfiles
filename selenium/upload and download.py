import time
import pyperclip

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import pyautogui

class upanddown():
    def download(self):
        chromeoptions =webdriver.ChromeOptions()
        downloadpath = {"download.defaultdirectory":"C:\\Users\\Sathe\\PycharmProjects\\pythonProject1\\Pythonclass\\selenium\\"}
        chromeoptions.add_experimental_option("prefs",downloadpath)
        chromeoptions.add_argument("--start-maximized")
        chromeoptions.add_argument("--incognito")
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options=chromeoptions)
        self.driver.get("https://leafground.com/file.xhtml")
        time.sleep(3)
        self.driver.find_element(by = By.XPATH,value="//*[text()='Download']").click()
        time.sleep(3)
        self.driver.quit()
    def upload(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.get("https://leafground.com/file.xhtml")
        self.driver.maximize_window()

        self.driver.find_element(by = By.XPATH,value="(//*[text()='Choose'])[2]").click()
        pyperclip.copy("C:\\Users\\Sathe\\Downloads\\TestLeaf Logo.png")
        time.sleep(2)
        pyautogui.hotkey("ctrl","v")
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(2)
        filenameafterupload =self.driver.find_element(by = By.XPATH,value="(//*[text()='Upload'])[1]").click()




obj = upanddown()
obj.download()
obj.upload()

