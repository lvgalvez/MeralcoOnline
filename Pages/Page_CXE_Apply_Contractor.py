from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class CXEApplyContractor:
    label_service_application = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[1]/div/h3"
    popup_no = "//a[@class = 'slds-button mov-button mov-element_max-width-170 mov-text_weight-bold CXE_marginCentralizer custom-btn2']"
    contractor = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[3]/section/div[1]/h3/button/p"
    contractor_start = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[3]/section/div[2]/div/a[1]"
    contractor_modify = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[3]/section/div[2]/div/a[2]"
    contractor_reactivate = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[3]/section/div[2]/div/a[3]"
    contractor_stop = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[3]/section/div[2]/div/a[4]"
    clk_contractor_start = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[3]/section/div[2]/div/a[1]"
    clk_contractor = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div/div/div[3]/a"
    first_name = "//div[1]/div/div/div/input"
    last_name = "//div[1]/div[2]/div/div/div/input"
    business_name = "//div[2]/div[1]/div[3]/div/div/div/input"
    email_address = "//div[2]/div[1]/div[4]/div/div/div/input"
    phone_number = "//input[@placeholder='+639xxxxxxxxx']"
    next_button = "//button[contains(text(), 'Next')]"
    can_input = "//input[@placeholder='1234567890']"
    last_name_recontract = "//div[3]/div/div/div/input"



    def get_popup_no(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.popup_no)))

    def get_label_service_application(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.label_service_application)))

    def get_clk_contractor_start(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.clk_contractor_start)))

    def get_contractor_stop(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.contractor_stop)))
    def get_contractor_reactivate(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.contractor_reactivate)))

    def get_contractor_modify(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.contractor_modify)))

    def get_contractor(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.contractor)))

    def get_contractor_start(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.contractor_start)))
    def get_clk_contractor(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.clk_contractor)))

    def get_first_name(self, driver):
        return WebMisc().wait_element(driver, self.first_name, "first_name")

    def get_last_name(self, driver):
        return WebMisc().wait_element(driver, self.last_name, "last_name")

    def get_business_name(self, driver):
        return WebMisc().wait_element(driver, self.business_name, "business_name")

    def get_email_address(self, driver):
        return WebMisc().wait_element(driver, self.email_address, "email_address")

    def get_phone_number(self, driver):
        return WebMisc().wait_element(driver, self.phone_number, "phone_number")

    def get_next_button(self, driver):
        return WebMisc().wait_element(driver, self.next_button, "next_button")

    def get_can_input(self, driver):
        return WebMisc().wait_element(driver, self.can_input, "can_input")

    def get_last_name_recontract(self, driver):
        return WebMisc().wait_element(driver, self.last_name_recontract, "last_name_recontract")


