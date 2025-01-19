from base_page import BasePage


class CurrencyPage(BasePage):
    CURRENCY_BUTTON = "button.btn.btn-link.dropdown-toggle"


    def switch_currency(self, currency_code):
        self.logger.info(f"Смена валюты")
        self.click(self.CURRENCY_BUTTON)
        currency_option = self.browser.find_element(By.CSS_SELECTOR, f"button[name='{currency_code}']")
        currency_option.click()
