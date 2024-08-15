from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class CartResultPage(Page):
    CART_TEXT = (By.XPATH, "//div[@data-test='boxEmptyMsg']")

    def verify_cart_result(self):
        actual_text = self.driver.find_element(*self.CART_TEXT).text
        assert actual_text == 'Your cart is empty', f'Expected "Your cart is empty" did not match actual {actual_text}'