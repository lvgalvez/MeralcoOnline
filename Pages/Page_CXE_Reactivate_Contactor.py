from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time


class CXEReactivateContractor:
    contractor = "//div/div/div/div[2]/ul/li[3]/section/div[1]/h3/button/p/span"
    start_service = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[3]/section/div[2]/div/a[1]"
    modify_service = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[3]/section/div[2]/div/a[2]"
    reactivate_service = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[3]/section/div[2]/div/a[3]"
    stop_service = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[3]/section/div[2]/div/a[4]"
    stop_lbl = "//*[@id='request_to_modify']/div/div/div/div/h4"
    CAN = "//div/div[3]/div[1]/div/div/div/div/input"
    SIN = "//div[2]/div/div/div/div/input"
    firstname = "//div[1]/div[1]/div/div/div/input"
    lastname = "//div/div[2]/div[1]/div[2]/div/div/div/input"
    emailaddress = "//div/div[2]/div[1]/div[4]/div/div/div/input"
    mobile_number = "//div/div[2]/div[1]/div[5]/div/div/div/input"
    next1 = "//div/div/div/div/div/div/div[2]/div/div[2]/div[2]/button"
    terms_cond = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/ul/li[3]/a"
    yes = "//*[@id='value_add_services']/div/div[5]/button"
    submit = "//*[@id='terms_and_conditions']/div/div[2]/div[3]/button"
    business = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[2]/section/div[1]/h3/button/p"
    designation = "//div/div/div/div/div/div[2]/div[4]/div/div[3]/div/div/input"
    companyname = "//div/div/div/div/div/div[2]/div[2]/div[1]/div/div/input"
    landline = "//div/div/div[1]/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/input"
    valueadd = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/ul/li[2]/a"
    terms_cond_clk = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[3]/div/div[2]/div[1]/label/div"
    businessname = "//div/div[2]/div[1]/div[3]/div/div/div/input"
    reactivate_page = "//div/div/div/div/div[2]/div/h2"
    customer_info = "//div/div/div/div/div/div/div[2]/div/div[1]/div/ol/li[2]/p"
    next2 = "//div/div/div/div/div/div/div[2]/div/div[3]/div[6]/button"

    firstname_cust = "//div[4]/div/div[1]/div/div/div/input"
    lastname_cust = "//div[4]/div/div[3]/div/div/div/input"
    emailaddress_cust = "//div[4]/div/div[4]/div/div/div/input"
    mobile_number_cust = "//div/div[6]/div/div/div/input"
    new_address = "//div/div/div/div/div/div/div[2]/div/div[4]/h3"

    province = "//div[1]/div[2]/div[1]/div/select"
    city = "//div/div[4]/div[1]/div[2]/div[2]/div/select"
    ownership = "//div/div[4]/div[1]/div[3]/div/div/select"



    def get_ownership(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.ownership)))
    def get_city(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.city)))
    def get_province(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.province)))
    def get_new_address(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.new_address)))
    def get_next2(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.next2)))
    def get_cust_info(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.customer_info)))

    def get_reactivate_page(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.reactivate_page)))
    def get_businessname(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.businessname)))

    def get_contractor(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.contractor)))

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
    def get_mobile_number_cust(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.mobile_number_cust)))
    def get_emailaddress(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.emailaddress)))

    def get_emailaddress_cust(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.emailaddress_cust)))
    def get_lastname(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.lastname)))
    def get_lastname_cust(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.lastname_cust)))

    def get_middlename(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.middlename)))

    def get_firstname(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.firstname)))

    def get_firstname_cust(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.firstname_cust)))

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




