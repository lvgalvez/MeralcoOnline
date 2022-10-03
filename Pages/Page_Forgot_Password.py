
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time


class ForgotPasswordPage:
    email = "//input[@id = '114:2;a']"
    send_confirmation_email = "//button[@data-aura-rendered-by= '135:2;a']"
    email_sent = "//h3[@data-aura-rendered-by= '152:2;a']"


    def get_email(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.email)))

    def get_send_confirmation_email(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.send_confirmation_email)))

    def get_email_sent(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.email_sent)))
