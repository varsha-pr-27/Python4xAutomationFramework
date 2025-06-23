import time

import allure
import pytest

from tests.pageObjects.DashboardPage import DashboardPage
from tests.pageObjects.LoginPage import LoginPage


class TestLogin:

    @allure.epic("VWO Login Test")
    @allure.description("TC#0 - VWO App Negative Test")
    @pytest.mark.usefixtures("setup")
    @pytest.mark.smoke
    @pytest.mark.negative
    def test_vwo_login_negative(self, setup):
        driver = setup
        login = LoginPage(driver)
        driver.get(self.base_url)
        login.login_to_vwo_page(usr=self.username, pwd="123")
        time.sleep(5)
        error_message = login.get_error_message_text()
        assert error_message == "Your email, password, IP address or location did not match"
        time.sleep(2)

    @allure.epic("VWO Login Test")
    @allure.description("TC#1 - VWO App Positive Test")
    @pytest.mark.usefixtures("setup")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_vwo_login_positive(self, setup):
        driver = setup
        login = LoginPage(driver)
        driver.get(self.base_url)
        login.login_to_vwo_page(usr=self.username, pwd=self.password)
        time.sleep(5)
        dashboard = DashboardPage(driver)
        assert "Dashboard" in driver.title
        assert "Aman" in dashboard.user_logged_in_text()
        time.sleep(2)
