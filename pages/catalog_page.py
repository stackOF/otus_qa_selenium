from pages.base_page import BaseClass
from pages.locators import CatalogPageLocators
import allure


class CatalogPage(BaseClass):

    def should_be_sort_select(self):
        assert self.is_element_present(CatalogPageLocators.SORT_SELECT), \
            "Страница товара: отсутствует  элемент выбора сортировки"

    def should_be_limit_show_input(self):
        assert self.is_element_present(CatalogPageLocators.LIMIT_SHOW_INPUT), \
            "Страница товара: отсутствует элемент выбора сортировки"

    def should_be_limit_sort_label(self):
        assert self.is_element_present(CatalogPageLocators.SORT_LABEL), \
            "Страница товара: отсутствует надпись 'Sort by'"

    def should_be_show_label(self):
        assert self.is_element_present(CatalogPageLocators.SHOW_LABEL), \
            "Страница товара: отсутствует надпись 'Show label'"

    def should_be_compare_total(self):
        assert self.is_element_present(CatalogPageLocators.COMPARISON_BTN), \
            "Страница товара: отсутствует кнопка сравнения"

    @allure.step("Go to catalog page")
    def go_to_catalog_page(self, browser, url):
        self.logger.info("Переход к каталогу")
        self.browser.get(url)
        browser.maximize_window()
        self.click_element(CatalogPageLocators.CATEGORY_DESCTOPS_LINK)
        self.click_element(CatalogPageLocators.SHOW_ALL_LINK)
