from tests.locators import AdminLoginPageLocators as Locators
from tests.pages.base_page import BasePage



class AdminLoginPage(BasePage):
    def login(self, username, password):
        self.logger.info("Вход в административную панель")
        self.wait_for_element(Locators.USERNAME).send_keys(username)
        self.wait_for_element(Locators.PASSWORD).send_keys(password)
        self.click(Locators.LOGIN_BUTTON)