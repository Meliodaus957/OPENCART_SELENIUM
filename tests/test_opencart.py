import pytest
import allure
from conftest import browser, base_url
from pages.product_page import ProductPage
from pages.registration_page import RegistrationPage
from tests.pages.currency_page import CurrencyPage
from tests.pages.login_page import AdminLoginPage


@pytest.fixture()
def login_page(browser, base_url):
    return AdminLoginPage(browser, base_url)

@pytest.fixture()
def registration_page(browser, base_url):
    return RegistrationPage(browser, base_url)

@pytest.fixture()
def currency_page(browser, base_url):
    return CurrencyPage(browser, base_url)

@pytest.fixture()
def product_page(browser, base_url):
    return ProductPage(browser, base_url)



@allure.feature("Администрирование")
@allure.story("Добавление товара")
def test_add_new_product(login_page, product_page):
        login_page.open("/administration")
        login_page.login("user", "bitnami")
        product_page.add_product("iphone15promaxxcx", "meta-tagdsdddd")


@allure.feature("Администрирование")
@allure.story("Удаление товара")
def test_delete_product(login_page, product_page):
    login_page.open("/administration")
    login_page.login("user", "bitnami")
    product_page.delete_product()


@allure.feature("Сайт")
@allure.story("Регистрация пользователя")
def test_register_new_user(registration_page):
    registration_page.open("/en-gb?route=common/home")
    registration_page.register_user('Johnа', 'Doeа', 'johnа.doe@example.com', '1234567890')


@allure.feature("Сайт")
@allure.story("Смена валюты")
def test_change_currency(currency_page):
    currency_page.open("/en-gb?route=common/home")
    currency_page.switch_currency()
    currency_page.is_currency_changed('$')

