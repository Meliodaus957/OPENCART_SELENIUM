from tests.locators import AdminProductPageLocators as Locators
from tests.pages.base_page import BasePage


class AdminProductPage(BasePage):

    def add_product(self, name, meta_tag):
        self.logger.info(f"Добавление нового товара: {name}")
        self.click(Locators.ADD_PRODUCT_BUTTON)
        self.enter_text(Locators.PRODUCT_NAME_INPUT, name)
        self.enter_text(Locators.META_TAG_INPUT, meta_tag)
        self.click(Locators.SAVE_BUTTON)


    def delete_product(self):
        self.logger.info("Удаление товара")
        self.click(Locators.PRODUCT_CHECKBOX)
        self.click(Locators.DELETE_BUTTON)
        self.logger.info("Подтверждение удаления")
        self.browser.switch_to.alert.accept()


    def is_product_added(self, name):
        """Проверка, был ли товар успешно добавлен."""
        try:
            # Поиск добавленного товара по его названию
            self.wait_for_element(f"//td[text()='{name}']")
            return True  # Товар найден, значит добавлен
        except NoSuchElementException:
            return False  # Товар не найден


    def is_product_deleted(self, name):
        """Проверка, был ли товар удален."""
        try:
            # Попытка найти строку с удаленным товаром
            self.wait_for_element(f"//td[text()='{name}']")
            return False  # Товар найден, значит он не удален
        except NoSuchElementException:
            # Если товар не найден, значит он был удален
            return True