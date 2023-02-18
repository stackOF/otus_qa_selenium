from pages.base_page import BaseClass
from pages.locators import ArticlePageLocators
import allure


class ArticlePage(BaseClass):
    def should_be_article(self):
        assert self.is_element_present(ArticlePageLocators.ARTICLE), "Главное окно: отсутствует карточка товара"

    def should_be_input_quantity(self):
        assert self.is_element_present(ArticlePageLocators.QUANTITY_INPUT), \
            "Окно товара: отсутствует поле ввода количества"

    def should_be_description_tab(self):
        assert self.is_element_present(ArticlePageLocators.DESCRIPTION_TAB), "Окно товара: отсутствует описание товара"

    def should_be_price(self):
        assert self.is_element_present(ArticlePageLocators.PRICE), "Окно товара: отсутствует цена товара"

    def should_be_cart_grade_stars(self):
        assert self.is_element_present(ArticlePageLocators.RATING_STARS), \
            "Окно товара: отсутствует элемент (звезды) оценки товара"

    @allure.step("Select article")
    def select_article(self):
        self.logger.info(f"Выбор товара")
        self.click_element(ArticlePageLocators.ARTICLE)
