from telnetlib import EC
from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from constants.base import BaseConstants
from constants.login_page import LoginPageConstants
from constants.add_new_language import AddNewLanguage


class TestAddNewLanguage:
    def test_add_new_language(self):
        # Authorization
        driver = webdriver.WebDriver(executable_path="../drivers/chromedriver")
        driver.get(BaseConstants.URL)
        # sleep(3)
        login_field = driver.find_element(by=By.XPATH, value=LoginPageConstants.LOGIN_FIELD_XPATH)
        login_field.clear()
        login_field.send_keys(LoginPageConstants.LOGIN_VALUE)
        sleep(2)
        password_field = driver.find_element(by=By.XPATH,
                                             value=LoginPageConstants.PASSWORD_FIELD_XPATH)
        password_field.clear()
        password_field.send_keys(LoginPageConstants.PASSWORD_VALUE)
        sleep(2)

        submit_button = driver.find_element(by=By.XPATH, value=LoginPageConstants.SUBMIT_BUTTON_XPATH)
        submit_button.click()
        sleep(2)

        # Find "Languages" in navigation menu
        languages_button = driver.find_element(by=By.XPATH, value=".//a[@href='/language/list']")
        languages_button.click()
        sleep(2)

        add_new_language_button = driver.find_element(by=By.XPATH, value=".//a[@href='/language/add']")
        add_new_language_button.click()

        # Test h3 is displayed and contain text "Adding a new language"
        h3_languages = driver.find_element(by=By.XPATH,
                                           value=AddNewLanguage.H3_LANGUAGES_XPATH)
        sleep(2)
        assert h3_languages.text == AddNewLanguage.H3_LANGUAGES_TEXT

        # Find and fill "Language Code:" field with STR type
        language_code = driver.find_element(by=By.XPATH, value=AddNewLanguage.LANGUAGE_CODE_XPATH)
        language_code.clear()
        language_code.send_keys(AddNewLanguage.LANGUAGE_CODE_VALUE)

        save_button = driver.find_element(by=By.XPATH, value=AddNewLanguage.SAVE_BUTTON_XPATH)
        save_button.click()
        sleep(3)

        check_lang_str = driver.find_element(by=By.XPATH, value=AddNewLanguage.CHECK_STR_XPATH)

        if EC.visibility_of_element_located(check_lang_str):
            return check_lang_str.text

        assert check_lang_str.text == AddNewLanguage.LANGUAGE_CODE_VALUE

        # запросить баннер об успешном добавлении провайдера
