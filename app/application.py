from pages.header import Header
from pages.main_page import MainPage
from pages.base_page import Page
from pages.search_results_page import SearchResultsPage
from pages.cart_result_page import CartResultPage


class Application:
    def __init__(self, driver):
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.base_page = Page(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_result_page = CartResultPage(driver)

