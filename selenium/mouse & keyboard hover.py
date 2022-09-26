import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class mousehovimplementation():
    def action(self,web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.facebook.com/")
        element = ActionChains(self.driver)
        element.move_to_element(self.driver.find_element(by = By.ID,value = "email"))
        element.send_keys("Satheesh").perform()
        element.double_click().context_click().perform()

        time.sleep(2)
        pyautogui.press("down")
        time.sleep(2)
        pyautogui.press("down")
        time.sleep(2)
        pyautogui.press("down")
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(2)
        pyautogui.press("Tab")
        time.sleep(2)
        pyautogui.hotkey("ctrl","v")

        pyautogui.press("Tab")
        pyautogui.click()






obj = mousehovimplementation()
obj.action()
