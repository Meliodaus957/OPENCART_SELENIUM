from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


# Таймаут для ожиданий
DEFAULT_TIMEOUT = 10


# Функция для ожидания элементов
def wait_for_element(browser, css_selector, timeout=DEFAULT_TIMEOUT):
    """Ожидание появления элемента по CSS селектору."""
    return WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
    )

# Тесты
def test_homepage_elements(browser):
    """Проверка наличия ключевых элементов на главной странице."""
    wait_for_element(browser, LOGO_SELECTOR)
    wait_for_element(browser, SEARCH_SELECTOR)
    wait_for_element(browser, PRODUCT_THUMB_SELECTOR)
    wait_for_element(browser, "a[title='Shopping Cart']")
    wait_for_element(browser, "a[title='Checkout']")


def test_catalog_elements(browser):
    """Проверка элементов страницы каталога."""
    browser.get(f"{browser.current_url}/index.php?route=product/category&path=20")
    wait_for_element(browser, "#content")
    wait_for_element(browser, PRODUCT_THUMB_SELECTOR)
    wait_for_element(browser, ".input-group")
    wait_for_element(browser, "select[name='category_id']")
    wait_for_element(browser, ".btn-primary")


def test_product_page_elements(browser):
    """Проверка элементов страницы товара."""
    browser.get(f"{browser.current_url}/index.php?route=product/product&path=57&product_id=49")
    wait_for_element(browser, BUTTON_CART_SELECTOR)
    wait_for_element(browser, ".thumbnails")
    wait_for_element(browser, PRICE_SELECTOR)
    wait_for_element(browser, "a[href='#tab-review']")
    wait_for_element(browser, "a[href='#tab-review']")


def test_admin_login_logout(browser):
    """Тест логина и разлогина в админку."""
    browser.get(f"{browser.current_url}/admin")
    username = wait_for_element(browser, ADMIN_USERNAME_SELECTOR)
    password = browser.find_element(By.CSS_SELECTOR, ADMIN_PASSWORD_SELECTOR)
    login_button = browser.find_element(By.CSS_SELECTOR, ADMIN_LOGIN_BUTTON_SELECTOR)

    username.send_keys("demo")
    password.send_keys("demo")
    login_button.click()

    wait_for_element(browser, ADMIN_LOGOUT_LINK_SELECTOR)
    browser.find_element(By.CSS_SELECTOR, ADMIN_LOGOUT_LINK_SELECTOR).click()
    wait_for_element(browser, ADMIN_USERNAME_SELECTOR)


def test_registration_page_elements(browser):
    """Проверка наличия ключевых элементов на странице регистрации."""
    # Переход на страницу регистрации
    browser.get(f"{browser.current_url}/index.php?route=account/register")

    # Проверка наличия элементов
    wait_for_element(browser, "#input-firstname")
    wait_for_element(browser, "#input-lastname")
    wait_for_element(browser, "#input-email")
    wait_for_element(browser, "#input-password")
    wait_for_element(browser, "input[name='agree']")