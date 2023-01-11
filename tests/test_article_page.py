from pages.article_page import ArticlePage


def test_elements_article_page(browser, url):
    page = ArticlePage(browser)
    page.open_page(url)
    page.should_be_article()
    page.select_article()
    page.should_be_price()
    page.should_be_input_quantity()
    page.should_be_description_tab()
    page.should_be_cart_grade_stars()
