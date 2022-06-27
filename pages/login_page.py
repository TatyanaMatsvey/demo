from selenium.webdriver.chrome import webdriver
from time import sleep

import constants
from constants.login_page import LoginPageConstants
from constants.main_page import MainPageConstants

from selenium.webdriver.common.by import By

from pages.base import BasePage


class LoginPage(BasePage):
    """doc"""

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = LoginPageConstants()

    def login(self, login_value, password_value):
        self.fill_field(by=By.XPATH, locator=self.constants.LOGIN_FIELD_XPATH, value=login_value)
        self.fill_field(by=By.XPATH, locator=self.constants.PASSWORD_FIELD_XPATH, value=password_value)
        sleep(2)

        submit_button = self.driver.find_element(by=By.XPATH, value=self.constants.SUBMIT_BUTTON_XPATH)
        submit_button.click()
        sleep(2)

    def verify_correct_auth(self):
        # Find user icon on main page
        user_icon = self.driver.find_element(by=By.XPATH, value=self.constants.USER_ICON_XPATH)
        user_icon.is_displayed()

    def verify_incorrect_login(self):
        error_message = self.driver.find_element(by=By.XPATH, value=self.constants.ERROR_MESSAGE_XPATH)
        assert error_message.text == self.constants.ERROR_MESSAGE_TEXT

    def verify_empy_fields(self):
        sign_in_button = self.driver.find_element(by=By.XPATH, value=self.constants.SUBMIT_BUTTON_XPATH)
        sign_in_button.is_displayed()
