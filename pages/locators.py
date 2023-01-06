from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы"""
    NAVBAR = (By.CSS_SELECTOR, "[id='narbar-menu']")
    NAVBAR_BTN = (By.CSS_SELECTOR, "[class='navbar-toggler']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "[class='form-control form-control-lg']")
    SEARCH_BTN = (By.CSS_SELECTOR, "[class='btn btn-light btn-lg']")
    BANNERS = (By.CSS_SELECTOR, "[id ='carousel-banner-1']")
    CURRENCY = (By.CSS_SELECTOR, "[id='form-currency']")
    USD_LINK = (By.LINK_TEXT, "$ US Dollar")
    TEXT_USD = (By.CSS_SELECTOR, "strong")
    ICON_USD = '$'


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
    DESCRIPTION_TAB = (By.LINK_TEXT, "Description")
    PRICE = (By.CSS_SELECTOR, "[class='price-new']")
    RATING_STARS = (By.CSS_SELECTOR, "[class='rating']")


class AdminPageLocators:
    TITLE = 'Administration'
    CLOSE_BTN = (By.CSS_SELECTOR, "[class='btn-close']")
    HEADER = (By.CLASS_NAME, "card-header")
    USERNAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BTN = (By.CSS_SELECTOR, "[class='btn btn-primary']")
    LOGIN = 'user'
    PASSWORD = 'bitnami'
    TEST_PRODUCT_NAME = 'TEST ARTICLE'
    TEST_PRODUCT_META = 'TEST META'
    TEST_PRODUCT_MODEL = 'TEST MODEL'
    TEST_SEO_INPUT = "TEST SEO"
    CATALOG = (By.CSS_SELECTOR, "[class='fas fa-tag']")
    PRODUCTS = (By.XPATH, "//*[@id ='collapse-1']/li[2]/a")
    ADD_NEW_BTN = (By.CSS_SELECTOR, "[title='Add New']")
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, "[id='input-name-1']")
    PRODUCT_META_INPUT = (By.CSS_SELECTOR, "[id='input-meta-title-1']")
    TAB_DATA = (By.CSS_SELECTOR, "[href='#tab-data']")
    TAB_SEO = (By.CSS_SELECTOR, "[href='#tab-seo']")
    MODEL_INPUT = (By.CSS_SELECTOR, "[id ='input-model']")
    SEO_URL_INPUT = (By.CSS_SELECTOR, "[name='product_seo_url[0][1]']")
    SUBMIT_BTN = (By.CSS_SELECTOR, "[type='submit']")
    CHECKBOX_ARTICLE = (By.CSS_SELECTOR, "tbody tr:nth-child(3) input")
    DELETE_BTN = (By.CSS_SELECTOR, "[class='fa-regular fa-trash-can']")


class RegisterPageLocators:
    REGISTER_FORM = (By.CSS_SELECTOR, "[id='form-register']")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "[id='input-firstname']")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "[id='input-lastname']")
    PRIVACY_POLICY = (By.LINK_TEXT, "Privacy Policy")
    MODAL_FORM = (By.CSS_SELECTOR, "[class='modal-content']")
    CLOSE_BTN = (By.CSS_SELECTOR, "[class= 'btn-close']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[id='input-email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[id='input-password']")
    PRIVACY_AGREE_CHECKBOX = (By.CSS_SELECTOR, "[name='agree']")
    SUBMIT_BTN = (By.CSS_SELECTOR, "button[type ='submit']")
    FIRSTNAME = 'SEMEN'
    LASTNAME = 'SEMENOV'
    EMAIL = 'semsem@mail.ru'
    PASSWORD = 'semsem123'
