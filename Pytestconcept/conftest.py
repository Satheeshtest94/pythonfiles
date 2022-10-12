
import pytest
from selenium import  webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from Testdata import testdata


@pytest.fixture(scope="class")
def open_launch_exit(request):
   web = webdriver.ChromeOptions()
   driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
   web.add_argument("--start maximized")
   request.cls.driver = driver
   yield
   driver.quit()
@pytest.fixture()
def user_name(request):
   return[testdata.username,testdata.password]

@pytest.fixture(params=[{testdata.username,testdata.password},{testdata.username,testdata.password}]

)
def multi_data(request):
   return request.param