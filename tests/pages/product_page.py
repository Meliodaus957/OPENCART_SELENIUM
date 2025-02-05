from tests.locators import AdminProductPageLocators as Locators
from tests.pages.base_page import BasePage

class ProductPage(BasePage):
    def add_product(self, name, meta_tag):
        self.wait_for_element(Locators.CATALOG)
        self.click(Locators.CATALOG)
        self.wait_for_element(Locators.PRODUCTS)
        self.click(Locators.PRODUCTS)
        self.wait_for_element(Locators.ADD_PRODUCT_BUTTON)
        self.click(Locators.ADD_PRODUCT_BUTTON)
        self.wait_for_element(Locators.PRODUCT_NAME_INPUT)
        self.enter_text(Locators.PRODUCT_NAME_INPUT, name)
        self.wait_for_element(Locators.META_TAG_INPUT)
        self.enter_text(Locators.META_TAG_INPUT, name)
        self.wait_for_element(Locators.DATA)
        self.click(Locators.DATA)
        self.wait_for_element(Locators.MODEL)
        self.enter_text(Locators.MODEL, name)
        self.wait_for_element(Locators.SEO).click()
        self.wait_for_element(Locators.KEYWORD)
        self.enter_text(Locators.KEYWORD, name)
        self.wait_for_element(Locators.SAVE_BUTTON)
        self.click(Locators.SAVE_BUTTON)


    def delete_product(self):
        self.wait_for_element(Locators.CATALOG)
        self.click(Locators.CATALOG)
        self.wait_for_element(Locators.PRODUCTS)
        self.click(Locators.PRODUCTS)
        self.wait_for_element(Locators.PRODUCT_CHECKBOX)
        self.click(Locators.PRODUCT_CHECKBOX)
        self.click(Locators.DELETE_BUTTON)
        self.for_element_alert_accept()
