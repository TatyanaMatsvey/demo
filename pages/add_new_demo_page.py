import string
import random
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from constants.add_new_demo_page import AddNewDemoPageConstants
from pages.base import BasePage


class AddNewDemoPage(BasePage):
    '''doc'''

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = AddNewDemoPageConstants()

    def fill_fields_new_demo(self):
        # # Press button "new demo" and open Bew Demo Page
        # add_new_demo_button = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.ADD_NEW_DEMO_BUTTON)
        # add_new_demo_button.click()
        # sleep(2)

        '''Game information'''
        # find end fill demo name
        demo_name = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.DEMO_NAME_XPATH)
        demo_name.clear()
        rnd_word = f" {''.join(random.choice(string.ascii_letters) for i in range(10))}  test0 "
        demo_name.send_keys(rnd_word)

        # provider
        provider_list = self.driver.find_element(by=By.XPATH, value=".//span[@class='select2-selection__rendered']")
        provider_list.click()
        provider_choice = self.driver.find_element(by=By.XPATH,
                                                   value=".//li[@class='select2-results__option select2-results__option--highlighted']")
        provider_choice.click()

        # tags
        tags_list = self.driver.find_element(by=By.XPATH,
                                             value=".//span[@class='select2-selection select2-selection--multiple']")
        tags_list.click()
        tags_choice = self.driver.find_element(by=By.XPATH,
                                               value=".//li[@class='select2-results__option select2-results__option--highlighted']")
        tags_choice.click()

        # default language
        default_language = self.driver.find_element(by=By.XPATH, value=".//select[@id='demo_defaultLanguage']")
        default_language.click()
        default_choice = self.driver.find_element(by=By.XPATH, value="//*[@id='demo_defaultLanguage']/option[5]")
        default_choice.click()

        '''Demo Links'''
        # language choice
        language_list = self.driver.find_element(by=By.XPATH, value="//*[@id='demo_links_0_language']/option[5]")
        language_list.click()

        # language checkbox active
        active_checkbox = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.ACTIVE_CHECKBOX_XPATH)
        active_checkbox.click()

        # language checkbox Replace
        # replace_checkbox = driver.find_element(by=By.XPATH, value = ".//input[@type='checkbox' and "
        #                                                             "@id='demo_links_0_replacement']")
        # replace_checkbox.click()

        # find end fill HTML field
        HTML_field = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.HTML_FIELD_XPATH)
        HTML_field.clear()
        HTML_field.send_keys(AddNewDemoPageConstants.HTML_FIELD_VALUE)

        # find end fill Mobile HTML field
        HTML_mobile_field = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.MOBILE_HTML_FIELD_XPATH)
        HTML_mobile_field.clear()
        HTML_mobile_field.send_keys(AddNewDemoPageConstants.MOBILE_HTML_VALUE)
        sleep(1)

        '''Comment'''

        # find and fill comment field
        comment_input = self.driver.find_element(by=By.XPATH, value=".//textarea[@id='demo_comment']")
        comment_input.clear()
        comment_input.send_keys(
            f" {''.join(random.choice(string.ascii_letters) for i in range(10))} and this is the end of the comment ")

        '''Features'''
        # free spins checkbox
        free_spins = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.FREE_SPINS_XPATH)
        fs_action = ActionChains(self.driver)
        fs_action.move_to_element(free_spins)
        fs_action.click(free_spins)
        fs_action.w3c_actions.perform()

        # Risk game checkbox
        risk_game = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.RISK_GAME_XPATH)
        rg_action = ActionChains(self.driver)
        rg_action.move_to_element(risk_game)
        rg_action.click(risk_game)
        rg_action.w3c_actions.perform()

        # bonus rounds checkbox
        bonus_rounds = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.BONUS_ROUNDS_XPATH)
        br_action = ActionChains(self.driver)
        br_action.move_to_element(bonus_rounds)
        br_action.click(bonus_rounds)
        br_action.w3c_actions.perform()

        # wild symbol checkbox
        wild_symbol = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.WILD_SYMBOL_XPATH)
        ws_action = ActionChains(self.driver)
        ws_action.move_to_element(wild_symbol)
        ws_action.click(wild_symbol)
        ws_action.w3c_actions.perform()

        # sounds checkbox
        sound = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.SOUND_XPATH)
        s_action = ActionChains(self.driver)
        s_action.move_to_element(sound)
        s_action.click(sound)
        s_action.w3c_actions.perform()

        # auto game checkbox
        auto_game = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.AUTO_GAME_XPATH)
        ag_action = ActionChains(self.driver)
        ag_action.move_to_element(auto_game)
        ag_action.click(auto_game)
        ag_action.w3c_actions.perform()

        # scatter symbol checkbox
        scatter_symbol = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.SCATTER_SYMBOL_XPATH)
        ss_action = ActionChains(self.driver)
        ss_action.move_to_element(scatter_symbol)
        ss_action.click(scatter_symbol)
        ss_action.w3c_actions.perform()

        # multiplier checkbox
        multiplier = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.MULTIPLIER_XPATH)
        m_action = ActionChains(self.driver)
        m_action.move_to_element(multiplier)
        m_action.click(multiplier)
        m_action.w3c_actions.perform()

        # find and fill reals amount field
        reals_amount = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.REELS_AMOUNT_XPATH)
        reals_amount.clear()
        reals_amount.send_keys(random.randint(1, 99))

        # find and fill min rate field
        min_rate = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.MIN_RATE_XPATH)
        min_rate.clear()
        min_rate.send_keys(random.randint(1, 99))

        # find and fill RTP field
        RTP = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.RTP_XPATH)
        RTP.clear()
        RTP.send_keys(random.randint(1, 99))

        # find and fill Lines amount field
        lines_amount = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.LINES_AMOUNT_XPATH)
        lines_amount.clear()
        lines_amount.send_keys(random.randint(1, 99))

        # find and fill Max rate field
        max_rate = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.MAX_RATE_XPATH)
        max_rate.clear()
        max_rate.send_keys(random.randint(1, 99))

        # find and fill Jackpot field
        jackpot = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.JACKPOT_XPATH)
        jackpot.clear()
        jackpot.send_keys(random.randint(1, 99))

        # find and fill POPULARITY field
        popularity = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.POPULARITY_XPATH)
        popularity.clear()
        popularity.send_keys(random.randint(1, 10))

        # # find and fill Release Date field
        # release = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.RELEASE_DATE_XPATH)
        # release.clear()
        # release.send_keys(25122023)
        # sleep(3)

        '''Images'''
        # browse select logo
        logo_select_file = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.LOGO_SELECT_FILE_XPATH)
        logo_select_file.send_keys(AddNewDemoPageConstants.SCREENSHOT_XPATH)
        sleep(4)

        '''Screenshots'''
        # browse screenshot
        screenshots = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.SCREENSHOTS_SELECT_FILE_XPATH)
        screenshots.send_keys(AddNewDemoPageConstants.SCREENSHOT_XPATH)
        sleep(4)

        save_button = self.driver.find_element(by=By.XPATH, value=AddNewDemoPageConstants.SAVE_BUTTON_XPATH)
        save_button.click()
        sleep(2)

    def verify_message(self):
        success_message = self.driver.find_element(by=By.XPATH, value=".//h5")
        assert success_message.text == AddNewDemoPageConstants.SUCCESS_MESSAGE_TEXT, "Сообщение об успешном создании " \
                                                                                     "демки не подтверждено "
