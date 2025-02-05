
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
                     help="Choose browser: chrome, firefox, opera, yandex")
    parser.addoption("--base_url", action="store", default="http://192.168.0.112:8081/", help="Base URL of the application")
    parser.addoption("--executor", action="store", default="127.0.0.1")
    parser.addoption("--bv")

@pytest.fixture()
def browser(request):
    """Фикстура для инициализации веб-драйвера на основе аргументов."""
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")


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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def runtest_makereport(item):
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
