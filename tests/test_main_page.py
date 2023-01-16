import pytest
from pages.main_page import MainPage
import allure


@allure.feature('Main page')
@allure.story('Page elements')
@pytest.mark.elements
def test_elements_main_page(browser, url):
    page = MainPage(browser)
    page.open_page(url)
    page.should_be_main_navbar()
    page.should_be_navbar_btn()
    page.should_be_search_btn()
    page.should_be_search_input()
    page.should_be_banners()


@allure.feature('Main page')
@allure.story('Change currency')
def test_change_currency(browser, url):
    page = MainPage(browser)
    page.open_page(url)
    page.change_currency_to_usd()
    page.check_currency_usd()
