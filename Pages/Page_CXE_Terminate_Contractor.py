from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time


class CXETerminateContractor:

    contractor = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[3]/section/div[1]/h3/button/p/span"
    start_service = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[3]/section/div[2]/div/a[1]"
    modify_service = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[3]/section/div[2]/div/a[2]"
    reactivate_service = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[3]/section/div[2]/div/a[3]"
    stop_service = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[3]/section/div[2]/div/a[4]"
    stop_lbl = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/h2"
    CAN = "//div/div[2]/div[1]/div/div/div/div/input"
    SIN = "//div[2]/div/div/div/div/input"
    firstname = "//div/div[2]/div[3]/div[1]/div/div/div/input"
    lastname = "//div[2]/div/div/div/input"
    emailaddress = "//div[3]/div[4]/div/div/div/input"
    mobile_number = "//div[5]/div/div/div/input"
    businessname = "//div[3]/div[3]/div/div/div/input"
    next1 = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div[2]/div[4]/button"
    terms_cond = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div[3]/div[1]/div[3]/div/label/div"
    yes = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/label/div"
    submit = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div[3]/div[3]/button"


    def  get_businessname(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.businessname)))

    def get_SIN(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.SIN)))
    def  get_submit(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.submit)))
    def  get_yes(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.yes)))
    def get_terms_cond(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.terms_cond)))

    def get_terms_cond(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.terms_cond)))
    def get_next1(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.next1)))
    def get_mobile_number(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.mobile_number)))
    def get_emailaddress(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.emailaddress)))

    def get_lastname(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.lastname)))



    def get_firstname(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.firstname)))

    def get_CAN(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.CAN)))

    def get_stop_lbl(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.stop_lbl)))
    def get_stop_service_clk(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.stop_service)))

    def get_stop_service(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.stop_service)))

    def get_reactivate_service(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.reactivate_service)))

    def get_contractor(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.contractor)))

    def get_modify_service(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.modify_service)))

    def get_start_service(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.start_service)))




