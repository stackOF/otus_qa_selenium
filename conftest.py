import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="https://demo.opencart.com")


@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(service=Service('chromedriver'), options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        service = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        driver = webdriver.Firefox(service=service)
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception("Драйвер не поддерживается")
    request.addfinalizer(driver.quit)
    return driver


@pytest.fixture
def url(request):
    return request.config.getoption('--url')
