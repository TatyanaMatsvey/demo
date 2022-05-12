import pytest
from selenium.webdriver.chrome import webdriver

from pages.login_page import LoginPage

'''Test login form'''


class TestLogin:
    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.WebDriver(executable_path="../drivers/chromedriver")
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def login_page(self, driver):
        driver.get("https://stage-tody.sptech.team/auth/login")
        return LoginPage(driver)

    def test_login(self, login_page):
        # fill fields to login
        login_page.login("Visla", "4u4a4u4aTesl@Pu")
        # verify user successful login and see user_icon on page
        login_page.verify_correct_auth()

    # def test_empy_login(self, login_page):
    #     # not fill fields to login
    #     login_page.login("", "")
    #     # verify user successful login and see user_icon on page
    #     login_page.verify_correct_auth()

    def test_unreal_user(self, login_page):
        # fill fields to login with not registered user
        login_page.login("Huilla", "testcom")
        # verify user successful login and see user_icon on page
        login_page.verify_incorrect_login()

    def test_incorrect_name(self, login_page):
        # incorrect email without point
        login_page.login("КТО НАТЕСТИЛ ТУТ", "test@hucom")
        # verify user successful login and see user_icon on page
        login_page.verify_incorrect_login()
