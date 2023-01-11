from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
import logging


class BaseClass:
    def __init__(self, browser, timeout=3):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler(f"logs/{self.browser.test_name}.log")
        file_handler.setFormatter(logging.Formatter('[%(asctime)s: %(levelname)s] %(message)s'))
        self.logger.addHandler(file_handler)
        self.logger.setLevel(logging.DEBUG)

    def open_page(self, url):
        self.logger.info(f"Открытие страницы: {url}")
        self.browser.get(url)

    def is_element_present(self, locator, timeout=1):
        """Проверка наличия элемента
        :param locator: локатор
        :param timeout: сколько ждать"""
        self.logger.info(f"Проверка наличия элемента: {locator}")
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located(locator))
        except TimeoutException:
            self.logger.exception(f'{TimeoutException}')
            return False
        return True

    def input_value(self, element, value):
        ActionChains(self.browser).move_to_element(element).click(element)
        element.clear()
        element.send_keys(value)

    def click_element(self, element):
        ActionChains(self.browser).move_to_element(element).click(element).perform()
