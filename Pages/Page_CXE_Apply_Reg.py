from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time


class CXEApplyRegPage:
    new_account = "/html/body/div[3]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/h3"
    email = "//*[@id='267:2;a']"
    first_name = "//*[@id='277:2;a']"
    middle_name = "//*[@id='294:2;a']"
    last_name = "//*[@id='304:2;a']"
    mobile_number = "//*[@id='326:2;a']"
    birthday = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[4]/div[3]/div/div/div/input"
    terms_condition = "/html/body/div[3]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[6]/div/div[1]/label/div"
    register = "/html/body/div[3]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[6]/div/div[2]/div[1]/button"
    confirmation = "/html/body/div[3]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]"

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

    def get_birthday(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.birthday)))

    def get_terms_condition(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.terms_condition)))

    def get_register(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.register)))

    def get_confirmation(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.confirmation)))
