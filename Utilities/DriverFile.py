from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from Utilities.Config import *


class Drivers:

    def getDriver( browser):
        if browser == "Chrome":
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser == "Edge":
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        elif browser == "Firefox":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.maximize_window()
        driver.get(meralco_online)
        return driver
