import pytest
import allure
from pages.admin_login_page import AdminLoginPage
from pages.admin_product_page import AdminProductPage
from pages.registration_page import RegistrationPage



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


@allure.feature("Администрирование")
@allure.story("Удаление товара")
def test_delete_product(admin_login, admin_product):
        admin_login.open("/admin")
        admin_login.login("demo", "demo")
        admin_product.delete_product()


@allure.feature("Регистрация пользователя")
@allure.story("Новый пользователь")
def test_registration_new_user(registration):
        registration.open("/index.php?route=account/register")
        registration.register_user("Pavel", "Gorodnev", "Pavel.Gorodnev@example.com", "password123")
