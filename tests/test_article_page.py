from pages.article_page import ArticlePage


def test_elements_article_page(browser, url):
    ArticlePage(browser).open_page(url)
    ArticlePage(browser).should_be_article()
    ArticlePage(browser).select_article()
    ArticlePage(browser).should_be_price()
    ArticlePage(browser).should_be_input_quantity()
    ArticlePage(browser).should_be_description_tab()
    ArticlePage(browser).should_be_cart_grade_stars()
