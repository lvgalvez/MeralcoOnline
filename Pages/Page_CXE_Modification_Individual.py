from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time


class CXEModificationIndividual:

    individual = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[1]/section/div[1]/h3/button/p/span"
    business = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[2]/section/div[1]/h3/button/p"
    start_service = "//*[@id='accordion-details-02']/div/a[1]"
    modify_service = "//*[@id='accordion-details-02']/div/a[2]"
    reactivate_service = "//*[@id='accordion-details-02']/div/a[3]"
    stop_service = "//*[@id='accordion-details-02']/div/a[4]"
    modify_service_clk = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/ul/li[1]/section/div[2]/div/a[2]"
    request = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/h3"
    CAN = "//*[@id='503:0']"
    SIN = "//*[@id='513:0']"
    change_contract_details = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div[4]/div/div/div[2]/div[1]/label/div"
    change_contract_name = "/html/body/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div[4]/div/div/div[2]/div[2]/input[1]"

    company_name = "//input[@placeholder= 'Meralco']"
    landline = "//input[@placeholder= '+6321234567']"
    first_name = "//input[@placeholder= 'Juan']"
    last_name = "//input[@placeholder= 'Dela Cruz']"
    emailddress = "//input[@placeholder= 'juan@meralco.com']"
    mobile_number = "//input[@placeholder= '+639123456789']"
    designation = "//input[@placeholder= 'Manager*']"

    next1 = "//*[@id='tab-1']/div/div/div/div/div/div[8]/div/button"
    contact_info = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/ul/li[2]/a"
    next2 = "//*[@id='tab-2']/div/div/div/div/div/div[3]/div/button"

    first_name_mod = "//*[@id='571:0']"
    last_name_mod = "//*[@id='591:0']"
    emailddress_mod = "//*[@id='602:0']"
    mobile_number_mod = "//*[@id='612:0']"

    value_added = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/ul/li[3]/a"

    yes = "//*[@id='value_add_services']/div/div[2]/div[2]/div/label[1]/span"
    next3 = "//*[@id='value_add_services']/div/div[5]/button"
    terms_condition = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/ul/li[4]/a"
    term_condition_clk = "//*[@id='tab-4']/div[3]/div[2]/div[1]/label/div"
    submit = "//*[@id='tab-4']/div[3]/div[2]/div[3]/button"
    confirmation = "//*[@id='confirmation']/div/div[1]/h3"


    def get_confirmation(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.confirmation)))

    def get_SIN(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.SIN)))

    def get_individual(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.individual)))


    def get_submit(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.submit)))

    def get_click_term_condition(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.term_condition_clk)))
    def get_terms_condition(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.terms_condition)))

    def get_next3(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.next3)))
    def get_yes(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.yes)))

    def get_value_added(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.value_added)))

    def get_first_name_mod(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.first_name_mod)))

    def get_last_name_mod(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.last_name_mod)))

    def get_emailddress_mod(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.emailddress_mod)))

    def get_mobile_number_mod(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.mobile_number_mod)))


    def get_next2(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.next2)))

    def get_contact_info(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.contact_info)))
    def get_next1(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.next1)))
    def get_designation(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.designation)))

    def get_mobile_number(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.mobile_number)))

    def get_emailaddress(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.emailddress)))
    def get_last_name(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.last_name)))
    def get_first_name(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_landline(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.landline)))


    def get_company_name(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.company_name)))
    def get_change_contract_name(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.change_contract_name)))

    def get_change_contract_details(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.change_contract_details)))


    def get_CAN(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.CAN)))
    def get_request(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.request)))

    def get_modify_service_clk(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.modify_service_clk)))

    def get_stop_service(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.stop_service)))

    def get_reactivate_service(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.reactivate_service)))

    def get_modify_service(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.modify_service)))


    def get_start_service(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.start_service)))


    def get_business(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.business)))






