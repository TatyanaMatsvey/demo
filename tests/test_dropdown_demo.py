from time import sleep
from telnetlib import EC

from pyatspi import action
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestDropdownDemo:
    def test_dropdown_demo(self):
        # Authorization
        driver = webdriver.WebDriver(executable_path="../drivers/chromedriver")
        driver.get("https://stage-tody.sptech.team/auth/login")
        # sleep(3)
        login_field = driver.find_element(by=By.XPATH, value=".//input[@type='text' and @placeholder='Login']")
        login_field.clear()
        login_field.send_keys("Visla")
        sleep(2)
        password_field = driver.find_element(by=By.XPATH,
                                             value=".//input[@type='password' and @placeholder='Password']")
        password_field.clear()
        password_field.send_keys("4u4a4u4aTesl@Pu")
        sleep(2)

        submit_button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        submit_button.click()
        sleep(2)
        #
        # # find dropdown and click 10 per page dropdown = driver.find_element(by=By.ID, value="dropdownMenuButton")
        # dropdown.click() dd_hidden_10 = driver.find_element(by=By.XPATH, value="/html/body/div/div/section[
        # 2]/div/div[1]/div[1]/div/div/a[1]") dd_action = ActionChains(driver) dd_action.click(dd_hidden_10)
        # dd_action.w3c_actions.perform() sleep(2)

        # find table
        table = driver.find_element(by=By.XPATH, value=".//tr[@class='accordion-content']")
