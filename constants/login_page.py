class LoginPageConstants:
    """Authorization"""
    URL = "https://stage-tody.sptech.team/auth/login"
    LOGIN_FIELD_XPATH = ".//input[@type='text' and @placeholder='Login']"
    PASSWORD_FIELD_XPATH = ".//input[@type='password' and @placeholder='Password']"
    SUBMIT_BUTTON_XPATH = ".//button[@type='submit']"
    ERROR_MESSAGE_TEXT = "An authentication exception occurred."
    ERROR_MESSAGE_XPATH = ".//div[@class='alert alert-danger']"
    H1_XPATH = ".//h1[@class='h1 mb-0']"
    LOGIN_VALUE = "Visla"
    PASSWORD_VALUE = "4u4a4u4aTesl@Pu"
    USER_ICON_XPATH = ".//i[@class='nav-icon fas fa-user mr-1']"