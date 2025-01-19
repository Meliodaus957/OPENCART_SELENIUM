import pytest
import allure
from tests.pages.admin_product_page import AdminProductPage
from tests.pages.registration_page import RegistrationPage
from tests.pages.admin_login_page import AdminLoginPage


@pytest.fixture
def admin_login(browser):
    return AdminLoginPage(browser)


@pytest.fixture
def admin_product(browser):
    return AdminProductPage(browser)


@pytest.fixture
def registration(browser):
    return RegistrationPage(browser)


@allure.feature("Администрирование")
@allure.story("Добавление товара")
def test_add_new_product(admin_login, admin_product):
        admin_login.open("/admin")
        admin_login.login("test", "test")
        admin_product.add_product("Test Product", "Meta Test")
        assert admin_product.is_product_added("Test Product"), "Продукт не был добавлен в список!"


@allure.feature("Администрирование")
@allure.story("Удаление товара")
def test_delete_product(admin_login, admin_product):
        admin_login.open("/admin")
        admin_login.login("demo", "demo")
        admin_product.delete_product()
        assert admin_product.is_product_deleted("Test Product"), "Продукт не был удален!"


@allure.feature("Регистрация пользователя")
@allure.story("Новый пользователь")
def test_registration_new_user(registration):
        registration.open("/index.php?route=account/register")
        registration.register_user("Pavel", "Gorodnev", "Pavel.Gorodnev@example.com", "password123")
        assert registration.is_registration_successful(), "Регистрация не прошла успешно!"
