from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc

class PageService:
    click_next = "//button[@data-aura-class = 'uiButton']"
    label_serv_add = "//h4[@class = 'slds-m-bottom_large mov-text_size-32 mov-text_weight-semi-bold slds-text-align_center']"

    inp_serv_add = "//input[@class = 'slds-input mov-input-trackmyapp input']"
    clk_province = "//select[@class = 'slds-select mov-select-aftersales mov-text_color-afafaf select']"
    clk_prnc_value = "//option[@value = 'METRO MANILA']"
    clk_munciplity = "//select[@class = 'slds-select mov-select-aftersales mov-text_color-afafaf slds-select inline select']"
    clk_mciplity_val = "//option[@value = 'CALOOCAN CITY']"
    clk_ownership = "//select[@class = 'slds-select mov-select-aftersales mov-text_color-afafaf slds-select_container mov-select_container select']"
    clk_reconnect_ownership = "//select[@class = 'slds-select mov-select-aftersales mov-text_color-afafaf select']"
    clk_ownshp_val = "//option[@value = 'Owned']"
    clk_radio_yes = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[4]/div/div/label[1]/span"
    clk_next = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[5]/div/button"
    value_added = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/ul/li[3]/a"
    automatic_payment = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div/div[5]/div[2]/div/label[1]/div"
    attach_docu = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div/div[6]/div/div[1]/div/div/label/span/span"
    clk_next_2 = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div/div[7]/button"
    label_term_condition = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/ul/li[4]/a"
    click_term_condition = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[4]/div/div[3]/div[2]/div[1]/label/div"
    submit = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[4]/div/div[3]/div[2]/div[3]/button"
    iam_not_robot = "/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]"
    birthday = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[4]/div[3]/div/div/div/input"
    next_btn = "//html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[5]/div/button"
    next_service_btn = "//html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div/div[7]/button"
    submit_btn = "//button[contains(text(), 'Submit')]"
    change_service = "//input[@value='Upgrade the kWh']"
    terms_and_conditions = "//html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[4]/div/div[3]/div[2]/div[1]/label/input"
    terms_and_condition_service_details = "//input[@id='agreeChkbx1']"
    terms_and_condition_contract_details = "//input[@id='agreeChkbx2']"
    peccbm_no_radio_btn = "//input[@id='no_radio']"
    change_contract_name = "//input[@value='Change in Contract Name']"
    transfer_service = "//input[@value='Transfer of Service']"
    ok_btn = "//button[contains(text(), 'OK')]"
    next_button = "//button[contains(text(), 'Next')]"
    next_modify_button = "//html/body/div[3]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[5]/div/button"
    submit_modify_button = "//html/body/div[3]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[3]/div/div[3]/div[4]/div/button"
    back_to_home = "//button[contains(text(), 'Back to Home')]"
    submit_modify_contract_button = "//html/body/div[3]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[3]/div/div[3]/div[4]/div/button"
    next_reconnect_button = "//html/body/div[3]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div/div[5]/div/button"
    next_second_recconect_button = "//html/body/div[3]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div[7]/button"
    submit_reconnect_button = "//html/body/div[3]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[4]/div[3]/div/div[2]/div[3]/button"

    def get_birthday(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.birthday)))

    def get_iam_not_robot(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.iam_not_robot)))

    def get_term_condition(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.label_term_condition)))

    def get_click_term_condition(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.click_term_condition)))

    def get_submit(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.submit)))

    def get_clk_next_2(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_next_2)))

    def get_attach_docu(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.attach_docu)))

    def get_value_added(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.value_added)))

    def get_automatic_payment(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.automatic_payment)))

    def get_next(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_next)))

    def get_inp_serv_add(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.inp_serv_add)))

    def get_clk_radio(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_radio_yes)))

    def get_clk_province(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_province)))

    def get_province_value(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_prnc_value)))

    def get_municipality(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_munciplity)))

    def get_clk_mciplity_val(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_mciplity_val)))

    def get_clk_ownership(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_ownership)))

    def get_clk_ownership_value(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_ownshp_val)))

    def get_click_next(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.click_next)))

    def get_label_serv_add(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.label_serv_add)))

    def get_clk_next_btn(self, driver):
        return WebMisc().wait_element(driver, self.next_btn, "next_btn")

    def get_province(self, driver):
        return Select(driver.find_element(By.XPATH, self.clk_province))

    def get_city(self, driver):
        return Select(driver.find_element(By.XPATH, self.clk_munciplity))

    def get_ownership(self, driver):
        return Select(driver.find_element(By.XPATH, self.clk_ownership))

    def get_submit_btn(self, driver):
        return WebMisc().wait_element(driver, self.submit_btn, "submit_btn")

    def get_change_service(self, driver):
        return WebMisc().wait_element(driver, self.change_service, "change_service")

    def get_terms_and_conditions_service_details(self, driver):
        return driver.find_element(By.XPATH, self.terms_and_condition_service_details)

    def get_terms_and_conditions_contract_details(self, driver):
        return driver.find_element(By.XPATH, self.terms_and_condition_contract_details)

    def get_no_radio_btn_peccbm(self, driver):
        return WebMisc().wait_element(driver, self.peccbm_no_radio_btn, "peccbm_no_radio_btn")

    def get_change_contract_radio_btn(self, driver):
        return WebMisc().wait_element(driver, self.change_contract_name, "change_contract_name")

    def get_ok_btn(self,driver):
        return WebMisc().wait_element(driver, self.ok_btn, "ok_btn")

    def get_transfer_service(self, driver):
        return WebMisc().wait_element(driver, self.transfer_service, "transfer_service")

    def get_next_button(self, driver):
        return WebMisc().wait_element(driver, self.next_button, "next_button")

    def get_next_service_btn(self, driver):
        return WebMisc().wait_element(driver, self.next_service_btn, "next_service_btn")

    def get_terms_and_conditions(self, driver):
        return WebMisc().wait_element(driver, self.terms_and_conditions, "terms_and_conditions")

    def get_next_modify_button(self, driver):
        return WebMisc().wait_element(driver, self.next_modify_button, "next_modify_button")

    def get_submit_modify_button(self, driver):
        return WebMisc().wait_element(driver, self.submit_modify_button, "submit_modify_button")

    def get_back_to_home(self, driver):
        return WebMisc().wait_element(driver, self.back_to_home, "back_to_home")

    def get_submit_modify_contract(self, driver):
        return WebMisc().wait_element(driver, self.submit_modify_contract_button, "submit_modify_contract_button")

    def get_reconnect_ownership(self, driver):
        return Select(driver.find_element(By.XPATH, self.clk_reconnect_ownership))

    def get_next_recconect(self, driver):
        return WebMisc().wait_element(driver, self.next_reconnect_button, "next_reconnect_button")

    def get_second_next_reconnect(self, driver):
        return WebMisc().wait_element(driver, self.next_second_recconect_button, "next_second_recconect_button")

    def get_submit_recconect(self, driver):
        return WebMisc().wait_element(driver, self.submit_reconnect_button, "submit_reconnect_button")