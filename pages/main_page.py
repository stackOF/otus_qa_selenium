from pages.base_page import BaseClass
from pages.locators import MainPageLocators
import allure


class MainPage(BaseClass):

    def should_be_main_navbar(self):
        assert self.is_element_present(MainPageLocators.NAVBAR), \
            "Главное окно: отсутвтует панель навигации"

    def should_be_navbar_btn(self):
        assert self.is_element_present(MainPageLocators.NAVBAR_BTN), \
            "Главное окно: отсутвтвует кнопка панели навигации"

    def should_be_search_input(self):
        assert self.is_element_present(MainPageLocators.SEARCH_INPUT), \
            "Главное окно: отсутствует поле поиска"

    def should_be_search_btn(self):
        assert self.is_element_present(MainPageLocators.SEARCH_BTN), \
            "Главное окно: отсутствует кнопка поиска"

    def should_be_banners(self):
        assert self.is_element_present(MainPageLocators.BANNERS), \
            "Главное окно: отсутствуют баннеры"

    @allure.step("Change currency to USD")
    def change_currency_to_usd(self):
        self.logger.info(f"Смена валюты на USD")
        self.click_element(MainPageLocators.CURRENCY)
        self.click_element(MainPageLocators.USD_LINK)

    @allure.step("Check currency USD")
    def check_currency_usd(self):
        self.logger.info(f"Проверка текущей валюты (что она USD)")
        assert self.browser.find_element(*MainPageLocators.TEXT_USD).get_attribute("textContent") ==\
               MainPageLocators.ICON_USD, "Валюта не установлена на выбранную"
