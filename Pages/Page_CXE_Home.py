from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc
from Utilities.Data import *


class CXEHomePage:

    search_button = "//button[@class= 'slds-button slds-button_neutral search-button slds-truncate']"
    search_input = "//input[@placeholder= 'Search...']"
    suggestion_case = "//*[contains(@id, 'suggestionsList')]/search_dialog-instant-result-item[1]/div[1]/div[2]/div/lightning-formatted-rich-text/span[contains(text(), 'Case')]"
    profile_options = ".mauto .userOptionBtn"
    logout_btn = "//button[text() = 'Logout']"
    switch_profile_btn = "//button[text() = 'Switch Profile']"
    switch_profile = "//*[@id='profileModal']/div/div/md-card/md-card-content/form/div[1]/div/button"
    #profile_account = "//li[text() = '"+ Outage['switch_profile'] + "']"
    profile_account = "//*[@id='profileModal']/div/div/md-card/md-card-content/form/div[1]/div/ul/li[2]"
    okay_btn = "//*[@id='profileModal']/div/div/md-card/md-card-content/form/div[4]/button[1]"
    accountdetails = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[2]/div/div/div[2]/div[6]/div/div/div[2]/div/a[3]"
    payment_history = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[2]/div/div/div[2]/div[6]/div/div/div[1]/div/div[3]/div[2]/div/ul/li[3]/a"
    peccbm_no_modal = "//div/div[1]/div/div/div[2]/a[2]"
    btn_navigation_menu_byxpath = "//button[@title= 'Show Navigation Menu']"
    btn_navigation_cases_byxpath = "//span[text() = 'Cases']"
    btn_navigation_home_byxpath = "//span[text() = 'Home']"
    btn_case_new_byxpath = "//a[@title= 'New']"
    cxe_search = "//div[4]/div[1]/section/header/div[2]/div[2]/div/button"
    cxe_search_case = "//div[4]/div[2]/div/div/div[1]/div/div[1]/lightning-input/div/input"
    cxe_change_owner = "//section/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/span[2]/ul/li[2]/a"
    cxe_search_user = "//div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div/div[1]/div[1]/div[2]/input"
    cxe_user = "//div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div/div[1]/div[1]/div[2]/div/div[2]/ul/li/a"
    cxe_assign_new_owner = "//div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div/div[1]/div[1]/div[2]/input"
    cxe_case_owner = "//div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div/div[1]/div[1]/div[2]/div/div[2]/ul/li/a/div[2]"
    cxe_case_submit = "//div[2]/div[2]/div/div[2]/div/div[3]/div/button[2]"
    cxe_edit_case = "//section/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/span[2]/ul/li[1]/a"
    cxe_case_status = "//div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/article/div[3]/div/div[1]/div/div/div[3]/div[2]/div/div/div/div/div[1]/div/div/a"
    cxe_app_validated_status = "//a[@title='Application Validated']"
    cxe_enegrization_date = "//div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/article/div[3]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/input"
    cxe_case_status_save_btn = "//html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/button[3]"
    cxe_meter_socket_status = "//a[@title='Meter Socket Issued']"
    cxe_customer_type = "//div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/article/div[3]/div/div[3]/div/div/div[9]/div[2]/div/div/div/div/div[1]/div/div/a"
    cxe_private_customer = "//a[@title='Private']"

    def get_payment_history(self, driver):
        return WebMisc().optional_wait_element(driver, self.payment_history, "payment_history")

    def get_submit(self, driver):
        return WebMisc().optional_wait_element(driver, self.submit, "submit")

    def get_account_details(self, driver):
        return WebMisc().optional_wait_element(driver, self.accountdetails, "accountdetails")

    def get_search_button(self, driver):
        return WebMisc().optional_wait_element(driver, self.search_button, "search_button")

    def get_search_input(self, driver):
        return WebMisc().optional_wait_element(driver, self.search_input, "search_input")

    def get_suggestion_case(self, driver):
        return WebMisc().clickable_element(driver, self.suggestion_case, "suggestion_case")

    def get_profile_options(self, driver):
        return driver.find_element(By.CSS_SELECTOR,self.profile_options).click()

    def logout_account(self,driver):
        return WebMisc().clickable_element(driver, self.logout_btn, "logout_btn")

    def click_switch_profile(self,driver):
        return WebMisc().clickable_element(driver, self.switch_profile_btn, "switch_profile_btn")

    def switch_account(self, driver):
        return WebMisc().clickable_element(driver, self.switch_profile, "switch_profile")

    def get_profile(self, driver):
        driver.find_element(By.XPATH, self.profile_account).click()

    def get_profile_value(self, driver):
        driver.find_element(By.XPATH, self.okay_btn).click()

    def get_peccbm_no(self, driver):
        return WebMisc().clickable_element(driver, self.peccbm_no_modal, "peccbm_no_modal")

    def get_navigation_menu(self, driver):
        return WebMisc().clickable_element(driver, self.btn_navigation_menu_byxpath, "btn_navigation_menu_byxpath")

    def get_navigation_cases(self, driver):
        return WebMisc().clickable_element(driver, self.btn_navigation_cases_byxpath, "btn_navigation_cases_byxpath")

    def get_navigation_home(self, driver):
        return WebMisc().clickable_element(driver, self.btn_navigation_home_byxpath, "btn_navigation_home_byxpath")

    def get_case_new(self, driver):
        return WebMisc().clickable_element(driver, self.btn_case_new_byxpath, "btn_case_new_byxpath")

    def get_cxe_search(self, driver):
        return WebMisc().clickable_element(driver, self.cxe_search, "cxe_search")

    def get_cxe_search_case(self, driver):
        return driver.find_element(By.XPATH, self.cxe_search_case)

    def get_cxe_change_owner(self, driver):
        return WebMisc().clickable_element(driver, self.cxe_change_owner, "cxe_change_owner")

    def get_cxe_user(self, driver):
        return WebMisc().clickable_element(driver, self.cxe_search_user, "cxe_search_user")

    def get_cxe_assign_new_owner(self, driver):
        return WebMisc().clickable_element(driver, self.cxe_assign_new_owner, "cxe_assign_new_owner")

    def get_cxe_case_owner(self, driver):
        return WebMisc().clickable_element(driver, self.cxe_case_owner, "cxe_case_owner")

    def get_cxe_case_submit(self, driver):
        return WebMisc().clickable_element(driver, self.cxe_case_submit, "cxe_case_submit")

    def get_cxe_edit_case(self, driver):
        return WebMisc().clickable_element(driver, self.cxe_edit_case, "cxe_edit_case")

    def get_case_status(self, driver):
        return WebMisc().clickable_element(driver, self.cxe_case_status, "cxe_case_status")

    def get_application_validated_stat(self, driver):
        return WebMisc().clickable_element(driver, self.cxe_app_validated_status, "cxe_app_validated_status")

    def get_energization_date(self, driver):
        return WebMisc().clickable_element(driver, self.cxe_enegrization_date, "cxe_enegrization_date")

    def get_case_status_save(self, driver):
        return WebMisc().clickable_element(driver, self.cxe_case_status_save_btn, "cxe_case_status_save_btn")

    def get_meter_socket_stat(self, driver):
        return WebMisc().clickable_element(driver, self.cxe_meter_socket_status, "cxe_meter_socket_status")

    def get_cxe_customer_type(self, driver):
        return WebMisc().clickable_element(driver, self.cxe_customer_type, "cxe_customer_type")

    def get_cxe_customer_private(self, driver):
        return WebMisc().clickable_element(driver, self.cxe_private_customer, "cxe_private_customer")

    def get_case_number_table(self, driver, caseNumber):
        cxe_case_number = "//a[@title='"+caseNumber+"']"
        return WebMisc().clickable_element(driver, cxe_case_number, "cxe_case_number")
