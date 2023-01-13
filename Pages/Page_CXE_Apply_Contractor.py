from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
    "//div[1]/div/div/div/input"
    last_name = "//div[1]/div[2]/div/div/div/input"
    business_name = "//div[2]/div[1]/div[3]/div/div/div/input"
    email_address = "//div[1]/div[4]/div/div/div/input"
    phone_number = "//input[@placeholder='+639xxxxxxxxx']"
    next_button = "//button[contains(text(), 'Next')]"
    can_input = "//input[@placeholder='1234567890']"
    last_name_recontract = "//div[3]/div/div/div/input"
    submit_btn_contractor = "//a[contains(text(), 'Submit')]"
    peccbm = "//div[2]/div/div[1]/div/div/div[2]/div/div[1]/div/div/div[1]/label[1]/div"
    applying_as = "//div[2]/div/div[1]/div/div/div[2]/div/div[1]/div/div"
    cxe_apply_business_name = "//div[3]/div/div/div/input"
    cxe_apply_firstname = "//div/div[2]/div/div[1]/div/div/div/input"
    cxe_apply_lastname = "//div[2]/div/div[3]/div/div/div/input"
    cxe_apply_email = "//div[2]/div/div[4]/div/div/div/input"
    cxe_apply_birthday = "//div[2]/div/div[5]/div/div/div/div/input"
    cxe_apply_number = "//div[2]/div/div[6]/div/div/div/input"
    cxe_apply_next = "//div[2]/div/div[3]/div/div/div[4]/button"
    cxe_apply_service_add = "//div[4]/div/div[1]/div[1]/div/div/div/input"
    cxe_apply_province = "//div[4]/div/div[1]/div[2]/div[1]/div/select"
    cxe_apply_city = "//div[4]/div/div[1]/div[2]/div[2]/div/select"
    cxe_apply_ownership = "//div[4]/div/div[1]/div[3]/div/div/select"
    cxe_apply_new_add_next_btn = "//div[4]/div/div[3]/button"
    cxe_apply_terms_conditions = "//div[5]/div/div[3]/div[2]/div/label/div"
    cxe_apply_terms_next_btn = "//div/div[5]/div/div[5]/button"

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

    def get_submit_btn(self, driver):
        return WebMisc().wait_element(driver, self.submit_btn_contractor, "submit_btn_contractor")

    def get_business_name_cxe_apply(self, driver):
        return WebMisc().wait_element(driver, self.cxe_apply_business_name, "cxe_apply_business_name")

    def get_firstname_cxe_apply(self, driver):
        return WebMisc().wait_element(driver, self.cxe_apply_firstname, "cxe_apply_firstname")

    def get_lastname_cxe_apply(self, driver):
        return WebMisc().wait_element(driver, self.cxe_apply_lastname, "cxe_apply_lastname")

    def get_email_cxe_apply(self, driver):
        return WebMisc().wait_element(driver, self.cxe_apply_email, "cxe_apply_email")

    def get_birthday_cxe_apply(self, driver):
        return WebMisc().wait_element(driver, self.cxe_apply_birthday, "cxe_apply_birthday")

    def get_mobile_num_cxe_apply(self, driver):
        return WebMisc().wait_element(driver, self.cxe_apply_number, "cxe_apply_number")

    def get_next_btn(self, driver):
        return WebMisc().wait_element(driver, self.cxe_apply_next, "cxe_apply_number")

    def get_service_add(self, driver):
        return WebMisc().wait_element(driver, self.cxe_apply_service_add, "cxe_apply_service_add")

    def get_ownership(self, driver):
        return Select(driver.find_element(By.XPATH, self.cxe_apply_ownership))

    def get_province(self, driver):
        return Select(driver.find_element(By.XPATH, self.cxe_apply_province))

    def get_city(self, driver):
        return Select(driver.find_element(By.XPATH, self.cxe_apply_city))

    def get_new_add_next_btn(self, driver):
        return WebMisc().wait_element(driver, self.cxe_apply_new_add_next_btn, "cxe_apply_new_add_next_btn")

    def get_terms_conditions(self, driver):
        return WebMisc().wait_element(driver, self.cxe_apply_terms_conditions, "cxe_apply_terms_conditions")

    def get_terms_next_btn(self, driver):
        return WebMisc().wait_element(driver, self.cxe_apply_terms_next_btn, "cxe_apply_terms_next_btn")

    def get_peccbm(self, driver):
        return WebMisc().wait_element(driver, self.peccbm, "peccbm")

    def get_applying_us(self, driver):
        return WebMisc().wait_element(driver, self.applying_as, "applying_as")