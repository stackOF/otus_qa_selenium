import pytest
from pages.main_page import MainPage


@pytest.mark.elements
def test_elements_main_page(browser, url):
    page = MainPage(browser)
    page.open_page(url)
    page.should_be_main_navbar()
    page.should_be_navbar_btn()
    page.should_be_search_btn()
    page.should_be_search_input()
    page.should_br_banners()


def test_change_currency(browser, url):
    page = MainPage(browser)
    page.open_page(url)
    page.change_currency_to_usd()
    page.check_currency_usd()
