import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    username = os.getenv("NAME")
    password = os.getenv("PASSWORD")
    base_url = os.getenv("BASE_URL")
    driver.get(base_url)
    katalon_url = os.getenv("KATALON_URL")
    hr_url = os.getenv("HR_APP_URL")

    request.cls.driver = driver
    request.cls.username = username
    request.cls.password = password
    request.cls.base_url = base_url
    request.cls.katalon_url = katalon_url
    request.cls.hr_url = hr_url

    yield driver  # This is signal to Py int -> driver(sometime) -> quit
    driver.quit()
