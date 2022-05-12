import string
import random
from telnetlib import EC
from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from constants.login_page import LoginPageConstants
from constants.base import BaseConstants
from constants.add_new_provider_page import AddNewProviderConstants


class TestAddProvider:
    def test_add_new_provider(self):
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

        # find and click provider button in nav menu
        providers_button = driver.find_element(by=By.XPATH, value=AddNewProviderConstants.PROVIDERS_BUTTON_XPATH)
        providers_button.click()
        sleep(1)

        # find and click Add new provider button
        add_new_provider_button = driver.find_element(by=By.XPATH, value=AddNewProviderConstants.ADD_NEW_PROVIDER_XPATH)
        add_new_provider_button.click()
        sleep(1)

        # find and fill Provider Title field
        provider_title = driver.find_element(by=By.XPATH, value=AddNewProviderConstants.PROVIDER_TITLE_XPATH)
        provider_title.clear()
        rnd_title = f" 1111aa {''.join(random.choice(string.ascii_letters) for i in range(5))}  provider0 "
        provider_title.send_keys(rnd_title)
        sleep(1)

        # click checkbox Restriction
        yes_checkbox = driver.find_element(by=By.XPATH, value=AddNewProviderConstants.CHECKBOX_YES_XPATH)
        yes_checkbox.click()
        sleep(1)

        # click on Save button
        save_button = driver.find_element(by=By.XPATH, value=AddNewProviderConstants.SAVE_BUTTON_XPATH)
        save_button.click()

        # запросить баннер об успешном добавлении провайдера
