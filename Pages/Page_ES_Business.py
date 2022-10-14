from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time


class CXEEsBusiness:
    click_next = "//*[@id='tab-2']/div/div[5]/div/button"
    change_contract_name = "//*[@id='62:586;a']"
    value_added = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/ul/li[2]/a"
    radio_yes = "//*[@id='tab-2']/div/div[2]/div[2]/div/label[1]/div"
    next = "//*[@id='tab-1']/div/div[2]/div/button"
    term_condition = "//*[@id='tab-3']/div[3]/div[2]/div/label/div"
    submit = "//*[@id='tab-3']/div[3]/div[4]/div/button"


    def get_next2(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.next)))
    def get_submit(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.submit)))

    def get_click_term_condition(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.term_condition)))

    def get_next(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.click_next)))

    def get_radio_yes(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.radio_yes)))

    def get_value_added(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.value_added)))


    def get_change_contract_name(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.change_contract_name)))


