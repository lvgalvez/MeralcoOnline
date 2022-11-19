from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc
from Utilities.Data import *


class CXEHomePage:

    search_button = "//button[@class= 'slds-button slds-button_neutral search-button slds-truncate']"
    search_input = "//input[@class= 'slds-input']"
    suggestion_case = "//*[contains(@id, 'suggestionsList')]/search_dialog-instant-result-item[1]/div[1]/div[2]/div/lightning-formatted-rich-text/span[contains(text(), 'Case')]"
    profile_options = ".mauto .userOptionBtn"
    logout_btn = "//button[text() = 'Logout']"
    switch_profile_btn = "//button[text() = 'Switch Profile']"
    switch_profile = "//*[@id='profileModal']/div/div/md-card/md-card-content/form/div[1]/div/button"
    #profile_account = "//li[text() = '"+ Outage['switch_profile'] + "']"
    profile_account = "//*[@id='profileModal']/div/div/md-card/md-card-content/form/div[1]/div/ul/li[2]"
    okay_btn = "//*[@id='profileModal']/div/div/md-card/md-card-content/form/div[4]/button[1]"

    def get_search_button(self, driver):
        return WebMisc().optional_wait_element(driver, self.search_button, "search_button")

    def get_search_input(self, driver):
        return WebMisc().optional_wait_element(driver, self.search_input, "search_input")

    def get_suggestion_case(self, driver):
        return WebMisc().clickable_element(driver, self.suggestion_case, "suggestion_case")

    def get_profile_options(self, driver):
        return driver.find_element(By.CSS_SELECTOR,self.profile_options).click()

    def logout_account(self,driver):
        return WebMisc().clickable_element(driver, self.logout_btn, "logout_btn")

    def click_switch_profile(self,driver):
        return WebMisc().clickable_element(driver, self.switch_profile_btn, "switch_profile_btn")

    def switch_account(self, driver):
        return WebMisc().clickable_element(driver, self.switch_profile, "switch_profile")

    def get_profile(self, driver):
        driver.find_element(By.XPATH, self.profile_account).click()

    def get_profile_value(self, driver):
        driver.find_element(By.XPATH, self.okay_btn).click()