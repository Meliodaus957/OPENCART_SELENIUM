from base_page import BasePage
from tests.locators import AdminProductPageLocators as Locators


class AdminProductPage(BasePage):
    def add_product(self, name, meta_tag):
        self.click(Locators.ADD_PRODUCT_BUTTON)
        self.enter_text(Locators.PRODUCT_NAME_INPUT, name)
        self.enter_text(Locators.META_TAG_INPUT, meta_tag)
        self.click(Locators.SAVE_BUTTON)

    def delete_product(self):
        self.click(Locators.PRODUCT_CHECKBOX)
        self.click(Locators.DELETE_BUTTON)
        self.browser.switch_to.alert.accept()
