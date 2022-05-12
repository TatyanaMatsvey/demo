class AddNewDemoPageConstants:
    URL = "https://stage-tody.sptech.team/demo/add"

    ADD_NEW_DEMO_BUTTON = ".//a[@href='/demo/add']"

    INPUT_DEMO_NAME_FIELD_XPATH = ".//input[@type='text' and @id='demo_demoName']"
    PROVIDER_LIST_XPATH = ".//select[@id='demo_provider']"
    PROVIDER_EVOPLAY_XPATH = ".//option[@value='8']"
    DEMOS_TAGS_XPATH = ".//span[@class='select2-selection select2-selection--multiple']"
    DEFAULT_LANGUAGE_SELECT_XPATH = ".//select[@id='demo_defaultLanguage']"
    SELECT_LANGUAGE_DE_XPATH = ".//option[@value=3 and text()='DE']"

    """GAME INFORMATION"""
    DEMO_NAME_XPATH = ".//input[@type='text' and @id='demo_demoName']"
    LANGUAGE_XPATH = ".//select[@id='demo_links_0_language']"
    ACTIVE_CHECKBOX_XPATH = ".//input[@type='checkbox' and @id='demo_links_0_isActive']"
    REPLACE_CHECKBOX_XPATH = ".//input[@type='checkbox' and @id='demo_links_0_replacement']"
    HTML_FIELD_XPATH = ".//textarea[@id='demo_links_0_html']"
    HTML_FIELD_VALUE = "HTML FIELD Test text test text test text"
    MOBILE_HTML_FIELD_XPATH = ".//textarea[@id='demo_links_0_mobileHtml']"
    MOBILE_HTML_VALUE = "HTML mobile field test text"

    """FEATURES"""
    #
    FREE_SPINS_XPATH = ".//input[@type='checkbox' and @id='demo_freeSpins']"
    RISK_GAME_XPATH = ".//input[@type='checkbox' and @id='demo_riskGame']"
    SOUND_XPATH = ".//input[@type='checkbox' and @id='demo_sound']"
    AUTO_GAME_XPATH = ".//input[@type='checkbox' and @id='demo_autoGame']"
    BONUS_ROUNDS_XPATH = ".//input[@type='checkbox' and @id='demo_bonusRounds']"
    SCATTER_SYMBOL_XPATH = ".//input[@type='checkbox' and @id='demo_scatterSymbol']"
    WILD_SYMBOL_XPATH = ".//input[@type='checkbox' and @id='demo_wildSymbol']"
    MULTIPLIER_XPATH = ".//input[@type='checkbox' and @id='demo_multiplier']"

    REELS_AMOUNT_XPATH = ".//input[@id='demo_drumsAmount']"
    MIN_RATE_XPATH = ".//input[@id='demo_minRate']"
    RTP_XPATH = ".//input[@id='demo_rtp']"
    LINES_AMOUNT_XPATH = ".//input[@id='demo_linesAmount']"
    MAX_RATE_XPATH = ".//input[@id='demo_maxRate']"
    JACKPOT_XPATH = ".//input[@id='demo_jackpot']"
    POPULARITY_XPATH = ".//input[@id='demo_popularity']"
    RELEASE_DATE_XPATH = ".//input[@id='demo_releaseDate']"

    LOGO_SELECT_FILE_XPATH = ".//input[@type='file' and @id='demo_logos']"
    SCREENSHOTS_SELECT_FILE_XPATH = ".//input[@type='file' and @id='demo_screenshots']"
    SCREENSHOT_XPATH = "/home/visla/PycharmProjects/demo/download.jpeg"

    SAVE_BUTTON_XPATH = ".//button[@class='btn btn-success']"
    TO_LIST_BUTTON_XPATH = ".//a[@class='btn btn-primary ml-2']"

    SUCCESS_MESSAGE_XPATH = ".//div[@class='alert alert-success alert-dismissible']"
    SUCCESS_MESSAGE_TEXT = "Success!"
