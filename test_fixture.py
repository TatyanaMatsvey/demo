from time import sleep
from telnetlib import EC

import pytest
from pyatspi import action
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage


class TestFixt:
    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def login_page(self, driver):
        driver.get("https://stage-tody.sptech.team/auth/login")
        return LoginPage(driver)

    def test_fixt(self, login_page):
        login_page.login("Visla", "4u4a4u4aTesl@Pu")

        # # find dropdown and click 10 per page dropdown = driver.find_element(by=By.ID, value="dropdownMenuButton")
        # dropdown.click() dd_hidden_10 = driver.find_element(by=By.XPATH, value="/html/body/div/div/section[
        # 2]/div/div[1]/div[1]/div/div/a[1]") dd_action = ActionChains(driver) dd_action.click(dd_hidden_10)
        # dd_action.w3c_actions.perform() sleep(2)
