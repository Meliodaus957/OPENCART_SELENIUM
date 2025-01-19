from tests.pages.base_page import BasePage


class CurrencyPage(BasePage):
    CURRENCY_BUTTON = "button.btn.btn-link.dropdown-toggle"


    def switch_currency(self, currency_code):
        self.logger.info(f"Смена валюты")
        self.click(self.CURRENCY_BUTTON)
        currency_option = self.browser.find_element(By.CSS_SELECTOR, f"button[name='{currency_code}']")
        currency_option.click()


    def is_currency_changed(self, expected_currency_symbol):
        """Проверка изменения валюты на странице."""
        try:
            # Ожидаем, что на странице появится символ ожидаемой валюты
            currency_element = self.wait_for_element(".currency-symbol")
            return expected_currency_symbol in currency_element.text
        except NoSuchElementException:
            return False  # Символ валюты не найден