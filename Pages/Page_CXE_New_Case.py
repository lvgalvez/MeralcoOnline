from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc
from Utilities.Data import *
class CXENewCasePage:
    rbx_modification_service_byxpath = "//span[text() = 'Modification of Electric Service' and @class = 'slds-form-element__label topdown-radio--label']"
    rbx_termination_service_byxpath = "//span[text() = 'Termination of Electric Service' and @class = 'slds-form-element__label topdown-radio--label']"
    rbx_recontract_service_byxpath = "//span[text() = 'Recontract of Electric Service' and @class = 'slds-form-element__label topdown-radio--label']"
    btn_next_byxpath = "//span[text() = 'Next' and @class = ' label bBody']"
    lbl_change_name_byxpath = "//span[text() = 'Change in Contract Name']"
    btn_move_chosen_byxpath = "//button[@title= 'Move selection to Chosen']"
    lbl_origin_kiosk_byxpath = "//a[text() = 'Kiosk']"
    lbl_energization_date_byxpath = "//div[1]/div[1]/div/div/div/div/a[@class = 'datePicker-openIcon display']"
    btn_energization_today_byxpath = "//tr[7]/td/button[text() = 'Today']"
    btn_case_save_byxpath = "//button[@title = 'Save']"
    lbl_can_text_byxpath = "//span[text()= 'Customer Account Number']"
    btn_close_modification_byxpath = "//button[@title= 'Close New Case: Modification of Electric Service']"
    btn_case_origin_byxpath = "//div[7]/div[1]/div/div/div/div/div[1]/div/div/a[text() = '--None--']"
    inp_can_byxpath = "//div[1]/div[2]/div/div/div/input[@class = ' input']"
    inp_sin_byxpath = "//input[@placeholder= 'Search Services...']"
    lnk_service_byxpath = "//a[contains(text(), 'SERV-')]"

    def get_service(self, driver):
        return WebMisc().clickable_element(driver, self.lnk_service_byxpath, "lnk_service_byxpath")

    def get_modification_service(self, driver):
        return WebMisc().clickable_element(driver, self.rbx_modification_service_byxpath, "rbx_modification_service_byxpath")

    def get_termination_service(self, driver):
        return WebMisc().clickable_element(driver, self.rbx_termination_service_byxpath, "rbx_termination_service_byxpath")

    def get_recontract_service(self, driver):
        return WebMisc().clickable_element(driver, self.rbx_recontract_service_byxpath, "rbx_recontract_service_byxpath")

    def get_next(self, driver):
        return WebMisc().clickable_element(driver, self.btn_next_byxpath, "btn_next_byxpath")

    def get_change_name(self, driver):
        return WebMisc().clickable_element(driver, self.lbl_change_name_byxpath, "lbl_change_name_byxpath")

    def get_move_chosen(self, driver):
        return WebMisc().clickable_element(driver, self.btn_move_chosen_byxpath, "btn_move_chosen_byxpath")

    def get_origin_kiosk(self, driver):
        return WebMisc().clickable_element(driver, self.lbl_origin_kiosk_byxpath, "lbl_origin_kiosk_byxpath")

    def get_energization_date(self, driver):
        return WebMisc().clickable_element(driver, self.lbl_energization_date_byxpath, "lbl_energization_date_byxpath")

    def get_energization_today(self, driver):
        return WebMisc().clickable_element(driver, self.btn_energization_today_byxpath, "btn_energization_today_byxpath")

    def get_case_save(self, driver):
        return WebMisc().clickable_element(driver, self.btn_case_save_byxpath, "btn_case_save_byxpath")

    def get_can_text(self, driver):
        return WebMisc().wait_element(driver, self.lbl_can_text_byxpath, "lbl_can_text_byxpath")

    def get_close_modification(self, driver):
        return WebMisc().clickable_element(driver, self.btn_close_modification_byxpath, "btn_close_modification_byxpath")

    def get_case_origin(self, driver):
        return WebMisc().clickable_element(driver, self.btn_case_origin_byxpath, "btn_case_origin_byxpath")

    def get_can(self, driver):
        return WebMisc().wait_element(driver, self.inp_can_byxpath, "inp_can_byxpath")

    def get_sin(self, driver):
        return WebMisc().wait_element(driver, self.inp_sin_byxpath, "inp_sin_byxpath")