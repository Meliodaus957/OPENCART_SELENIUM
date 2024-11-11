from selenium.webdriver.common.by import By


class AdminLoginPageLocators:
    USERNAME = (By.CSS_SELECTOR, "#input-username")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    LOGOUT_LINK = (By.CSS_SELECTOR, "a[href*='logout']")


class AdminProductPageLocators:
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, "a[data-original-title='Add New']")
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, "#input-name1")
    META_TAG_INPUT = (By.CSS_SELECTOR, "#input-meta-title1")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Save']")
    PRODUCT_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox'][name*='selected']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Delete']")


class RegistrationPageLocators:
    FIRST_NAME = (By.CSS_SELECTOR, "#input-firstname")
    LAST_NAME = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    AGREE_CHECKBOX = (By.CSS_SELECTOR, "input[name='agree']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[type='submit'][value='Continue']")


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
