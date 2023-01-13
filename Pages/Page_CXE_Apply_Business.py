from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time


class CXEApplyBusiness:
    label_service_application = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[1]/div/h3"
    popup_no = "//a[@class = 'slds-button mov-button mov-element_max-width-170 mov-text_weight-bold CXE_marginCentralizer custom-btn2']"
    business = "//div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[2]/section/div[1]/h3/button/p"
    business_start = "//div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[2]/section/div[2]/div/a[1]"
    business_modify = "//div[2]/ul/li[2]/section/div[2]/div/a[2]"
    business_reactivate = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[2]/section/div[2]/div/a[1]"
    business_stop = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[2]/section/div[2]/div/a[1]"
    clk_business_start = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[2]/section/div[2]/div/a[1]"
    popup_no = "//a[@class = 'slds-button mov-button mov-element_max-width-170 mov-text_weight-bold CXE_marginCentralizer custom-btn2']"


    def get_popup_no(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.popup_no)))

    def get_clk_business_start(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.clk_business_start)))

    def get_business_stop(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.business_stop)))
    def get_business_reactivate(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.business_reactivate)))

    def get_business_modify(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.business_modify)))

    def get_business(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.business)))

    def get_business_start(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.business_start)))

    def get_popup_no(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.popup_no)))




