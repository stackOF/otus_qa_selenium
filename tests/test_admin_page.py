import allure

from pages.admin_page import AdminPage


@allure.feature('Admin page')
@allure.story('Page elements')
def test_elements_admin_page(browser, url):
    page = AdminPage(browser)
    page.open_page(f'{url}/administration')
    page.should_be_title(browser)
    page.should_be_login_btn()
    page.should_be_header()
    page.should_be_username_input()
    page.click_login_btn()
    page.should_be_close_btn()


@allure.feature('Admin page')
@allure.story('Add new article to catalog')
def test_add_article(browser, url):
    page = AdminPage(browser)
    page.open_page(f'{url}/administration/')
    page.authorization()
    page.add_article()


@allure.feature('Admin page')
@allure.story('Delete article from catalog')
def test_delete_article(browser, url):
    page = AdminPage(browser)
    page.open_page(f'{url}/administration/')
    page.authorization()
    page.delete_article()
