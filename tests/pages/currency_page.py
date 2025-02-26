from tests.pages.base_page import BasePage
from tests.locators import CurrencyPageLocators as Locators
from selenium.webdriver.common.by import By


class CurrencyPage(BasePage):


    def switch_currency(self):
        self.logger.info(f"Смена валюты")
        self.wait_for_element(Locators.CURRENCY_BUTTON)
        self.click(Locators.CURRENCY_BUTTON)
        self.wait_for_element(Locators.USD_CURRENCY)
        self.click(Locators.USD_CURRENCY)


    def is_currency_changed(self, expected_currency_symbol):
        """Проверка изменения валюты на странице."""
        currency_element = self.wait_for_element((By.CSS_SELECTOR, "#form-currency > div > a > strong"))
        if currency_element:
            return expected_currency_symbol in currency_element.text
        return False  # Символ валюты не найден
