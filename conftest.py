import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# путь до драйверов
DRIVER_PATH_CHROME = './chromedriver'
DRIVER_PATH_FIREFOX = './geckodriver'


@pytest.fixture(params=['firefox', 'chrome'], scope='class')
def driver(request):
    driver = None
    if request.param == 'chrome':
        service = Service(executable_path=DRIVER_PATH_CHROME)
        options = Options()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=service, options=options)
    if request.param == 'firefox':
        service = Service(executable_path=DRIVER_PATH_FIREFOX)
        driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()
