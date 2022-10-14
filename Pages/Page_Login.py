
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time


class LoginPage:
    email = "//input[@class = 'slds-input mov-input custom-email input uiInput uiInputText uiInput--default uiInput--input']"
    password = "//input[@class = 'slds-input mov-input custom-email input uiInput uiInputSecret uiInput--default uiInput--input']"
    log_in = "//button[@class = 'slds-button slds-button--neutral slds-button mov-button mov-button_login uiButton']"
    forgot_password = "//span[@data-aura-rendered-by = '168:2;a']"
    new_password_confirmation = "//strong[@data-aura-rendered-by = '4:95;a']"


    def get_email(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.email)))

    def get_password(self, driver):
        return driver.find_element(By.XPATH, self.password)

    def get_log_in(self, driver):
        return driver.find_element(By.XPATH, self.log_in)

    def get_forgot_password(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.forgot_password)))


    def get_new_password_confirmation(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.new_password_confirmation)))

