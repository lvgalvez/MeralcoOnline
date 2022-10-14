from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class CXEHomePage:

    search_button = "//button[@class= 'slds-button slds-button_neutral search-button slds-truncate']"
    search_input = "//input[@class= 'slds-input']"

    def get_search_button(self, driver):
        return WebMisc().optional_wait_element(driver, self.search_button, "search_button")

    def get_search_input(self, driver):
        return WebMisc().optional_wait_element(driver, self.search_input, "search_input")