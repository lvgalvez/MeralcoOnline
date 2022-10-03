from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time


class CXEApplyHomePage:
    label_service_application = "//h3[@data-aura-rendered-by = '88:2;a']"
    popup_no = "//a[@class = 'slds-button mov-button mov-element_max-width-170 mov-text_weight-bold CXE_marginCentralizer custom-btn2']"
    individual = "//p[@data-aura-rendered-by = '100:2;a']"
    individual_start = "//a[@data-aura-rendered-by = '113:2;a']"
    individual_modify = "//a[@data-aura-rendered-by = '116:2;a']"
    individual_reactivate = "//a[@data-aura-rendered-by = '119:2;a']"
    individual_stop = "//a[@data-aura-rendered-by = '122:2;a']"

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

    #def get_popup_no(self, driver):
    #    return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, "//a[starts-with(@onclick,'toIndexHtml')]")))

    def get_popup_no(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.popup_no)))


