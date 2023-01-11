from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains


class BaseClass:
    def __init__(self, browser, timeout=3):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def open_page(self, url):
        self.browser.get(url)

    def is_element_present(self, locator, timeout=1):
        """Проверка наличия элемента
        :param locator: локатор
        :param timeout: сколько ждать"""
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def input_value(self, element, value):
        ActionChains(self.browser).move_to_element(element).click(element)
        element.clear()
        element.send_keys(value)

    def click_element(self, element):
        ActionChains(self.browser).move_to_element(element).click(element).perform()
