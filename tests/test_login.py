import pytest
from selenium.webdriver.chrome import webdriver

from constants.base import BaseConstants
from constants.login_page import LoginPageConstants
from pages.login_page import LoginPage

'''Test login form:
 - login valid data real user
 - login without data (empty fields)
 - login with valid but unregistered user
 - login with incorrect login name and valid password
 - login with real login name and incorrect password '''


class TestLogin:
    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.WebDriver(BaseConstants.DRIVER_PATH)
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def login_page(self, driver):
        driver.get(LoginPageConstants.URL)
        return LoginPage(driver)

    def test_login(self, login_page):
        # fill fields to log in
        login_page.login("Visla", "4u4a4u4aTesl@Pu")
        # verify user successful login and see user_icon on page
        login_page.verify_correct_auth()

    def test_empy_login(self, login_page):
        # not fill fields to log in
        login_page.login("", "")
        # verify user successful login still see SigIn button
        login_page.verify_empy_fields()

    def test_unreal_user(self, login_page):
        # fill fields to log in with not registered user data
        login_page.login("Hullio", "testcom")
        # verify user successful login and see user_icon on page
        login_page.verify_incorrect_login()

    def test_incorrect_name(self, login_page):
        # incorrect log in name
        login_page.login("КТО НАТЕСТИЛ ТУТ", "111111")
        # verify user successful login and see user_icon on page
        login_page.verify_incorrect_login()

    def test_incorrect_password(self, login_page):
        # incorrect password
        login_page.login("admin", "111111111")
        # verify user successful login and see user_icon on page
        login_page.verify_incorrect_login()
