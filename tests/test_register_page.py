from pages.register_page import RegisterPage


def test_elements_article_page(browser, url):
    RegisterPage(browser).open_page(f'{url}/index.php?route=account/register')
    RegisterPage(browser).should_be_register_form()
    RegisterPage(browser).should_be_firstname_input()
    RegisterPage(browser).should_be_privacy_link()
    RegisterPage(browser).call_privacy_form()
    RegisterPage(browser).should_be_modal_form()
    RegisterPage(browser).should_be_close_privacy()


def test_register_new_user(browser, url):
    RegisterPage(browser).open_page(f'{url}/index.php?route=account/register')
    RegisterPage(browser).register_new_user()
