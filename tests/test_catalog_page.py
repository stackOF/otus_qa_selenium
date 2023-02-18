import pytest
from pages.catalog_page import CatalogPage
import allure


@allure.feature('Catalog page')
@allure.story('Go to page and page elements')
@pytest.mark.elements
def test_elements_catalog_page(browser, url):
    page = CatalogPage(browser)
    page.go_to_catalog_page(browser, url)
    page.should_be_show_label()
    page.should_be_compare_total()
    page.should_be_limit_show_input()
    page.should_be_limit_sort_label()
    page.should_be_compare_total()
