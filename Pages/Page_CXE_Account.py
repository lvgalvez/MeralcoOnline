from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time


class CXEAccountPage:
    click_next = "//*[@id='request_to_modify']/div/div/div/div/div/div[4]/div/button"
    account_page = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div[1]/h3"
   # change_contract = "//*[@id='TableHolder']/div[3]/div[2]/div[2]"
    request = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/h3"
    change_name = "//*[@id='TableHolder']/div[3]/div[2]/div[2]/a"
    value_added = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/ul/li[3]/a"
    click_amc = "//*[@id='tab-2']/div/div[2]/div[2]/div/label[1]/span"
    click_next2 = "//*[@id='new_address']/div/div/div/div/div/div[5]/div/button"
    terms_condition = "//*[@id=;ServiceCommunityTemplate;]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/ul/li[4]/a"
    change_contract_name = "/html/body/div[3]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/div[1]/ul/li[1]"
    click_term_condition = "//*[@id='tab-3']/div[3]/div[2]/div/label/div"
    submit = "//*[@id='terms_and_conditions']/div/div[2]/div[3]/button"
    change_contract_details = "/html/body/div[3]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div[3]/div[2]/div[2]"
    #confirmation = ""
    view_details = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[2]/div/div/div[2]/div[6]/div/div/div[2]/div/a[3]"
    submit_term = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/div[3]/button"
    account_clk = "/html/body/div[3]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/table/tbody/tr[3]/td[1]/div/label/div"
    stop_service = "/html/body/div[3]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div[3]/div[2]/div[4]/a/span"
    request_page = "//*[@id='request_to_modify']/div/div/div/div/div/h4"
    submit_next = "//*[@id='request_details']/div/div[2]/div[2]/button"
    submit_account = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/div[3]/button"
    clk_account = "//*[@id='TableHolder']/div[1]/table/tbody/tr[5]/td[1]/div/label/div"
    service_details = "/html/body/div[3]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/a/span"
    newaddress = "//*[@id='new_address']/div/div/div/div/div/h4"
    reactivateservice = "/html/body/div[3]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div[3]/div[2]/div[3]/a/span"
    birthday = "/html/body/div[3]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[3]/div[2]/div[4]/div/div/div/input"
    ownership = "/html/body/div[3]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div/div[3]/div[3]/div/div/select"
    ownership_value = "//option[@value = 'Owned']"
    next3 = "//*[@id='value_add_services']/div/div[7]/button"
    terms_cond = "/html/body/div[3]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[4]/div[3]/div/div[2]/div[1]/label/div"


    def get_terms_cond(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.terms_cond)))
    def get_click_next3(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.next3)))
    def get_ownership(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.ownership)))

    def get_ownership_value(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.ownership_value)))
    def get_birthday(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.birthday)))
    def get_reactivate_service(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.reactivateservice)))
    def get_new_address(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.newaddress)))
    def get_service_details(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.service_details)))

    def get_clk_account(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.clk_account)))

    def get_submit_account(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.submit_account)))
    def get_submit_next(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.submit_next)))

    def get_request_page(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.request_page)))
    def get_stop_service(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.stop_service)))
    def get_account_clk(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.account_clk)))
    def get_submit_term(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.submit_term)))
    def get_view_details(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.view_details)))

    def get_confirmation(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.confirmation)))

    def get_submit(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.submit)))

    def get_click_term_condition(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.click_term_condition)))

    def get_change_contract_name(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.change_contract_name)))


    def get_terms_condition(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.terms_condition)))

    def get_click_next2(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.click_next2)))
    def get_click_amc(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.click_amc)))

    def get_value_added(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.value_added)))

    def get_change_name(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.change_name)))

    def get_click_next(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.click_next)))

    def get_request(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.request)))
    def get_account_page(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.account_page)))



    def get_change_contract_details(self, driver):
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.change_contract_details)))

