from time import sleep

from selenium.webdriver.common.by import By
from webdriver_manager import driver

from pages.base import BasePage
from constants.add_new_provider_page import AddNewProviderConstants


class AddNewProvider(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = AddNewProviderConstants()

    # def login(self, login_value, password_value):
    #     self.fill_field(by=By.XPATH, locator=self.constants.LOGIN_FIELD_XPATH, value=login_value)
    #     self.fill_field(by=By.XPATH, locator=self.constants.PASSWORD_FIELD_XPATH, value=password_value)
    #     sleep(2)
    #
    #     submit_button = self.driver.find_element(by=By.XPATH, value=self.constants.SUBMIT_BUTTON_XPATH)
    #     submit_button.click()
    #     sleep(2)

    def add_new_provider(self, providers_button, add_new_providers_button):
        self.click_button(by=By.XPATH, locator=self.constants.PROVIDERS_BUTTON_XPATH)
        self.click_button(by=By.XPATH, locator=self.constants.ADD_NEW_PROVIDER_XPATH)

        # # find and click provider button in nav menu
        # providers_button = driver.find_element(by=By.XPATH, value=AddNewProviderConstants.PROVIDERS_BUTTON_XPATH)
        # providers_button.click()
        # sleep(1)
        #
        # # find and click Add new provider button
        # add_new_provider_button = driver.find_element(by=By.XPATH, value=AddNewProviderConstants.ADD_NEW_PROVIDER_XPATH)
        # add_new_provider_button.click()
        # sleep(1)

        # # find and fill Provider Title field
        # provider_title = driver.find_element(by=By.XPATH, value=AddNewProviderConstants.PROVIDER_TITLE_XPATH)
        # provider_title.clear()
        # rnd_title = f" 1111aa {''.join(random.choice(string.ascii_letters) for i in range(5))}  provider0 "
        # provider_title.send_keys(rnd_title)
        # sleep(1)
        #
        # # click checkbox Restriction
        # yes_checkbox = driver.find_element(by=By.XPATH, value=AddNewProviderConstants.CHECKBOX_YES_XPATH)
        # yes_checkbox.click()
        # sleep(1)
        #
        # # click on Save button
        # save_button = driver.find_element(by=By.XPATH, value=AddNewProviderConstants.SAVE_BUTTON_XPATH)
        # save_button.click()
