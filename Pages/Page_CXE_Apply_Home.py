from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class CXEApplyHomePage:
    label_service_application = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[1]/div/h3"
    peccbm = "//div[@id='modal-content-id-1']"
    popup_no = "//a[@class = 'slds-button mov-button mov-element_max-width-170 mov-text_weight-bold CXE_marginCentralizer custom-btn2']"
    popup_yes = "//div/div[1]/div/div/div[2]/div/div[1]/div/div/div[2]/a[1]"
    individual = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[1]/section/div[1]/h3/button/p"
    individual_start = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[1]/section/div[2]/div/a[1]"
    individual_modify = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[1]/section/div[2]/div/a[2]"
    individual_reactivate = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[1]/section/div[2]/div/a[3]"
    individual_stop = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[1]/section/div[2]/div/a[4]"




    def get_label_service_application(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.label_service_application)))

    def get_individual(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.individual)))

    def get_individual_start(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.individual_start)))

    def get_individual_modify(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.individual_modify)))

    def get_individual_reactivate(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.individual_reactivate)))

    def get_individual_stop(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.individual_stop)))

    def get_popup_no(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.popup_no)))

    def get_popup_yes(self, driver):
        return WebMisc().optional_clickable_element(driver, self.popup_yes, "popup_yes")

    def get_peccbm(self, driver):
        return WebMisc().optional_clickable_element(driver, self.peccbm, "peccbm")
