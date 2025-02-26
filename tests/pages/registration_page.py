from tests.locators import RegistrationPageLocators as Locators
from tests.pages.base_page import BasePage


class RegistrationPage(BasePage):
    def register_user(self, first_name, last_name, email, password):
        # self.logger.info("Выход из аккаунта")
        # self.click(Locators.LOGOUT)
        self.logger.info(f"Регистрация пользователя: {first_name} {last_name}")
        self.wait_for_element(Locators.MY_ACCOUNT)
        self.click(Locators.MY_ACCOUNT)
        self.wait_for_element(Locators.REGISTER_BUTTON)
        self.click(Locators.REGISTER_BUTTON)
        self.wait_for_element(Locators.FIRST_NAME)
        self.enter_text(Locators.FIRST_NAME, first_name)
        self.enter_text(Locators.LAST_NAME, last_name)
        self.enter_text(Locators.EMAIL, email)
        self.enter_text(Locators.PASSWORD, password)
        self.click(Locators.AGREE_CHECKBOX)
        self.click(Locators.CONTINUE_BUTTON)
        self.click(Locators.MY_ACCOUNT)
        self.wait_for_element(Locators.LOGOUT)
        self.click(Locators.LOGOUT)

    # def is_registration_successful(self):
    #     """Проверка успешной регистрации."""
    #     try:
    #         # Проверка наличия сообщения об успешной регистрации
    #         success_message = self.wait_for_element(".alert-success")
    #         return "Your Account Has Been Created!" in success_message.text
    #     except NoSuchElementException:
    #         return False  # Сообщение не найдено, значит регистрация не прошла