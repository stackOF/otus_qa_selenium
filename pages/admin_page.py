from selenium.webdriver import ActionChains, Keys
from pages.base_page import BaseClass
from pages.locators import AdminPageLocators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class AdminPage(BaseClass):
    def should_be_title(self, browser):
        assert WebDriverWait(browser, 1).until(ec.title_is(AdminPageLocators.TITLE)), \
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

    def click_login_btn(self):
        self.browser.find_element(*AdminPageLocators.LOGIN_BTN).click()

    def authorization(self):
        self.input_value(self.browser.find_element(*AdminPageLocators.USERNAME_INPUT), AdminPageLocators.LOGIN)
        self.input_value(self.browser.find_element(*AdminPageLocators.PASSWORD_INPUT), AdminPageLocators.PASSWORD)
        self.click_login_btn()

    def go_to_products_tab(self):
        self.browser.maximize_window()
        self.click_element(self.browser.find_element(*AdminPageLocators.CATALOG))
        self.click_element(self.browser.find_element(*AdminPageLocators.PRODUCTS))

    def add_article(self):
        self.go_to_products_tab()
        self.click_element(self.browser.find_element(*AdminPageLocators.ADD_NEW_BTN))
        self.input_value(self.browser.find_element(*AdminPageLocators.PRODUCT_NAME_INPUT),
                         AdminPageLocators.TEST_PRODUCT_NAME)
        self.input_value(self.browser.find_element(*AdminPageLocators.PRODUCT_META_INPUT),
                         AdminPageLocators.TEST_PRODUCT_META)
        self.click_element(self.browser.find_element(*AdminPageLocators.TAB_DATA))
        self.input_value(self.browser.find_element(*AdminPageLocators.MODEL_INPUT),
                         AdminPageLocators.TEST_PRODUCT_MODEL)
        self.click_element(self.browser.find_element(*AdminPageLocators.TAB_SEO))
        self.input_value(self.browser.find_element(*AdminPageLocators.SEO_URL_INPUT),
                         AdminPageLocators.TEST_SEO_INPUT)
        self.click_element(self.browser.find_element(*AdminPageLocators.SUBMIT_BTN))

    def delete_article(self):
        self.go_to_products_tab()
        self.click_element(self.browser.find_element(*AdminPageLocators.CHECKBOX_ARTICLE))
        self.click_element(self.browser.find_element(*AdminPageLocators.DELETE_BTN))
        ActionChains(self.browser).send_keys(Keys.ENTER)
