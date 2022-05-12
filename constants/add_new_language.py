class AddNewLanguage:
    LANGUAGES_BUTTON_XPATH = ".//a[text()='Languages']"
    LANGUAGES_NAV_BUTTON_XPATH = ".//a[@href='/language/list']"
    H3_LANGUAGES_XPATH = ".//h3[@class='card-title']"
    H3_LANGUAGES_TEXT = "Adding a new language"
    LANGUAGE_CODE_XPATH = ".//input[@id='language_code']"
    SAVE_BUTTON_XPATH = ".//button[@class='btn btn-success']"
    CHECK_STR_XPATH = "/html/body/div/div/section[2]/div/div[2]/table/tbody/tr[1]/td[2]"
    LANGUAGE_CODE_VALUE = "aaa"
