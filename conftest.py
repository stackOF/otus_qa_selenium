import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import logging
import datetime
import allure
import json


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="http://localhost")


@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('[%(asctime)s: %(levelname)s] %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)

    logger.info(f"===//// Старт тестов {request.node.name} в {datetime.datetime.now()} ===////")
    if browser == "chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(service=Service('chromedriver'), options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(service=Service('geckodriver'), options=options)
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception("Драйвер не поддерживается")

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities),
        attachment_type=allure.attachment_type.JSON)

    with open("allure-results/environment.xml", "w+") as file:
        file.write(f"""<environment>
                  <parameter>
                      <key>Browser</key>
                      <value>{browser}</value>
              </environment>""")

    driver.logger = logger
    driver.test_name = request.node.name

    def fin():
        driver.quit()
        logger.info(f"===//// Завершение тестов {request.node.name} в {datetime.datetime.now()} ===////")

    request.addfinalizer(fin)
    return driver


@pytest.fixture
def url(request):
    return request.config.getoption('--url')
