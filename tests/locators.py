from selenium.webdriver.common.by import By


class AdminLoginPageLocators:
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#form-login > div.text-end > button")
    LOGOUT_LINK = (By.CSS_SELECTOR, "a[href*='logout']")


class AdminProductPageLocators:
    CATALOG = (By.ID, 'menu-catalog')
    PRODUCTS = (By.LINK_TEXT, 'Products')
    PRODUCT_CHECKBOX = (By.CSS_SELECTOR, "#form-product > div.table-responsive > table > tbody > tr:nth-child(3) > td:nth-child(1) > input")
    DELETE_BUTTON = (By.CSS_SELECTOR, "#content > div.page-header > div > div > button.btn.btn-danger")
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, "#content > div.page-header > div > div > a")
    PRODUCT_NAME_INPUT = (By.ID, "input-name-1")
    META_TAG_INPUT = (By.ID, "input-meta-title-1")
    DATA = (By.LINK_TEXT, 'Data')
    MODEL = (By.ID, "input-model")
    SEO = (By.LINK_TEXT, 'SEO')
    KEYWORD = (By.NAME, "product_seo_url[0][1]")
    SAVE_BUTTON = (By.CSS_SELECTOR, '#content > div.page-header > div > div > button')
    SUCCESS_ALERT = (By.CSS_SELECTOR, "#alert > div")

class RegistrationPageLocators:
    MY_ACCOUNT = (By.CSS_SELECTOR, "#top > div > div.nav.float-end > ul > li:nth-child(2) > div > a")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#top > div > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(1) > a")
    FIRST_NAME = (By.CSS_SELECTOR, "#input-firstname")
    LAST_NAME = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    AGREE_CHECKBOX = (By.CSS_SELECTOR, "input[name='agree']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#form-register > div > button")
    CONTINUE_BUTTON_SECOND = (By.CSS_SELECTOR, "#content > div > a")
    LOGOUT = (By.CSS_SELECTOR, "#column-right > div > a:nth-child(13)")


class HomePageLocators:
    LOGO_SELECTOR = (By.CSS_SELECTOR, "#logo a")
    SEARCH_SELECTOR = (By.CSS_SELECTOR, "input[name='search']")
    PRODUCT_THUMB_SELECTOR = (By.CSS_SELECTOR, ".product-thumb")
    SHOPPING_CART_LINK = (By.CSS_SELECTOR, "a[title='Shopping Cart']")
    CHECKOUT_LINK = (By.CSS_SELECTOR, "a[title='Checkout']")


class CatalogPageLocators:
    CONTENT = (By.CSS_SELECTOR, "#content")
    PRODUCT_THUMB_SELECTOR = (By.CSS_SELECTOR, ".product-thumb")
    INPUT_GROUP = (By.CSS_SELECTOR, ".input-group")
    CATEGORY_DROPDOWN = (By.CSS_SELECTOR, "select[name='category_id']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".btn-primary")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    THUMBNAILS = (By.CSS_SELECTOR, ".thumbnails")
    PRICE = (By.CSS_SELECTOR, ".price")
    REVIEW_TAB = (By.CSS_SELECTOR, "a[href='#tab-review']")


class CurrencyPageLocators:
    CURRENCY_BUTTON = (By.CSS_SELECTOR, "#form-currency")
    USD_CURRENCY = (By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(3)")