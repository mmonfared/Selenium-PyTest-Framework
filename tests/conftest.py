import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "firefox":
        # driver = webdriver.Firefox(executable_path="./drivers/geckodriver.exe")
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:
        # driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser: chrome or firefox"
    )
