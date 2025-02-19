import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    def __init__(self, browser, base_url="http://opencart:8080"):
        self.browser = browser
        self.base_url = base_url
        self.wait = WebDriverWait(self.browser, 15)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)


    def open(self, url):
        """Открытие страницы по URL."""
        full_url = f"{self.base_url}{url}"
        self.logger.info(f"Открытие страницы: {full_url}")
        self.browser.get(full_url)


    def wait_for_element(self, locator, timeout=10):
        """Ожидание появления элемента на странице."""
        try:
            self.logger.info(f"Ожидание элемента: {locator}")
            return WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            self.logger.error(f"Элемент {locator} не найден за {timeout} секунд")
            return None


    def click(self, locator):
        """Клик по элементу."""
        element = self.wait_for_element(locator)
        if element:
            self.logger.info(f"Клик по элементу: {locator}")
            element.click()
        else:
            self.logger.warning(f"Не удалось кликнуть по элементу: {locator} (Элемент не найден)")


    def enter_text(self, locator, text):
        """Ввод текста в поле."""
        element = self.wait_for_element(locator)
        if element:
            self.logger.info(f"Ввод текста в элемент {locator}: {text}")
            element.clear()
            element.send_keys(text)
        else:
            self.logger.warning(f"Не удалось ввести текст в элемент {locator} (Элемент не найден)")


    def for_element_alert_accept(self):
        alert = WebDriverWait(self.browser, timeout=10).until(EC.alert_is_present())
        print(alert.text)
        alert.accept()

    def for_element_alert_dismiss(self):
        alert = WebDriverWait(self.browser, timeout=10).until(EC.alert_is_present())
        print(alert.text)
        alert.dismiss()