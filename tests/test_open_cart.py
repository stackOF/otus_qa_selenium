import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from dataclasses import dataclass

#
# @dataclass(frozen=True)
# class MainPageLocators:
#     main_navbar: tuple = (By.CSS_SELECTOR, "[id='narbar-menu']")
#     main_navbar_btn: tuple = (By.CSS_SELECTOR, "[class='navbar-toggler']")
#     main_search_input: tuple = (By.CSS_SELECTOR, "[class='form-control form-control-lg']")
#     main_search_btn: tuple = (By.CSS_SELECTOR, "[class='btn btn-light btn-lg']")
#     main_banners: tuple = (By.CSS_SELECTOR, "[id ='carousel-banner-1']")
#
#
# def is_element_present(browser, how, what, timeout=1):
#     return WebDriverWait(browser, timeout).until(ec.presence_of_element_located((how, what)))
#
#
# def test_main_page(browser, url):
#     """Тест главного окна"""
#     browser.get(url)
#     assert browser.title == 'Your Store', "Страница отличается от ожидаемой"
#     assert is_element_present(browser, *MainPageLocators.main_navbar, timeout=2), "Главное окно: нет навигационной" \
#                                                                                   " панели"
#     assert is_element_present(browser, *MainPageLocators.main_navbar_btn), "Главное окно: нет кнопки-навигации по " \
#                                                                            "разделам"
#     assert is_element_present(browser, *MainPageLocators.main_search_input), "Главное окно: нет поля ввода поиска"
#     assert is_element_present(browser, *MainPageLocators.main_search_btn), "Главное окно: нет кнопки 'поиск'"
#     assert is_element_present(browser, *MainPageLocators.main_banners), "Главное окно: нет баннера"
#

# @pytest.mark.parametrize("elements_locators", ["//select[@id='input-sort']", "//select[@id='input-limit']",
#                                                "//label[@for='input-sort']", "//label[@for='input-limit']",
#                                                "//a[@id='compare-total']"])
# def test_catalog_page(browser, url, elements_locators):
#     """Тест каталога товаров"""
#     browser.get(url)
#     browser.maximize_window()
#     WebDriverWait(browser, 1).until(ec.presence_of_element_located((By.LINK_TEXT, "Desktops"))).click()
#     WebDriverWait(browser, 2).until(ec.presence_of_element_located((By.LINK_TEXT, "Show All Desktops"))).click()
#     try:
#         WebDriverWait(browser, 2).until(ec.presence_of_element_located((By.XPATH, elements_locators)))
#     except TimeoutException:
#         raise AssertionError(f"Элемент '{elements_locators}' не найден на странице каталога товаров")


# def test_article_page(browser, url):
#     browser.get(url)
#     wait = WebDriverWait(browser, 1)
#     wait.until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR, "[id=content] > div.row .product-thumb")))[0].\
#         click()
#     wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[id='button-cart']")))
#     wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[id='input-quantity']")))
#     wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[id='description-tab']")))
#     wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[class='price-new']")))
#     assert len(wait.until(ec.visibility_of_all_elements_located
#                           ((By.CSS_SELECTOR, "[class='far fa-star fa-stack-1x']")))) == 5


def test_admin_page(browser, url):
    browser.get(f'{url}/admin')
    wait = WebDriverWait(browser, 1)
    wait.until(ec.title_is("Administration"))
    wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "[class=btn-close]")))
    wait.until(ec.text_to_be_present_in_element((By.CLASS_NAME, "card-header"), "Please enter your login details."))
    wait.until(ec.element_to_be_clickable(browser.find_element(By.ID, "input-username")))
    browser.find_element(By.ID, "input-username").send_keys('superman')
    browser.find_element(By.CSS_SELECTOR, "[class='btn btn-primary']").click()
    WebDriverWait(browser, 3).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[class=btn-close]")))


def test_register_user_page(browser, url):
    browser.get(f'{url}/index.php?route=account/register')
    wait = WebDriverWait(browser, 1)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[id='form-register']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[id='input-firstname']")))
    wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Privacy Policy"))).click()
    WebDriverWait(browser, 3).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[class='modal-content']")))
    WebDriverWait(browser, 3).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[class= 'btn-close']"))).click()
