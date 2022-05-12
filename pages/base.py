import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """doc"""

    def __init__(self, driver):
        self.driver = driver
        self.log = logging.getLogger(__name__)
        self.wait = WebDriverWait(driver, timeout=5)

    def fill_field(self, by, locator, value):
        login_field = self.driver.find_element(by=By.XPATH, value=locator)
        login_field.clear()
        login_field.send_keys(value)

    def click_button(self, by, locator, value):
        button = self.driver.find_element(by=By.XPATH, value=locator)
        button.click()

    # def wait_until_find_element(self, by, value):
    #     """wait until find element"""
    #     return self.wait.until(EC.presence_of_element_located(locator=(by, value)))
