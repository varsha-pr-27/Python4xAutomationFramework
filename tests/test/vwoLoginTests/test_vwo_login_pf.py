import logging
import time

import allure
import pytest
from tests.pageObjects.page_factory.dashboardPage_pf import DashboardPage
from tests.pageObjects.page_factory.loginPage_pf import LoginPage

from tests.constants.constants import Constants


@allure.epic("VWO App")
@allure.feature("Login Test")
class TestVWOLogin:

    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwo_login_negative(self, setup):
        logger = logging.getLogger(__name__)
        driver = setup
        driver.get(Constants.app_url())
        login_page = LoginPage(driver)
        login_page.login_to_vwo(user=self.username, pwd="123")
        error_msg_element = login_page.error_msg()
        logger.info("Negative cases done.")
        assert error_msg_element == "Your email, password, IP address or location did not match"

        if "Dashboard" not in driver.title:
            Constants.take_screenshot(driver, "test_vwo_login_negative_tc0")

    def test_vwo_login_positive(self, setup):
        logger = logging.getLogger(__name__)
        logger.info("Starting the Testcase")
        driver = setup
        driver.get(Constants.app_url())
        login_page = LoginPage(driver)
        login_page.login_to_vwo(user=self.username, pwd=self.password)
        dashboard_page = DashboardPage(driver)
        username = dashboard_page.user_logged_in_text()
        assert "Dashboard" in driver.title
        assert "Aman Ji" == username
        time.sleep(5)

    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwo_login_negative_tc3(self, setup):
        pass

    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwo_login_negative_tc4(self, setup):
        pass
