from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc
from Utilities.Data import *
class CXENewCaseRecontractPage:

    lbl_origin_kiosk_byxpath = "//a[text() = 'Kiosk']"
    btn_case_save_byxpath = "//button[@title = 'Save']"
    lbl_can_text_byxpath = "//span[text()= 'Customer Account Number']"
    btn_close_recontract_byxpath = "//button[@title= 'Close New Case: Recontract of Electric Service']"
    btn_case_origin_byxpath = "//div[1]/div/div/div[4]/div[1]/div/div/div/div/div[1]/div/div/a[text() = '--None--']"
    inp_can_byxpath = "//div[2]/div/div/div[1]/div[1]/div/div/div/input[@class = ' input']"
    inp_sin_byxpath = "//div[2]/div/div/div[2]/div[1]/div/div/div/input[@class = ' input']"
    lbl_energization_date_byxpath = "//div[1]/div[1]/div/div/div/div/a[@class = 'datePicker-openIcon display']"
    btn_energization_today_byxpath = "//tr[7]/td/button[text() = 'Today']"
    lbl_text_reconnect_byxpath = "//h2[text() = 'New Case: Recontract of Electric Service']"

    def get_text_reconnect(self, driver):
        return WebMisc().clickable_element(driver, self.lbl_text_reconnect_byxpath, "lbl_text_reconnect_byxpath")

    def get_origin_kiosk(self, driver):
        return WebMisc().clickable_element(driver, self.lbl_origin_kiosk_byxpath, "lbl_origin_kiosk_byxpath")

    def get_case_save(self, driver):
        return WebMisc().clickable_element(driver, self.btn_case_save_byxpath, "btn_case_save_byxpath")

    def get_can_text(self, driver):
        return WebMisc().wait_element(driver, self.lbl_can_text_byxpath, "lbl_can_text_byxpath")

    def get_close_recontract(self, driver):
        return WebMisc().clickable_element(driver, self.btn_close_recontract_byxpath, "btn_close_termination_byxpath")

    def get_case_origin(self, driver):
        return WebMisc().clickable_element(driver, self.btn_case_origin_byxpath, "btn_case_origin_byxpath")

    def get_energization_date(self, driver):
        return WebMisc().clickable_element(driver, self.lbl_energization_date_byxpath, "lbl_energization_date_byxpath")

    def get_energization_today(self, driver):
        return WebMisc().clickable_element(driver, self.btn_energization_today_byxpath, "btn_energization_today_byxpath")

    def get_can(self, driver):
        return WebMisc().wait_element(driver, self.inp_can_byxpath, "inp_can_byxpath")

    def get_sin(self, driver):
        return WebMisc().wait_element(driver, self.inp_sin_byxpath, "inp_sin_byxpath")