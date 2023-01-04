from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time


class CXEReactivateBusiness:

    individual = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[1]/section/div[1]/h3/button/p"
    start_service = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[2]/section/div[2]/div/a[1]"
    modify_service = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[2]/section/div[2]/div/a[2]"
    reactivate_service = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[2]/section/div[2]/div/a[3]"
    stop_service = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[2]/section/div[2]/div/a[4]"
    stop_lbl = "//*[@id='request_to_modify']/div/div/div/div/h4"
    CAN = "//div[1]/div/div[1]/div/input"
    SIN = "//div/div/div/div/div/div[2]/div[1]/div/div[2]/div/input"
    firstname = "//div[3]/div/div[1]/div/div/input"
    lastname = "//div[3]/div/div[2]/div/div/input"
    emailaddress = "//div[4]/div/div[1]/div/div/input"
    mobile_number = "//div[4]/div/div[2]/div/div/input"
    next1 = "//*[@id='request_to_modify']/div/div/div/div/div[2]/div[5]/div/button"
    terms_cond = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/ul/li[3]/a"
    yes = "//*[@id='value_add_services']/div/div[5]/button"
    submit = "//*[@id='terms_and_conditions']/div/div[2]/div[3]/button"
    business = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[2]/section/div[1]/h3/button/p"
    designation = "//div/div/div/div/div/div[2]/div[4]/div/div[3]/div/div/input"
    companyname = "//div/div/div/div/div/div[2]/div[2]/div[1]/div/div/input"
    landline = "//div/div/div[1]/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/input"
    valueadd = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/ul/li[2]/a"
    terms_cond_clk = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[3]/div/div[2]/div[1]/label/div"

    def  get_terms_cond_clk(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.terms_cond_clk)))
    def  get_SIN(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.SIN)))
    def  get_value_add(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.valueadd)))
    def  get_landline(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.landline)))
    def  get_companyname(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.companyname)))
    def  get_designation(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.designation)))
    def  get_business(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.business)))
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

    def get_middlename(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.middlename)))

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

    def get_individual(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.individual)))

    def get_modify_service(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.modify_service)))

    def get_start_service(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.start_service)))




