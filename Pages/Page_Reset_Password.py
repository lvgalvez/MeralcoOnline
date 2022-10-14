
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time


class ResetPasswordPage:
    new_password = "//*[@id='526:2;a']"
    confirm_password = "//*[@id='554:2;a']"
    set_password = "/html/body/div[3]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div/div[1]/div[3]/table/tr[2]/td[2]/button"


    def get_new_password(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.new_password)))

    def get_confirm_password(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.confirm_password)))

    def get_set_password(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.set_password)))
