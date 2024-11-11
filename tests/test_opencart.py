import pytest
import allure
from logger import setup_logger
from pages.admin_login_page import AdminLoginPage
from pages.admin_product_page import AdminProductPage
from pages.registration_page import RegistrationPage

logger = setup_logger()


@pytest.fixture
def admin_login(browser):
    return AdminLoginPage(browser)


@pytest.fixture
def admin_product(browser):
    return AdminProductPage(browser)


@pytest.fixture
def registration(browser):
    return RegistrationPage(browser)


@allure.feature("Admin Panel")
@allure.story("Add New Product")
def test_add_new_product(admin_login, admin_product):
    logger.info("Открытие страницы логина администратора")
    with allure.step("Open admin login page and login"):
        admin_login.open("/admin")
        admin_login.login("test", "test")
    with allure.step("Add a new product"):
        admin_product.add_product("Test Product", "Meta Test")
        logger.info("Добавлен новый продукт 'Test Product'")


@allure.feature("Admin Panel")
@allure.story("Delete Product")
def test_delete_product(admin_login, admin_product):
    logger.info("Открытие страницы логина администратора для удаления продукта")
    with allure.step("Open admin login page and login"):
        admin_login.open("/admin")
        admin_login.login("demo", "demo")
    with allure.step("Delete an existing product"):
        admin_product.delete_product()
        logger.info("Продукт успешно удален")


@allure.feature("User Registration")
@allure.story("Register New User")
def test_registration_new_user(registration):
    logger.info("Открытие страницы регистрации")
    with allure.step("Open user registration page"):
        registration.open("/index.php?route=account/register")
    with allure.step("Register new user"):
        registration.register_user("Pavel", "Gorodnev", "Pavel.Gorodnev@example.com", "password123")
        logger.info("Регистрация нового пользователя: Pavel Gorodnev")
