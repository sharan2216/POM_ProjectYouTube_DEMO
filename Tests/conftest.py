import pytest
from selenium import webdriver
from Config.config import TestData
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.selenium_manager import SeleniumManager
# class Testdata:
#     pass

s = Service("D:\\CHROME\\DRIVERS\\chromedriver_win32.exe")


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=s)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.Firefox_executable_path)
    request.cls.driver = web_driver
    # webdriver.implicitly_wait(10)
    yield
    web_driver.close()
# @pytest.fixture(scope='class')
#   def init_chrome_driver(request):
#     web_driver = webdriver.Chrome()
#     request.cls.driver = web_driver
#     yield
#     web_driver.close()
