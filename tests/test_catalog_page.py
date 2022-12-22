import pytest
from pages.catalog_page import CatalogPage


@pytest.mark.elements
def test_elements_catalog_page(browser, url):
    CatalogPage(browser).go_to_catalog_page(browser, url)
    CatalogPage(browser).should_be_show_label()
    CatalogPage(browser).should_be_compare_total()
    CatalogPage(browser).should_be_limit_show_input()
    CatalogPage(browser).should_be_limit_sort_label()
    CatalogPage(browser).should_be_compare_total()
