import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', help="Choose language")
    parser.addoption('--browser', action='store', help="Choose browser")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption('language')
    browser_name = request.config.getoption('browser')
    if browser_name == "Chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "Firefox":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be Chrome or Firefox")
    yield browser
    browser.quit()
