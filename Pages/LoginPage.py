from Pages.BasePage import BasePage

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    """By Locators (OR-object Repository)"""
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "LoginBtn")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")
    """-----Constructor of the Page class----------"""

    def __int__(self,driver):
        super.__init__(driver)
        self.driver.get(TestData.Base_URL)

    """---<<<<Page Actions for Login page->>>>>>-----------------------------"""
    """----this is use to get Page title-----------"""

    def get_login_page_title(self, title):
        return self.get_title(title)

    """-----this is use to check sign up link---------"""

    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    """-----this is use to login to app------------"""

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
