from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART = (By.XPATH, "//div[@data-test='@web/CartIcon']")

    def search(self):
        self.input_text('coffee', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def go_to_carts(self):
        self.click(*self.CART)



