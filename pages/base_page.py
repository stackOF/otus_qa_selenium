from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
import logging
import allure


class BaseClass:
    def __init__(self, browser, timeout=3):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler(f"logs/{self.browser.test_name}.log")
        file_handler.setFormatter(logging.Formatter('[%(asctime)s: %(levelname)s] %(message)s'))
        self.logger.addHandler(file_handler)
        self.logger.setLevel(logging.DEBUG)

    @allure.step("Open url: {url}")
    def open_page(self, url):
        self.logger.info(f"Открытие страницы: {url}")
        self.browser.get(url)

    @allure.step("Check if element {locator} is present")
    def is_element_present(self, locator, timeout=1):
        """Проверка наличия элемента
        :param locator: локатор
        :param timeout: сколько ждать"""
        self.logger.info(f"Проверка наличия элемента: {locator}")
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located(locator))
        except TimeoutException as e:
            self.logger.exception(f'{TimeoutException}')
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG,
                name='screen_image')
            raise AssertionError(e.msg)
            return False
        return True

    @allure.step("Input {value} in {locator}")
    def input_value(self, locator, value, timeout=0.1):
        self.logger.info(f"Ввод {value} в поле ввода {locator}")
        input_field = WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located(locator))
        input_field.click()
        input_field.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
        input_field.send_keys(value)

    @allure.step("Clicking element {locator}")
    def click_element(self, locator, timeout=0.1):
        self.logger.info(f"Клик по элементу {locator}")
        WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located(locator)).click()
