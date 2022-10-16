
import pytest
from selenium import  webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from Pytestconcept import Testdata
from Pytestconcept.Utils.excelinput import datainput


@pytest.fixture(scope="class")
def open_launch_exit(request):
   web = webdriver.ChromeOptions()
   driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
   driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
   web.add_argument("--start maximized")
   request.cls.driver = driver
   yield
   driver.quit()
@pytest.fixture()
def user_name(request):
   return Testdata.datafromexcel

@pytest.fixture(params=Testdata.datafromexcel)
def multi_data(request):
   return request.param