import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language")


@pytest.fixture(scope="function")
def browser_op(request):
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': "language"})
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()
