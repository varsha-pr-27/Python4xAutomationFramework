import allure
import pytest
from selenium import webdriver
import time

from tests.pageObjects.LoginPage import LoginPage
from tests.pageObjects.DashboardPage import DashboardPage


# Start the web
@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    return driver


@allure.epic("VWO Login Test")
@allure.description("TC#0 - VWO App Negative Test")
@pytest.mark.negative
def test_vwo_login_negative(setup):
    driver = setup
    loginPage = LoginPage(driver)
    loginPage.login_to_vwo_page(usr="abc@gmail.com", pwd="admin")
    time.sleep(5)
    error_message = loginPage.get_error_message_text()
    assert error_message == "Your email, password, IP address or location did not match"
    time.sleep(2)


@allure.epic("VWO Login Test")
@allure.feature("TC#1 - VWO App Positive Test")
def test_vwo_login_positive(setup):
    driver = setup
    loginPage = LoginPage(driver)
    loginPage.login_to_vwo_page(usr="py2x@thetestingacademy@gmail.com", pwd="Wingify@1234")
    time.sleep(5)
    dashboardPage = DashboardPage(driver)
    assert "Dashboard" in driver.title
    assert "Aman" in dashboardPage.user_logged_in_text()
    time.sleep(2)
