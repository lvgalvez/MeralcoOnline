from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class CXEApplyBusinessRegPage:
    lbl_start_service = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/h4"
    company_name = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div/input"
    trade_name = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[1]/div/div/input"
    company_email = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[1]/div/div/input"
    company_landline = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[3]/div/div/input"
    first_name = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[3]/div[1]/div/div/input"
    last_name = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[3]/div[2]/div/div/input"
    email_address = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[4]/div/div/div/input"
    mobile_number = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[5]/div[1]/div/div/input"
    designation = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[5]/div[2]/div/div/input"
    btn_next = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[6]/div/button"
    btn_next2 = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[4]/div/button"
    btn_next3 = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div/div[5]/button"
    lbl_new_address = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/ul/li[2]/a"

    inp_serv_add = "//input[@class = 'slds-input mov-input-trackmyapp input']"
    clk_province = "//select[@class = 'slds-select mov-select-aftersales mov-text_color-afafaf select']"
    clk_prnc_value = "//option[@value = 'METRO MANILA']"
    clk_munciplity = "//select[@class = 'slds-select mov-select-aftersales mov-text_color-afafaf slds-select inline select']"
    clk_mciplity_val = "//option[@value = 'CALOOCAN CITY']"
    clk_radio_yes = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[3]/div/div/label[1]/span"
    value_added = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/ul/li[3]/a"
    service_address = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div/div/div/input"
    clk_term_condition = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[4]/div/div[3]/div[2]/div[1]/label/div"
    submit = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[4]/div/div[3]/div[2]/div[3]/button"
    confirmation = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[5]/div/div/div[1]/h3"
    cxe_apply_can = "//div[1]/div/div/div/div/div/div/div[2]/div/input"
    cxe_change_contract = "//div[4]/div/div/div[2]/div/label/div"
    cxe_change_contract_name = "//div[4]/div/div/div[2]/div[2]/input[1]"
    cxe_company_name = "//div[6]/div[1]/div/div/input"
    cxe_landline = "//div[7]/div[1]/div/div/input"
    cxe_firstname = "//div[8]/div[1]/div/div/input"
    cxe_lastname = "//div[8]/div[2]/div/div/input"
    cxe_email_add = "//div[9]/div[1]/div/div/input"
    cxe_mobile_num = "//div[9]/div[2]/div/div/input"
    cxe_designation = "//div[9]/div[3]/div/div/input"
    cxe_modify_next_btn = "//div[10]/div/button"
    cxe_contact_firstname = "//div[2]/div/div/div/div/div/div/div[1]/div[1]/div/div/input"
    cxe_contact_lastname = "//div[2]/div/div/div/div/div/div/div[1]/div[3]/div/div/input"
    cxe_contact_email = "//div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/input"
    cxe_contact_mobile = "//div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/input"
    cxe_contact_next_btn = "//div/div/div[3]/div/button"
    cxe_addedServ_next_btn = "//div[2]/div/div/div[3]/div/div/div[5]/button"
    cxe_terms_conditions = "//div/div/div[4]/div/div[3]/div[2]/div[1]/label/div"
    cxe_submit = "//div/div/div[4]/div/div[3]/div[2]/div[3]/button"


    def get_submit(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.submit)))

    def get_click_term_condition(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.clk_term_condition)))

    def get_inp_serv_add(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.service_address)))

    def get_btn_next3(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.btn_next3)))

    def get_value_added(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.value_added)))

    def get_confirmation(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.confirmation)))

    def get_clk_radio(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_radio_yes)))

    def get_clk_province(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_province)))

    def get_province_value(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_prnc_value)))

    def get_municipality(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_munciplity)))

    def get_clk_mciplity_val(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.clk_mciplity_val)))

    def get_company_name(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.company_name)))

    def get_lbl_new_address(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.lbl_new_address)))

    def get_next(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.btn_next)))

    def get_next2(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.btn_next2)))


    def get_trade_name(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.trade_name)))

    def get_company_email(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.company_email)))

    def get_company_landline(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.company_landline)))

    def get_first_name(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_email_address(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.email_address)))

    def get_mobile(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.mobile_number)))

    def get_designation(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.designation)))

    def get_lbl_start_service(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.lbl_start_service)))

    def get_can_cxe_modify(self, driver):
        return WebMisc().wait_element(driver, self.cxe_apply_can, "cxe_apply_can")

    def get_change_contract(self, driver):
        return WebMisc().wait_element(driver, self.cxe_change_contract, "cxe_change_contract")

    def get_change_contract_name(self, driver):
        return WebMisc().wait_element(driver, self.cxe_change_contract_name, "cxe_change_contract_name")

    def get_company_name(self, driver):
        return WebMisc().wait_element(driver, self.cxe_company_name, "cxe_company_name")

    def get_landline(self, driver):
        return WebMisc().wait_element(driver, self.cxe_landline, "cxe_landline")

    def get_firstname(self, driver):
        return WebMisc().wait_element(driver, self.cxe_firstname, "cxe_firstname")

    def get_lastname(self, driver):
        return WebMisc().wait_element(driver, self.cxe_lastname, "cxe_lastname")

    def get_email(self, driver):
        return WebMisc().wait_element(driver, self.cxe_email_add, "cxe_email_add")

    def get_mobile_num(self, driver):
        return WebMisc().wait_element(driver, self.cxe_mobile_num, "cxe_mobile_num")

    def get_cxe_designation(self, driver):
        return WebMisc().wait_element(driver, self.cxe_designation, "cxe_designation")

    def get_modify_next_btn(self, driver):
        return WebMisc().wait_element(driver, self.cxe_modify_next_btn, "cxe_modify_next_btn")

    def get_modify_contact_firstname(self, driver):
        return WebMisc().wait_element(driver, self.cxe_contact_firstname, "cxe_contact_firstname")

    def get_modify_contact_lastname(self, driver):
        return WebMisc().wait_element(driver, self.cxe_contact_lastname, "cxe_contact_lastname")

    def get_modify_contact_email(self, driver):
        return WebMisc().wait_element(driver, self.cxe_contact_email, "cxe_contact_email")

    def get_modify_contact_mobilenum(self, driver):
        return WebMisc().wait_element(driver, self.cxe_contact_mobile, "cxe_contact_mobile")

    def get_modify_contact_next_btn(self, driver):
        return WebMisc().wait_element(driver, self.cxe_modify_next_btn, "cxe_modify_next_btn")

    def get_modify_addedServ_next_btn(self, driver):
        return WebMisc().wait_element(driver, self.cxe_addedServ_next_btn, "cxe_addedServ_next_btn")

    def get_modify_terms_conditions(self, driver):
        return WebMisc().wait_element(driver, self.cxe_terms_conditions, "cxe_terms_conditions")

    def get_modify_submit(self, driver):
        return WebMisc().wait_element(driver, self.cxe_submit, "cxe_submit")
