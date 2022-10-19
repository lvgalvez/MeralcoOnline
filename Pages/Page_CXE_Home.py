from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class CXEHomePage:

    search_button = "//button[@class= 'slds-button slds-button_neutral search-button slds-truncate']"
    search_input = "//input[@class= 'slds-input']"
    suggestion_case = "//*[contains(@id, 'suggestionsList')]/search_dialog-instant-result-item[1]/div[1]/div[2]/div/lightning-formatted-rich-text/span[contains(text(), 'Case')]"

    def get_search_button(self, driver):
        return WebMisc().optional_wait_element(driver, self.search_button, "search_button")

    def get_search_input(self, driver):
        return WebMisc().optional_wait_element(driver, self.search_input, "search_input")

    def get_suggestion_case(self, driver):
        return WebMisc().clickable_element(driver, self.suggestion_case, "suggestion_case")

