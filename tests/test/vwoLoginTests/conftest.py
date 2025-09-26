import os
from selenium.webdriver import Chrome


import pytest
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()

driver = webdriver.Chrome()


@pytest.fixture(scope='class')
def setup(request):
    driver.maximize_window()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    request.cls.driver = driver
    request.cls.username = username
    request.cls.password = password

    yield driver  # return driver
    driver.quit()