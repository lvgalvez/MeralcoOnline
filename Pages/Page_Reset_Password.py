
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class ResetPasswordPage:
    new_password = "//input[@placeholder= 'New Password *']"
    confirm_password = "//input[@placeholder= 'Confirm New Password *']"
    set_password = "//button[@class= 'slds-button slds-button--neutral slds-button mov-button mov-button_login responsive-width-button uiButton']"

    def get_new_password(self, driver):
        return WebMisc().wait_element(driver, self.new_password, "new_password")

    def get_confirm_password(self, driver):
        return WebMisc().wait_element(driver, self.confirm_password, "confirm_password")

    def get_set_password(self, driver):
        return WebMisc().wait_element(driver, self.set_password, "set_password")
