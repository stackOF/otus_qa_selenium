from pages.register_page import RegisterPage


def test_elements_article_page(browser, url):
    page = RegisterPage(browser)
    page.open_page(f'{url}/index.php?route=account/register')
    page.should_be_register_form()
    page.should_be_firstname_input()
    page.should_be_privacy_link()
    page.call_privacy_form()
    page.should_be_modal_form()
    page.should_be_close_privacy()


def test_register_new_user(browser, url):
    page = RegisterPage(browser)
    page.open_page(f'{url}/index.php?route=account/register')
    page.register_new_user()
