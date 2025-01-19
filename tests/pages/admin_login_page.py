
from tests.locators import AdminLoginPageLocators as Locators
from tests.pages.base_page import BasePage


class AdminLoginPage(BasePage):
    def login(self, username, password):
        self.logger.info("Вход в административную панель")
        self.enter_text(Locators.USERNAME, username)
        self.enter_text(Locators.PASSWORD, password)
        self.click(Locators.LOGIN_BUTTON)


