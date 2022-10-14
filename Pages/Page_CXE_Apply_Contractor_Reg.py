from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time


class CXEApplyContractorRegPage:
    lbl_start_service = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/h2"
    trade_name = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[1]/div/div/input"
    first_name = "//*[@id='179:2;a']"
    last_name = "//*[@id='194:2;a']"
    first_name_customer = "//*[@id='331:2;a']"
    last_name_customer = "//*[@id='359:2;a']"
    middle_name = "//*[@id='344:2;a']"
    email_address = "//*[@id='224:2;a']"
    email_address_customer = "//*[@id='374:2;a']"
    mobile_number = "//*[@id='239:2;a']"
    mobile_number_customer = "//*[@id='411:2;a']"
    designation = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[5]/div[2]/div/div/input"
    btn_next = "//*[@id='conIndStartForm1']/div[2]/button"
    btn_next2 = "//*[@id='conIndStartForm2']/div[4]/button"
    btn_next3 = "//*[@id='tab-3']/div[3]/button"
    lbl_new_address = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/ol/li[3]/p"
    inp_serv_add = "//*[@id='507:2;a']"
    clk_province = "//*[@id='528:2;a']"
    clk_prnc_value = "//option[@value = 'METRO MANILA']"
    clk_munciplity = "//*[@id='544:2;a']"
    clk_mciplity_val = "//option[@value = 'CALOOCAN CITY']"
    clk_radio_yes = "//*[@id='tab-3']/div[1]/div[4]/div/div/span/div/label[1]/span"
    terms_condition = "//*[@id='tab-4']/div[3]/div[1]/h3"
    service_address = "//*[@id='507:2;a']"
    clk_term_condition = "//*[@id='tab-4']/div[3]/div[2]/div/label/div"
    submit = "//*[@id='tab-4']/div[5]/button"
    confirmation = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div[6]/div[2]/button"
    business_name = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div/div/input"
    birthday = "//*[@id='389:2;a']"
    clk_ownership = "//*[@id='561:2;a']"
    clk_ownshp_val = "//option[@value = 'Owned']"

    def get_clk_ownership(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_ownership)))

    def get_clk_ownership_value(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_ownshp_val)))


    def get_first_name_cus(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.first_name_customer)))

    def get_last_name_cus(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.last_name_customer)))

    def get_email_address_cus(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.email_address_customer)))

    def get_mobile_cus(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.mobile_number_customer)))

    def get_birthday(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.birthday)))
    def get_middle_name(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.middle_name)))
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

    def get_terms_condition(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.terms_condition)))

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

    def get_first_name(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_lbl_new_address(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.lbl_new_address)))

    def get_next(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.btn_next)))

    def get_next2(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.btn_next2)))

    def get_businessName(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.business_name)))


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
