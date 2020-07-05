import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: ru or es")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption('language')
    browser = webdriver.Chrome()
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    if language == "ru":
        browser.get(link)
    elif language == "es":
        browser.get(link)
    else:
        raise pytest.UsageError("--language= should be ru or es")
    yield browser
    browser.quit()
