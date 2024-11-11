from base_page import BasePage
from tests.locators import AdminLoginPageLocators as Locators


class AdminLoginPage(BasePage):
    def login(self, username, password):
        self.enter_text(Locators.USERNAME, username)
        self.enter_text(Locators.PASSWORD, password)
        self.click(Locators.LOGIN_BUTTON)


