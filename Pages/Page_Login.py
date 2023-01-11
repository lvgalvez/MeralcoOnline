
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class LoginPage:
    email = "//input[@class = 'slds-input mov-input custom-email input uiInput uiInputText uiInput--default uiInput--input']"
    password = "//input[@class = 'slds-input mov-input custom-email input uiInput uiInputSecret uiInput--default uiInput--input']"
    log_in = "//button[@class = 'slds-button slds-button--neutral slds-button mov-button mov-button_login uiButton']"
    forgot_password = "//u[contains(text(), 'Forgot password?')]"
    new_password_confirmation = "//button[contains(text(), 'Send Confirmation Email')]"
    google_login = "//button[@class = 'slds-button slds-button--neutral slds-button slds-button--neutral slds-button mov-button mov-button_gplogin uiButton']"
    sign_up_here = "span.signup-pw"
    red_banner = "//div[contains(@class, 'cCXE_Alert_Header')]"
    apple_login = "//form/div/div[4]/div/div[3]/div/div[3]/div[2]/button"


    def get_email(self, driver):
        return WebMisc().wait_element(driver, self.email, "email")

    def get_password(self, driver):
        return WebMisc().wait_element(driver, self.password, "password")

    def get_log_in(self, driver):
        return WebMisc().wait_element(driver, self.log_in, "log_in")

    def get_forgot_password(self, driver):
        return WebMisc().wait_element(driver, self.forgot_password, "forgot_password")

    def get_new_password_confirmation(self, driver):
        return WebMisc().wait_element(driver, self.new_password_confirmation, "new_password_confirmation")

    def get_google_login(self, driver):
        return WebMisc().wait_element(driver, self.google_login, "google_login")

    def get_sign_up_here(self, driver):
        return driver.find_element(By.CSS_SELECTOR, "span.signup-pw")

    def get_red_banner(self, driver):
        return driver.find_element(By.XPATH, self.red_banner)

    def get_apple_login(self, driver):
        return WebMisc().wait_element(driver, self.apple_login, "apple_login")
