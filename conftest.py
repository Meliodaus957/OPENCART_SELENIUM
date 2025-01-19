import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


import allure
from datetime import datetime


def pytest_addoption(parser):
    """Добавление опций командной строки для pytest."""
    parser.addoption("--browser", action="store", default="chrome",
                     help="Choose browser: chrome, firefox")
    parser.addoption("--base_url", action="store", default="http://127.0.0.1", help="Base URL of the application")
    parser.addoption("--executor", action="store", default="http://127.0.0.1", help="Base URL of the selenoid")


@pytest.fixture(scope='session')
def browser(request):
    """Фикстура для инициализации веб-драйвера на основе аргументов."""
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")
    executor = request.config.getoption("--executor")

    selenoid_url = f"{executor}:4444/wd/hub"

    """Инициализация веб-драйвера на основе выбора браузера."""
    if browser == "chrome":
       options = ChromeOptions()
    elif browser == "firefox":
       options = FirefoxOptions()
    else:
        raise ValueError(f"Unsupported browser: {browser}")


    caps = {
        "browserName": browser
    }

    for k, v in caps.items():
        options.set_capability(k, v)


    # Инициализация драйвера на основе выбранного браузера
    driver = webdriver.Remote(
        command_executor=selenoid_url,
        options=options
    )

    driver.maximize_window()
    driver.get(base_url)
    yield driver
    driver.quit()


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
