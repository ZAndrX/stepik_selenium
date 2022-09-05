import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser_op(request):
    chrome_options = Options()
    chrome_options.add_argument("--lang=ru")
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()