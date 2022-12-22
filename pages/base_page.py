from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class BaseClass:
    def __init__(self, browser, timeout=3):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def open_page(self, url):
        self.browser.get(url)

    def is_element_present(self, how, what, timeout=1):
        """Проверка наличия элемента
        :param how: способ поиска элемента (By.CSS_SELECTOR/ By.XPATH, ...)
        :param what: локатор искомого объекта
        :param timeout: сколько ждать"""
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
