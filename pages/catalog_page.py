from pages.base_page import BaseClass
from pages.locators import CatalogPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class CatalogPage(BaseClass):

    def should_be_sort_select(self):
        assert self.is_element_present(*CatalogPageLocators.SORT_SELECT), \
            "Страница товара: отсутствует  элемент выбора сортировки"

    def should_be_limit_show_input(self):
        assert self.is_element_present(*CatalogPageLocators.LIMIT_SHOW_INPUT), \
            "Страница товара: отсутствует элемент выбора сортировки"

    def should_be_limit_sort_label(self):
        assert self.is_element_present(*CatalogPageLocators.SORT_LABEL), \
            "Страница товара: отсутствует надпись 'Sort by'"

    def should_be_show_label(self):
        assert self.is_element_present(*CatalogPageLocators.SHOW_LABEL), \
            "Страница товара: отсутствует надпись 'Show label'"

    def should_be_compare_total(self):
        assert self.is_element_present(*CatalogPageLocators.COMPARISON_BTN), \
            "Страница товара: отсутствует кнопка сравнения"

    def go_to_catalog_page(self, browser, url):
        self.browser.get(url)
        browser.maximize_window()
        WebDriverWait(browser, 2).until(ec.presence_of_element_located(CatalogPageLocators.CATEGORY_DESCTOPS_LINK)) \
            .click()
        WebDriverWait(browser, 2).until(ec.presence_of_element_located(CatalogPageLocators.SHOW_ALL_LINK)).click()
