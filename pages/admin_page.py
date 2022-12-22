from pages.base_page import BaseClass
from pages.locators import AdminPageLocators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class AdminPage(BaseClass):
    def should_be_title(self, browser):
        assert WebDriverWait(browser, 1).until(ec.title_is(AdminPageLocators.TITLE)), \
            f"Окно администратора: нет заголовка{AdminPageLocators.TITLE}"

    def should_be_close_btn(self):
        assert self.is_element_present(*AdminPageLocators.CLOSE_BTN), \
            "Окно администратора: отсутствует кнопка закрытия сообщения о неуспешной авторизации"

    def should_be_header(self):
        assert self.is_element_present(*AdminPageLocators.HEADER), "Окно администратора: отсутствует заголовок"

    def should_be_username_input(self):
        assert self.is_element_present(*AdminPageLocators.USERNAME_INPUT), \
            "Окно администратора: отсутствует поле ввода username"

    def should_be_login_btn(self):
        assert self.is_element_present(*AdminPageLocators.LOGIN_BTN), "Окно администратора: отсутствует кнопка логина"

    def click_login_btn(self):
        self.browser.find_element(*AdminPageLocators.LOGIN_BTN).click()
