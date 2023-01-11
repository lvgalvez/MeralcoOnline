from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class CXELoginPage:
    meralco_user_id = "//button[contains(@class, 'secondary wide') and span[contains(text(), 'Meralco User ID')]]"
    use_another_account ="//div[contains(text(), 'Use another account')]"
    email = "//input[@class = 'form-control ltr_override input ext-input text-box ext-text-box']"
    next = "//input[@class = 'win-button button_primary button ext-button primary ext-primary']"
    password = "//input[@class = 'form-control input ext-input text-box ext-text-box']"
    sign_in = "//input[@value= 'Sign in']"
    stay_sign_no = "//input[@class= 'win-button button-secondary button ext-button secondary ext-secondary']"
    sms = "//div[2]/div/div[2]/div/div[3]/div/div/div[2]"
    loginBtn = "//*[@id='mainAppBody']/div[2]/md-content/md-card/md-card-content/form/button"

    def get_meralco_user_id(self, driver):
        return WebMisc().optional_wait_element(driver, self.meralco_user_id, "meralco_user_id")
    def get_sms(self, driver):
        return WebMisc().optional_wait_element(driver, self.sms, "sms")

    def get_use_another_account(self, driver):
        return WebMisc().wait_element(driver, self.use_another_account, "use_another_account")

    def get_email(self, driver):
        return WebMisc().wait_element(driver, self.email, "email")

    def get_next(self, driver):
        return WebMisc().wait_element(driver, self.next, "next")

    def get_password(self, driver):
        return WebMisc().wait_element(driver, self.password, "password")

    def get_sign_in(self, driver):
        return WebMisc().wait_element(driver, self.sign_in, "sign_in")

    def get_stay_sign_no(self, driver):
        return WebMisc().optional_wait_element(driver, self.stay_sign_no, "stay_sign_no")

    def get_default_login(self,driver):
        return WebMisc().optional_clickable_element(driver, self.loginBtn, "loginBtn")
