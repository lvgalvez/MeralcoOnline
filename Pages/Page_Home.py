
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time


class HomePage:
    hello_message = "//h3[@class = 'mov-text_size-24 mov-text_weight-bold']"
    request_tile = "//h3[contains(text(), 'REQUEST FOR A SERVICE')]"
    label_start_serv = "//h4[@class = 'slds-m-bottom_large mov-text_size-32 mov-text_weight-semi-bold']"
    account = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[2]/div/div/div[2]/div[6]/div/div/div[2]/div/a[3]"
    popupNO = "//*[@id='modal-content-id-1']/div[2]/a[2]"

    def get_popupNO(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.popupNO)))
    def get_account(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.account)))

    def get_request_tile(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.request_tile)))

    def get_label_start_serv(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.label_start_serv)))


    def get_hello_message(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.hello_message)))
