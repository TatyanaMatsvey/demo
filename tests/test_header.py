from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from constants.header import HeaderConstants
from constants.base import BaseConstants
from constants.login_page import LoginPageConstants
from selenium.common.exceptions import NoSuchElementException

'''Checked nav menu:
- nav menu is displayed
- nav menu buttons are clickable'''


class TestHeader:
    def test_header(self):
        # Authorization
        driver = webdriver.WebDriver(executable_path=BaseConstants.DRIVER_PATH)
        driver.get(BaseConstants.URL)
        # sleep(3)
        login_field = driver.find_element(by=By.XPATH, value=LoginPageConstants.LOGIN_FIELD_XPATH)
        login_field.clear()
        login_field.send_keys("Visla")
        sleep(2)
        password_field = driver.find_element(by=By.XPATH,
                                             value=LoginPageConstants.PASSWORD_FIELD_XPATH)
        password_field.clear()
        password_field.send_keys("4u4a4u4aTesl@Pu")
        sleep(2)

        submit_button = driver.find_element(by=By.XPATH, value=LoginPageConstants.SUBMIT_BUTTON_XPATH)
        submit_button.click()
        sleep(2)

        # try:
        #     providers = driver.find_element(by=By.XPATH, value=HeaderConstants.PROVIDERS_BUTTON_XPATH)
        #     return True
        # except NoSuchElementException:
        #     print('Zero element for U!')
        #     return False

        # demos is displayed
        demos = driver.find_element(by=By.XPATH, value=HeaderConstants.DEMOS_BUTTON_XPATH)
        demos.is_displayed()
        assert demos.is_displayed() == True, "de1mos button is not displayed"

        # providers button is displayed
        # providers = driver.find_element(by=By.XPATH, value=HeaderConstants.PROVIDERS_BUTTON_XPATH)
        # assert providers. == "Providers", "providers button is not displayed"
        #
        # # tags is displayed
        # tags = driver.find_element(by=By.XPATH, value=HeaderConstants.TAGS_BUTTON_XPATH)
        # tags.is_displayed()
        # assert tags.is_displayed() == True, "tags button is not displayed"
        #
        # # languages button is displayed
        # languages = driver.find_element(by=By.XPATH, value=HeaderConstants.LANGUAGES_BUTTON_XPATH)
        # languages.is_displayed()
        # assert languages.is_displayed() == True, "languages button is not displayed"
