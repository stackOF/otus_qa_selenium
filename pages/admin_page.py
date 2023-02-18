from selenium.webdriver import ActionChains, Keys
from pages.base_page import BaseClass
from pages.locators import AdminPageLocators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import allure


class AdminPage(BaseClass):
    def should_be_title(self, browser):
        assert WebDriverWait(browser, 3).until(ec.title_is(AdminPageLocators.TITLE)), \
            f"Окно администратора: нет заголовка {AdminPageLocators.TITLE}"

    def should_be_close_btn(self):
        assert self.is_element_present(AdminPageLocators.CLOSE_BTN), \
            "Окно администратора: отсутствует кнопка закрытия сообщения о неуспешной авторизации"

    def should_be_header(self):
        assert self.is_element_present(AdminPageLocators.HEADER), "Окно администратора: отсутствует заголовок"

    def should_be_username_input(self):
        assert self.is_element_present(AdminPageLocators.USERNAME_INPUT), \
            "Окно администратора: отсутствует поле ввода username"

    def should_be_login_btn(self):
        assert self.is_element_present(AdminPageLocators.LOGIN_BTN), "Окно администратора: отсутствует кнопка логина"

    @allure.step("Click login button")
    def click_login_btn(self):
        self.logger.info(f"Клик кнопки логина")
        self.click_element(AdminPageLocators.LOGIN_BTN)

    @allure.step("Authorization by admin")
    def authorization(self):
        self.logger.info(f"Авторизация")
        self.input_value(AdminPageLocators.USERNAME_INPUT, AdminPageLocators.LOGIN)
        self.input_value(AdminPageLocators.PASSWORD_INPUT, AdminPageLocators.PASSWORD)
        self.click_login_btn()

    @allure.step("Go to products tab")
    def go_to_products_tab(self):
        self.logger.info(f"Переход к вкладке продуктов")
        self.browser.maximize_window()
        self.click_element(AdminPageLocators.CATALOG)
        self.click_element(AdminPageLocators.PRODUCTS)

    @allure.step("Add article to catalog")
    def add_article(self):
        self.logger.info(f"Добавление товара в панели админа")
        self.go_to_products_tab()
        self.click_element(AdminPageLocators.ADD_NEW_BTN)
        self.input_value(AdminPageLocators.PRODUCT_NAME_INPUT, AdminPageLocators.TEST_PRODUCT_NAME)
        self.input_value(AdminPageLocators.PRODUCT_META_INPUT, AdminPageLocators.TEST_PRODUCT_META)
        self.click_element(AdminPageLocators.TAB_DATA)
        self.input_value(AdminPageLocators.MODEL_INPUT, AdminPageLocators.TEST_PRODUCT_MODEL)
        self.click_element(AdminPageLocators.TAB_SEO)
        self.input_value(AdminPageLocators.SEO_URL_INPUT, AdminPageLocators.TEST_SEO_INPUT)
        self.click_element(AdminPageLocators.SUBMIT_BTN)

    @allure.step("Delete article from catalog")
    def delete_article(self):
        self.logger.info(f"Удаление товара в панели админа")
        self.go_to_products_tab()
        self.click_element(AdminPageLocators.CHECKBOX_ARTICLE)
        self.click_element(AdminPageLocators.DELETE_BTN)
        ActionChains(self.browser).send_keys(Keys.ENTER)
