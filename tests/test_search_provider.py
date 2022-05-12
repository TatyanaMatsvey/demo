from telnetlib import EC
from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestSearch:

    def test_search(self):
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

        """ go to providers page with search field"""
        # find and click provider button in nav menu
        provider_button = driver.find_element(by=By.XPATH, value=".//a[@href='/provider/list']")
        provider_button.click()

        """testing search field"""
        # find search field and send "ar"
        search_field = driver.find_element(by=By.XPATH, value=".//input[@id='provider_search_form_providerName']")
        search_field.clear()
        search_field.send_keys("Ar")

        # find and click SEARCH-submit button
        search_button = driver.find_element(by=By.XPATH, value=".//input[@type='submit']")
        search_button.click()
        sleep(3)

        # compare first search resul with search query "Ar"
        check_provider = driver.find_element(by=By.XPATH,
                                             value="/html/body/div/div/section[2]/div/div[2]/table/tbody/tr[1]/td[2]")

        x = check_provider.text[0:2]
        assert x == "Ar", "no match"
