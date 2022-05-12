import random
from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:

    def random_num(self):
        """Generate random number"""
        return str(random.choice(range(11111, 99999)))

    # invalid login and password
    def test_invalid_sign_in(self):
        '''Test invalid username and invalid password'''
        driver = webdriver.WebDriver(executable_path="../drivers/chromedriver")
        driver.get("https://stage-tody.sptech.team/auth/login")
        login = driver.find_element(by=By.XPATH, value=".//input[@type='text' and @name='_username']")
        login.clear()
        # random name
        login.send_keys(f"userName{self.random_num()}")
        sleep(2)
        password = driver.find_element(by=By.XPATH, value=".//input[@type='password' and @name='_password']")
        password.clear()
        # random password
        password.send_keys(f"Pwd{self.random_num()}")
        sleep(2)
        sign_in_button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        sign_in_button.click()
        message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger']")
        assert message.text == "An authentication exception occurred."

    # invalid password and verified name
    def test_invalid_password(self):
        '''Test invalid username and invalid password'''
        driver = webdriver.WebDriver(executable_path="../drivers/chromedriver")
        driver.get("https://stage-tody.sptech.team/auth/login")
        login = driver.find_element(by=By.XPATH, value=".//input[@type='text' and @name='_username']")
        login.clear()
        # verified name
        login.send_keys("visla")
        sleep(2)
        password = driver.find_element(by=By.XPATH, value=".//input[@type='password' and @name='_password']")
        password.clear()
        # random password
        password.send_keys(f"Pwd{self.random_num()}")
        sleep(2)
        sign_in_button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        sign_in_button.click()
        message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger']")
        assert message.text == "An authentication exception occurred."

    # invalid name and valid password
    def test_invalid_name(self):
        '''Test invalid username and invalid password'''
        driver = webdriver.WebDriver(executable_path="../drivers/chromedriver")
        driver.get("https://stage-tody.sptech.team/auth/login")
        login = driver.find_element(by=By.XPATH, value=".//input[@type='text' and @name='_username']")
        login.clear()
        # random_name
        login.send_keys(f"userName{self.random_num()}")
        sleep(2)
        password = driver.find_element(by=By.XPATH, value=".//input[@type='password' and @name='_password']")
        password.clear()
        # random password
        password.send_keys("4u4a4u4aTesl@Pu")
        sleep(2)
        sign_in_button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        sign_in_button.click()
        message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger']")
        assert message.text == "An authentication exception occurred."

    # valid password and valid name
    def test_valid_login(self):
        '''Test invalid username and invalid password'''
        driver = webdriver.WebDriver(executable_path="../drivers/chromedriver")
        driver.get("https://stage-tody.sptech.team/auth/login")
        login = driver.find_element(by=By.XPATH, value=".//input[@type='text' and @name='_username']")
        login.clear()
        # verified name
        login.send_keys("visla")
        sleep(2)
        password = driver.find_element(by=By.XPATH, value=".//input[@type='password' and @name='_password']")
        password.clear()
        # random password
        password.send_keys("4u4a4u4aTesl@Pu")
        sleep(2)
        sign_in_button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        sign_in_button.click()
        logout_button = driver.find_element(by=By.XPATH,
                                            value=".//a[@href='/auth/logout' and @class='d-block nav-link']")
        logout_button.is_displayed()

    # Наличие Placeholder в поле Login
    def test_placeholder_login(self):
        driver = webdriver.WebDriver(executable_path="../drivers/chromedriver")
        driver.get("https://stage-tody.sptech.team/auth/login")
        placeholder = driver.find_element(by=By.XPATH,
                                          value=".//input[@type='text' and @placeholder='Login']")
        sleep(2)
        placeholder.is_displayed()

    # Наличие Placeholder в поле Password
    def test_placeholder_password(self):
        driver = webdriver.WebDriver(executable_path="../drivers/chromedriver")
        driver.get("https://stage-tody.sptech.team/auth/login")
        placeholder = driver.find_element(by=By.XPATH,
                                          value=".//input[@type='password' and @placeholder='Password']")
        sleep(2)
        placeholder.is_displayed()

    # Наличие h1 и его содержание "Tody Demos" в форме логина
    def test_h1(self):
        driver = webdriver.WebDriver(executable_path="../drivers/chromedriver")
        driver.get("https://stage-tody.sptech.team/auth/login")
        h1 = driver.find_element(by=By.XPATH,
                                 value=".//h1[@class='h1 mb-0']")
        sleep(2)
        assert h1.text == "Tody Demos"

        # user_icon = driver.find_element(by=By.XPATH, value=".//i[@class='nav-icon fas fa-user mr-1']")
        # user_icon.is_displayed()
        # """Test login form with valid value"""
        # def test_loogin(self):
        # driver = webdriver.WebDriver(executable_path="../drivers/chromedriver")
        # driver.get("https://stage-tody.sptech.team/auth/login")
        # # sleep(3)
        # login_field = driver.find_element(by=By.XPATH, value=".//input[@type='text' and @placeholder='Login']")
        # login_field.clear()
        # login_field.send_keys("Visla")
        # sleep(2)
        # password_field = driver.find_element(by=By.XPATH,
        #                                      value=".//input[@type='password' and @placeholder='Password']")
        # password_field.clear()
        # password_field.send_keys("4u4a4u4aTesl@Pu")
        # sleep(2)
        #
        # submit_button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        # submit_button.click()
        # sleep(2)
        # """Verify success login"""
        #
        # # Find user icon on main page
        # user_icon = driver.find_element(by=By.XPATH, value=".//i[@class='nav-icon fas fa-user mr-1']")
        # user_icon.is_displayed()
