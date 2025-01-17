import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import allure
from datetime import datetime

YANDEX_BROWSER_PATH = "/Applications/Opera\ Opera.app"
OPERA_BROWSER_PATH = "/Applications/Yandex\ Yandex.app"


def pytest_addoption(parser):
    """Добавление опций командной строки для pytest."""
    parser.addoption("--browser", action="store", default="chrome",
                     help="Choose browser: chrome, firefox, opera, yandex")
    parser.addoption("--base_url", action="store", default="http://localhost", help="Base URL of the application")


@pytest.fixture(scope='session')
def browser(request):
    """Фикстура для инициализации веб-драйвера на основе аргументов."""
    browser_choice = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")

    # Инициализация драйвера на основе выбранного браузера
    driver = _initialize_browser(browser_choice)

    driver.maximize_window()
    driver.get(base_url)

    yield driver
    driver.quit()


def _initialize_browser(browser_choice):
    """Инициализация веб-драйвера на основе выбора браузера."""
    if browser_choice == "chrome":
        chrome_options = ChromeOptions()
        return chrome_options
    elif browser_choice == "firefox":
        firefox_options = FirefoxOptions()
        return firefox_options
    elif browser_choice == "opera":
        chrome_options = ChromeOptions()
        chrome_options.binary_location = OPERA_BROWSER_PATH
        return chrome_options
    elif browser_choice == "yandex":
        chrome_options = ChromeOptions()
        chrome_options.binary_location = YANDEX_BROWSER_PATH
        return chrome_options
    else:
        raise ValueError(f"Unsupported browser: {browser_choice}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Хук для проверки статуса каждого теста
    outcome = yield
    result = outcome.get_result()
    setattr(item, "rep_" + result.when, result)

@pytest.fixture(autouse=True)
def screenshot_on_failure(request, browser):
    yield
    # Проверка, был ли тест неудачным
    if request.node.rep_call.failed:
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_name = f"screenshot_{timestamp}.png"
        browser.save_screenshot(screenshot_name)
        allure.attach.file(screenshot_name, name="Ошибка - скриншот", attachment_type=allure.attachment_type.PNG)
