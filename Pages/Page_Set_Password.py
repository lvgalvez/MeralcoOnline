
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class ResetPasswordPage:
    new_password = "//input[@placeholder= 'New Password *']"
    confirm_password = "//input[@id = '555:2;a']"
    set_password = "//button[@data-aura-rendered-by= '612:2;a']"

    def get_new_password(self, driver):
        return WebMisc().wait_element(driver, self.new_password, "new_password")

    def get_confirm_password(self, driver):
        return WebMisc().wait_element(driver, self.confirm_password, "confirm_password")

    def get_set_password(self, driver):
        return WebMisc().wait_element(driver, self.set_password, "set_password")
