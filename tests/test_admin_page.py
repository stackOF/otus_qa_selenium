from pages.admin_page import AdminPage


def test_elements_admin_page(browser, url):
    AdminPage(browser).open_page(f'{url}/administration')
    AdminPage(browser).should_be_title(browser)
    AdminPage(browser).should_be_login_btn()
    AdminPage(browser).should_be_header()
    AdminPage(browser).should_be_username_input()
    AdminPage(browser).click_login_btn()
    AdminPage(browser).should_be_close_btn()


def test_add_article(browser, url):
    AdminPage(browser).open_page(f'{url}/administration/')
    AdminPage(browser).authorization()
    AdminPage(browser).add_article()


def test_delete_article(browser, url):
    AdminPage(browser).open_page(f'{url}/administration/')
    AdminPage(browser).authorization()
    AdminPage(browser).delete_article()
