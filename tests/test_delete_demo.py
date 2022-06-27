import random
import string
from telnetlib import EC
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from constants.add_new_demo_page import AddNewDemoPageConstants
from constants.base import BaseConstants
from constants.login_page import LoginPageConstants
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class TestDeleteDemo:
    """Positive test to delete demo:
    - Authorization on Tody
    - Go to ADD NEW DEMO page
    - Create new demo named 'Testing'
    - Find new demo 'Testing' on demo list
    - Open Edit page
    - Delete 'Testing' demo
    - Check Demo List, 'Testing' demo not exist """

    def test_delete_demo(self):
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

        # Press button "new demo" and open Bew Demo Page
        add_new_demo_button = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.ADD_NEW_DEMO_BUTTON)
        add_new_demo_button.click()
        sleep(2)

        '''Game information'''
        # find end fill demo name
        demo_name = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.DEMO_NAME_XPATH)
        demo_name.clear()
        demo_name.send_keys("Testing")

        '''Demo Links'''
        # language checkbox active
        active_checkbox = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.ACTIVE_CHECKBOX_XPATH)
        active_checkbox.click()

        # language checkbox Replace
        # replace_checkbox = driver.find_element(by=By.XPATH, value = ".//input[@type='checkbox' and "
        #                                                             "@id='demo_links_0_replacement']")
        # replace_checkbox.click()

        # find end fill HTML field
        HTML_field = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.HTML_FIELD_XPATH)
        HTML_field.clear()
        HTML_field.send_keys(AddNewDemoPageConstants.HTML_FIELD_VALUE)

        # find end fill Mobile HTML field
        HTML_mobile_field = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.MOBILE_HTML_FIELD_XPATH)
        HTML_mobile_field.clear()
        HTML_mobile_field.send_keys(AddNewDemoPageConstants.MOBILE_HTML_VALUE)
        sleep(1)

        '''Features'''
        # free spins checkbox
        free_spins = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.FREE_SPINS_XPATH)
        fs_action = ActionChains(driver)
        fs_action.move_to_element(free_spins)
        fs_action.click(free_spins)
        fs_action.w3c_actions.perform()

        # Risk game checkbox
        risk_game = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.RISK_GAME_XPATH)
        rg_action = ActionChains(driver)
        rg_action.move_to_element(risk_game)
        rg_action.click(risk_game)
        rg_action.w3c_actions.perform()

        # bonus rounds checkbox
        bonus_rounds = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.BONUS_ROUNDS_XPATH)
        br_action = ActionChains(driver)
        br_action.move_to_element(bonus_rounds)
        br_action.click(bonus_rounds)
        br_action.w3c_actions.perform()

        # wild symbol checkbox
        wild_symbol = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.WILD_SYMBOL_XPATH)
        ws_action = ActionChains(driver)
        ws_action.move_to_element(wild_symbol)
        ws_action.click(wild_symbol)
        ws_action.w3c_actions.perform()

        # sounds checkbox
        sound = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.SOUND_XPATH)
        s_action = ActionChains(driver)
        s_action.move_to_element(sound)
        s_action.click(sound)
        s_action.w3c_actions.perform()

        # auto game checkbox
        auto_game = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.AUTO_GAME_XPATH)
        ag_action = ActionChains(driver)
        ag_action.move_to_element(auto_game)
        ag_action.click(auto_game)
        ag_action.w3c_actions.perform()

        # scatter symbol checkbox
        scatter_symbol = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.SCATTER_SYMBOL_XPATH)
        ss_action = ActionChains(driver)
        ss_action.move_to_element(scatter_symbol)
        ss_action.click(scatter_symbol)
        ss_action.w3c_actions.perform()

        # multiplier checkbox
        multiplier = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.MULTIPLIER_XPATH)
        m_action = ActionChains(driver)
        m_action.move_to_element(multiplier)
        m_action.click(multiplier)
        m_action.w3c_actions.perform()

        # find and fill reals amount field
        reals_amount = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.REELS_AMOUNT_XPATH)
        reals_amount.clear()
        reals_amount.send_keys(random.randint(1, 99))

        # find and fill min rate field
        min_rate = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.MIN_RATE_XPATH)
        min_rate.clear()
        min_rate.send_keys(random.randint(1, 99))

        # find and fill RTP field
        RTP = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.RTP_XPATH)
        RTP.clear()
        RTP.send_keys(random.randint(1, 99))

        # find and fill Lines amount field
        lines_amount = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.LINES_AMOUNT_XPATH)
        lines_amount.clear()
        lines_amount.send_keys(random.randint(1, 99))

        # find and fill Max rate field
        max_rate = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.MAX_RATE_XPATH)
        max_rate.clear()
        max_rate.send_keys(random.randint(1, 99))

        # find and fill Jackpot field
        jackpot = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.JACKPOT_XPATH)
        jackpot.clear()
        jackpot.send_keys(random.randint(1, 99))

        # find and fill POPULARITY field
        popularity = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.POPULARITY_XPATH)
        popularity.clear()
        popularity.send_keys(random.randint(1, 10))

        # find and fill Release Date field
        release = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.RELEASE_DATE_XPATH)
        release.clear()
        release.send_keys(14121994)
        sleep(3)

        '''Images'''
        # browse select logo
        logo_select_file = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.LOGO_SELECT_FILE_XPATH)
        logo_select_file.send_keys(AddNewDemoPageConstants.SCREENSHOT_XPATH)
        sleep(4)

        '''Screenshots'''
        # browse screenshot
        screenshots = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.SCREENSHOTS_SELECT_FILE_XPATH)
        screenshots.send_keys(AddNewDemoPageConstants.SCREENSHOT_XPATH)
        sleep(4)

        save_button = driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.SAVE_BUTTON_XPATH)
        save_button.click()
        sleep(2)

        success_message = driver.find_element(by=By.XPATH, value=".//h5")
        assert success_message.text == AddNewDemoPageConstants.SUCCESS_MESSAGE_TEXT, "Сообщение об успешном создании демки не подтверждено"

        # go to demo list
        demos_button = driver.find_element(by=By.XPATH, value=".//a[@href='/demo/list']")
        demos_button.click()

        # search first name in table demo list and see that demo @deleted@ is real
        first_demo_title = driver.find_element(by=By.XPATH,
                                               value="/html/body/div/div/section[2]/div/div[2]/table/tbody/tr[1]/td[2]/a")
        compare = first_demo_title.text[0:7]
        assert compare == "Testing", "no match"

        '''part 3
        - go to edit page
        - delete new adding demo with name Testing
        - see, that Testing demo not exist'''

        # find edit button for first cell in table (Testing demo)
        edit_button = driver.find_element(by=By.XPATH,
                                          value="/html/body/div/div/section[2]/div/div[2]/table/tbody/tr[1]/td[12]/a/i")
        edit_button.click()
        sleep(3)

        new_tab = driver.switch_to.window(driver.window_handles[1])
        sleep(3)

        delete_button = driver.find_element(by=By.XPATH, value=".//a[@class='btn btn-danger']")
        delete_button.click()
        sleep(5)

        accept_ok = driver.switch_to.alert.accept()
        sleep(5)

        first_demo_title = driver.find_element(by=By.XPATH,
                                               value="/html/body/div/div/section[2]/div/div[2]/table/tbody/tr[1]/td[2]/a")
        compare = first_demo_title.text[0:7]
        assert compare != "Testing", "not deleted"

        driver.close()
