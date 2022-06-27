import pickle
import random
import string
from time import sleep

import pytest
from selenium.webdriver import ActionChains

from constants.add_new_demo_page import AddNewDemoPageConstants
from constants.base import BaseConstants
from constants.login_page import LoginPageConstants
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from pages.add_new_demo_page import AddNewDemoPage
from pages.login_page import LoginPage
from pages.demos_page import DemosPage


class TestAddDemo:
    """Positive test to ADD NEW DEMO
    - authorization on Tody
    - go to ADD NEW DEMO page
    - fill all fields with valid data
    - press save button
    - assert SUCCESS message"""

    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.WebDriver(executable_path="../drivers/chromedriver")
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def login_page(self, driver):
        driver.get(LoginPageConstants.URL)
        return LoginPage(driver)

    @pytest.fixture(scope="function")
    def add_new_demo(self, driver):
        driver.get(AddNewDemoPageConstants.URL)
        return AddNewDemoPage(driver)

    def test_add_demo(self, login_page, add_new_demo):
        # fill fields to log in
        login_page.login("Visla", "4u4a4u4aTesl@Pu")
        login_page.verify_correct_auth()
        add_new_demo.fill_fields_new_demo()
        add_new_demo.verify_message()
