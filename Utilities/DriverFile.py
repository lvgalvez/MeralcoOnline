from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
#import undetected_chromedriver as uc
from Utilities.Config import *
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
chromeOption = Options()
chromeOption.add_argument(f'user-agent={user_agent}')
class Drivers:

    def getDriver( browser):
        if browser == "Chrome":
            #driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()))
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chromeOption)
        elif browser == "Edge":
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        elif browser == "Firefox":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.maximize_window()
        driver.get(meralco_online)
        return driver
