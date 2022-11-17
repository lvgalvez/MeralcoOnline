import pytest
from Utilities.DriverFile import Drivers
from Utilities.Functions import Functions
from Utilities.Utils import *


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--tags")

@pytest.fixture(scope="function")
def setup(request):
    log = Utilities().getlogger()
    log.info("Browser Launched!")

    browser = request.config.getoption('--browser')
    tags = request.config.getoption('--tags')

    request.cls.tags = tags

    if browser.lower() == "chrome":
        driver = Drivers.getDriver("Chrome")
    elif browser.lower() == "firefox":
        driver = Drivers.getDriver("Firefox")
    else:
        driver = Drivers.getDriver("Edge")

    request.cls.driver = driver
    request.cls.browser = browser
    yield
    log.info("Close Browser")
    #driver.close()
