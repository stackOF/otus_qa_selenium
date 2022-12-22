from pages.base_page import BaseClass
from pages.locators import RegisterPageLocators


class RegisterPage(BaseClass):
    def should_be_register_form(self):
        assert self.is_element_present(*RegisterPageLocators.REGISTER_FORM),\
            "Окно регистрации: нет регистрационной формы"

    def should_be_firstname_input(self):
        assert self.is_element_present(*RegisterPageLocators.FIRSTNAME_INPUT), "Окно регистрации: нет поля ввода имени"

    def should_be_privacy_link(self):
        assert self.is_element_present(*RegisterPageLocators.PRIVACY_POLICY), "Окно регистрации: нет ссылки политики"

    def should_be_modal_form(self):
        assert self.is_element_present(*RegisterPageLocators.MODAL_FORM),\
            "Окно регистрации: нет модального окна  с политикой"

    def should_be_close_privacy(self):
        assert self.is_element_present(*RegisterPageLocators.CLOSE_BTN), \
            "Окно регистрации: нет кнопки закрытия модельной формы с политикой"

    def call_privacy_form(self):
        self.browser.find_element(*RegisterPageLocators.PRIVACY_POLICY).click()
