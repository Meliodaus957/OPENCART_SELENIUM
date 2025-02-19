
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions



def pytest_addoption(parser):
    """Добавление опций командной строки для pytest."""
    parser.addoption("--browser", action="store", default="chrome",
                     help="Choose browser: chrome, firefox")
    parser.addoption("--base_url", action="store", default="http://192.168.0.112:8081/", help="Base URL of the application")
    parser.addoption("--executor", action="store", default="host.docker.internal")
    parser.addoption("--bv")



@pytest.fixture()
def browser(request):
    """Фикстура для инициализации веб-драйвера на основе аргументов."""
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    base_url = request.config.getoption("--base_url")

    executor_url = f"http://{executor}:4444/wd/hub"


    """Инициализация веб-драйвера на основе выбора браузера."""
    if browser == "chrome":
       options = ChromeOptions()
    elif browser == "firefox":
       options = FirefoxOptions()
    else:
        raise ValueError(f"Unsupported browser: {browser}")


    caps = {
        "browserName": browser,
        "browserVersion": version,
        "selenoid:options": {
             "enableVNC": True,
             "enableVideo": False
         }
    }

    for k, v in caps.items():
        options.set_capability(k, v)


    # Инициализация драйвера на основе выбранного браузера
    browser = webdriver.Remote(
        command_executor=executor_url,
        options=options
    )

    browser.maximize_window()
    browser.get(base_url)

    yield browser

    browser.quit()



