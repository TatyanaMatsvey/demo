from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class TestLogin:
    """Test login form with valid value"""

    def test_login(self):
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

        items = driver.find_elements_by_class_name("a")
        print(items)

        for item in items:
            href = item.get_attribute('target')
            print(href)

        #
