from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc

class CXETerminateIndividual:

    individual = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[1]/section/div[1]/h3/button/p"
    start_service = "//*[@id='accordion-details-01']/div/a[1]"
    modify_service = "//*[@id='accordion-details-01']/div/a[2]"
    reactivate_service = "//*[@id='accordion-details-01']/div/a[3]"
    stop_service = "//*[@id='accordion-details-01']/div/a[4]"
    stop_lbl = "//*[@id='request_to_modify']/div/div/div/div/div/h3[1]"
    CAN = "//div[2]/div[1]/div/input"
    SIN = "//input[@placeholder= 'Service ID Number']"
    firstname = "//input[@placeholder= 'First Name']"
    lastname = "//input[@placeholder= 'Last Name']"
    emailaddress = "//input[@placeholder= 'Email Address']"
    mobile_number = "//input[@placeholder= 'Mobile Number']"
    next1 = "//*[@id='request_to_modify']/div/div/div/div/div/div[6]/div/button"
    terms_cond = "//*[@id='terms_and_conditions']/div[2]/div[2]/label/div"
    yes = "//div[2]/div[2]/div[2]/label/div"
    submit = "//*[@id='terms_and_conditions']/div[2]/div[4]/button"
    next_button = "//button[contains(text(), 'Next')]"

    def get_SIN(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.SIN)))
    def  get_submit(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.submit)))
    def  get_yes(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.yes)))
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

    def get_next_button(self, driver):
        return WebMisc().wait_element(driver, self.next_button, "next_button")


