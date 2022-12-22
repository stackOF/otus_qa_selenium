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


class ArticlePageLocators:
    ARTICLE = (By.CSS_SELECTOR, "[id=content] > div.row .product-thumb")
    QUANTITY_INPUT = (By.CSS_SELECTOR, "[id='button-cart']")
    DESCRIPTION_TAB = (By.CSS_SELECTOR, "[id='description-tab']")
    PRICE = (By.CSS_SELECTOR, "[class='price-new']")
    STARS = (By.CSS_SELECTOR, "[class='far fa-star fa-stack-1x']")


class AdminPageLocators:
    TITLE = 'Administration'
    CLOSE_BTN = (By.CSS_SELECTOR, "[class='btn-close']")
    HEADER = (By.CLASS_NAME, "card-header")
    USERNAME_INPUT = (By.ID, "input-username")
    LOGIN_BTN = (By.CSS_SELECTOR, "[class='btn btn-primary']")


class RegisterPageLocators:
    REGISTER_FORM = (By.CSS_SELECTOR, "[id='form-register']")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "[id='input-firstname']")
    PRIVACY_POLICY = (By.LINK_TEXT, "Privacy Policy")
    MODAL_FORM = (By.CSS_SELECTOR, "[class='modal-content']")
    CLOSE_BTN = (By.CSS_SELECTOR, "[class= 'btn-close']")
