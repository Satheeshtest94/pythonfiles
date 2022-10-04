import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

class gridtry():
    def action(self,web=None):
        count = 0
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=web)
        self.driver.get("https://leafground.com/grid.xhtml")
        self.driver.maximize_window()
        pages = self.driver.find_elements(by = By.XPATH,value="//*[contains(@class,'ui-paginator-page')]//a")
        for eachpages in range(1,len(pages)+1):
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.driver.find_element(by = By.XPATH,value="//*[contains(@class,'ui-paginator-page')]//a["+str(eachpages)+"]").click()
            time.sleep(2)
            rows = self.driver.find_elements(by=By.XPATH,
                                             value="//*[contains(@class,'ui-datatable-data ui-widget-content')]//tr")
            for eachrows in range(1, len(rows)):
                time.sleep(2)
                # self.driver.find_element(by=By.XPATH, value="//div//*[text()='+productname+']").click()
                self.driver.find_element(by=By.XPATH, value="//div//*[text()='Black Watch']").click()
                self.driver.find_element(by=By.XPATH,
                                         value="//*[contains(@id,'form:dt-products_data')]//tr["+str(eachrows)+"]//td[2]").click()
                time.sleep(2)
                tableinside = self.driver.find_elements(by=By.XPATH,
                                                        value="//*[contains(@id,'form:dt-products:1:j_idt118_data')]//tr")
                time.sleep(1)
                for eachline in range(1, len(tableinside) + 1):
                    time.sleep(1)
                    orderstatus = self.driver.find_element(by=By.XPATH,
                                                           value="//*[contains(@id,'1:j_idt118_data')]//tr[" + str(
                                                               eachline) + "]//td[5]//span[2]").text
                    print(orderstatus)
                    # time.sleep(3)
                else:
                    print("No more rows inside table")
            else:
                print("Your order not here")

        else:
            print("Page over")


                





        #self.driver.quit()

obj = gridtry()
obj.action()