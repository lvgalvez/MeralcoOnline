
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time


class ResetPasswordPage:
    new_password = "//input[@id = '527:2;a']"
    confirm_password = "//input[@id = '555:2;a']"
    set_password = "//button[@data-aura-rendered-by= '612:2;a']"


    def get_new_password(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.new_password)))

    def get_confirm_password(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.confirm_password)))

    def get_set_password(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.set_password)))
