from selenium.webdriver.common.by import By
class MainPageLocators:
    """Локаторы главной страницы"""
    NAVBAR = (By.CSS_SELECTOR, "[id='narbar-menu']")
    NAVBAR_BTN = (By.CSS_SELECTOR, "[class='navbar-toggler']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "[class='form-control form-control-lg']")
    SEARCH_BTN = (By.CSS_SELECTOR, "[class='btn btn-light btn-lg']")
    BANNERS = (By.CSS_SELECTOR, "[id ='carousel-banner-1']")

class CatalogPageLocators:
    CATEGORY_DESCTOPS_LINK = (By.LINK_TEXT, "Desktops")
    SHOW_ALL_LINK = (By.LINK_TEXT, "Show All Desktops")

    SORT_SELECT = (By.XPATH, "//select[@id='input-sort']")
    LIMIT_SHOW_INPUT = (By.XPATH, "//select[@id='input-limit']")
    SORT_LABEL = (By.XPATH, "//label[@for='input-sort']")
    SHOW_LABEL = (By.XPATH, "//label[@for='input-limit']")
    COMPARISON_BTN = (By.XPATH, "//a[@id='compare-total']")


