from pages.base_page import BaseClass
from pages.locators import MainPageLocators

class MainPage(BaseClass):

    def should_be_main_navbar(self):
        assert self.is_element_present(*MainPageLocators.NAVBAR), \
            "Главное окно: отсутвтует панель навигации"

    def should_be_navbar_btn(self):
        assert self.is_element_present(*MainPageLocators.NAVBAR_BTN), \
            "Главное окно: отсутвтвует кнопка панели навигации"

    def should_be_search_input(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_INPUT), \
            "Главное окно: отсутствует поле поиска"

    def should_be_search_btn(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_BTN), \
            "Главное окно: отсутствует кнопка поиска"

    def should_br_banners(self):
        assert self.is_element_present(*MainPageLocators.BANNERS), \
            "Главное окно: отсутствуют баннеры"
