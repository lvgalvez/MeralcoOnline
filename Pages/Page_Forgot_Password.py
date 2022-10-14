
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class ForgotPasswordPage:
    email = "//input[@id = '114:2;a']"
    send_confirmation_email = "//button[@data-aura-rendered-by= '135:2;a']"
    email_sent = "//h3[@data-aura-rendered-by= '152:2;a']"
    sso_forgot = "//li[@class = 'form-element__help']"


    def get_email(self, driver):
        return WebMisc().wait_element(driver, self.email, "email")

    def get_send_confirmation_email(self, driver):
        return WebMisc().wait_element(driver, self.send_confirmation_email, "send_confirmation_email")

    def get_email_sent(self, driver):
        return WebMisc().wait_element(driver, self.email_sent, "email_sent")

    def get_sso_forgot(self, driver):
        return WebMisc().wait_element(driver, self.sso_forgot, "sso_forgot")


