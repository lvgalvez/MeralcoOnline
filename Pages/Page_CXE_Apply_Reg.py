from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time


class CXEApplyRegPage:
    new_account = "//h3[@data-aura-rendered-by = '263:2;a']"
    email = "//input[@id = '268:2;a']"
    first_name = "//input[@id = '278:2;a']"
    middle_name = "//input[@id = '295:2;a']"
    last_name = "//input[@id = '305:2;a']"
    mobile_number = "//input[@id = '327:2;a']"
    terms_condition = "//div[@data-aura-rendered-by = '354:2;a']"
    register = "//button[@data-aura-rendered-by = '360:2;a']"
    confirmation = "//p[contains(text(), 'sent you a confirmation email')]"

    def get_new_account(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.new_account)))

    def get_email(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.email)))

    def get_first_name(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.first_name)))

    def get_middle_name(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.middle_name)))

    def get_last_name(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.last_name)))

    def get_mobile_number(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.mobile_number)))

    def get_terms_condition(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.terms_condition)))

    def get_register(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.register)))

    def get_confirmation(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.confirmation)))
