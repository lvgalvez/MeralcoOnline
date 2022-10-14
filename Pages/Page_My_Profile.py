from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class MyProfilePage:
    change_password = "//a[contains(text(), 'CHANGE PASSWORD')]"
    current_password = "//input[@placeholder= 'Current Password']"
    new_password = "//input[@placeholder= 'New Password']"
    confirm_new_password = "//input[@placeholder= 'Confirm New Password']"
    set_password = "//button[contains(text(), 'Set Password')]"
    password_confirmation = "//a[@class ='slds-button mov-button mov-element_max-width-170']"
    sso_prompt = "//p[contains(text(), 'For added security,')]"

    def get_change_password(self, driver):
        return WebMisc().wait_element(driver, self.change_password, "change_password")

    def get_current_password(self, driver):
        return WebMisc().wait_element(driver, self.current_password, "current_password")

    def get_new_password(self, driver):
        return WebMisc().wait_element(driver, self.new_password, "new_password")

    def get_confirm_new_password(self, driver):
        return WebMisc().wait_element(driver, self.confirm_new_password, "confirm_new_password")

    def get_set_password(self, driver):
        return WebMisc().wait_element(driver, self.set_password, "set_password")

    def get_password_confirmation(self, driver):
        return WebMisc().clickable_element(driver, self.password_confirmation, "password_confirmation")

    def get_sso_prompt(self, driver):
        return WebMisc().wait_element(driver, self.sso_prompt, "sso_prompt")
