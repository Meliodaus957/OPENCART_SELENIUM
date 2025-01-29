import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, base_url="192.168.0.112:8081"):
        self.browser = browser
        self.base_url = base_url
        self.logger = logging.getLogger(self.__class__.__name__)
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def open(self, url):
        full_url = f"{self.base_url}{url}"
        logging.info(f"Открытие страницы: {full_url}")
        self.browser.get(full_url)

    def wait_for_element(self, locator, timeout=10):
        logging.info(f"Ожидание элемента: {locator}")
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        logging.info(f"Клик по элементу: {locator}")
        self.wait_for_element(locator).click()

    def enter_text(self, locator, text):
        logging.info(f"Ввод текста в элемент {locator}: {text}")
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

