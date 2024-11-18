from base_page import BasePage
from tests.locators import RegistrationPageLocators as Locators


class RegistrationPage(BasePage):
    def register_user(self, first_name, last_name, email, password):
        self.logger.info(f"Регистрация пользователя: {first_name} {last_name}")
        self.enter_text(Locators.FIRST_NAME, first_name)
        self.enter_text(Locators.LAST_NAME, last_name)
        self.enter_text(Locators.EMAIL, email)
        self.enter_text(Locators.PASSWORD, password)
        self.click(Locators.AGREE_CHECKBOX)
        self.click(Locators.CONTINUE_BUTTON)

