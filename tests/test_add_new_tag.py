import random
import string
from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from constants.base import BaseConstants
from constants.login_page import LoginPageConstants
from constants.add_new_tag import AddNewTagConstants
from pages.base import BasePage


class TestAddNewTag:

    def test_add_new_tag(self):
        # Authorization
        driver = webdriver.WebDriver(executable_path=BaseConstants.DRIVER_PATH)
        driver.get(BaseConstants.URL)
        # sleep(3)
        login_field = driver.find_element(by=By.XPATH, value=LoginPageConstants.LOGIN_FIELD_XPATH)
        login_field.clear()
        login_field.send_keys("Visla")
        sleep(1)
        password_field = driver.find_element(by=By.XPATH,
                                             value=LoginPageConstants.PASSWORD_FIELD_XPATH)
        password_field.clear()
        password_field.send_keys("4u4a4u4aTesl@Pu")
        sleep(1)

        submit_button = driver.find_element(by=By.XPATH, value=LoginPageConstants.SUBMIT_BUTTON_XPATH)
        submit_button.click()
        sleep(3)

        # find and click Tags button in nav menu
        tags = driver.find_element(by=By.XPATH, value=AddNewTagConstants.TAG_NAV_MENU_XPATH)
        tags.click()
        sleep(1)

        # find and click Add new tag button
        add_new_tag_button = driver.find_element(by=By.XPATH, value=AddNewTagConstants.ADD_NEW_TAG_XPATH)
        add_new_tag_button.click()
        sleep(1)

        # find and field tag title field
        tag_title = driver.find_element(by=By.XPATH, value=AddNewTagConstants.TAG_TITLE_XPATH)
        tag_title.clear()
        rnd_tag = f" 111aa {''.join(random.choice(string.ascii_letters) for i in range(5))}  tag "
        tag_title.send_keys(rnd_tag)
        sleep(1)

        # save button click
        save_button = driver.find_element(by=By.XPATH, value=AddNewTagConstants.SAVE_BUTTON_XPATH)
        save_button.click()

        # запросить сообщение о подтверждении успешного добавления тега
