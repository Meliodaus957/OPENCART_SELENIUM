import allure
import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from datetime import datetime

def pytest_addoption(parser):
    """Добавление опций командной строки для pytest."""
    parser.addoption("--browser", action="store", default="chrome",
                     help="Choose browser: chrome, firefox")
    parser.addoption("--base_url", action="store", default="http://192.168.0.112:8081/",
                     help="Base URL of the application")
    parser.addoption("--executor", action="store", default="selenoid")
    parser.addoption("--bv")

@pytest.fixture()
def base_url(request):
    """Фикстура для получения base_url из параметров pytest"""
    return request.config.getoption("--base_url")

@pytest.fixture()
def browser(request, base_url):
    """Фикстура для инициализации веб-драйвера на основе аргументов."""
    browser_name = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")

    executor_url = f"http://{executor}:4444/wd/hub"

    # Инициализация драйвера на основе выбора браузера
    if browser_name == "chrome":
        options = ChromeOptions()
    elif browser_name == "firefox":
        options = FirefoxOptions()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    caps = {
        "browserName": browser_name,
        "browserVersion": version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    for k, v in caps.items():
        options.set_capability(k, v)

    browser = webdriver.Remote(
        command_executor=executor_url,
        options=options
    )

    browser.maximize_window()
    browser.get(base_url)  # Теперь browser открывает страницу с base_url

    yield browser

    browser.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    # Хук для проверки статуса каждого теста
    outcome = yield
    result = outcome.get_result()
    setattr(item, "rep_" + result.when, result)

@pytest.fixture(autouse=True)
def screenshot_on_failure(request, browser):
    """Снимает скриншот при падении теста и добавляет в отчёт Allure"""
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        if browser:
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            screenshot_name = f"screenshot_{timestamp}.png"
            screenshot_path = os.path.join("allure-results", screenshot_name)

            os.makedirs("allure-results", exist_ok=True)
            browser.save_screenshot(screenshot_path)
            allure.attach.file(screenshot_path, name="Ошибка - скриншот", attachment_type=allure.attachment_type.PNG)
