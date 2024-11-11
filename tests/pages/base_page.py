import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, base_url="http://localhost"):
        self.browser = browser
        self.base_url = base_url

    def open(self, url=""):
        full_url = f"{self.base_url}{url}"
        logging.info(f"Opening URL: {full_url}")
        self.browser.get(full_url)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        logging.info(f"Clicking on element: {locator}")
        self.wait_for_element(locator).click()

    def enter_text(self, locator, text):
        logging.info(f"Entering text into element {locator}: {text}")
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

