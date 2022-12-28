import pytest
from pages.main_page import MainPage


@pytest.mark.elements
def test_elements_main_page(browser, url):
    MainPage(browser).open_page(url)
    MainPage(browser).should_be_main_navbar()
    MainPage(browser).should_be_navbar_btn()
    MainPage(browser).should_be_search_btn()
    MainPage(browser).should_be_search_input()
    MainPage(browser).should_br_banners()


def test_change_currency(browser, url):
    MainPage(browser).open_page(url)
    MainPage(browser).change_currency_to_usd()
    MainPage(browser).check_currency_usd()
