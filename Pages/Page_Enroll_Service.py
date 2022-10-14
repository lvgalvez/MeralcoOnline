
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class EnrollServicePage:
    can = "//input[@placeholder= 'Customer Account Number (CAN)*']"
    sin = "//input[@placeholder= 'Service ID Number *']"
    bill_date = "//input[@class= 'CXE_billDate slds-input mov-input mov-input_date  input']"
    total_kwh = "//input[@placeholder= 'Total kWh*']"
    submit = "//button[@class= 'slds-button slds-button--neutral slds-button mov-button-default mov-element_max-width-170 custom-modal-submit-btn uiButton']"
    service_text = "//h3[contains(text(), 'Enroll a Service')]"
    no_bill = "//label[contains(text(), 'received my first Meralco bill')]"
    payment_date = "//input[@class= 'CXE_payDate slds-input mov-input mov-input_date custom-date-placeholder input']"
    bill_deposit = "//input[@placeholder= 'Bill Deposit*']"

    def get_can(self, driver):
        return WebMisc().wait_element(driver, self.can, "can")

    def get_sin(self, driver):
        return WebMisc().wait_element(driver, self.sin, "sin")

    def get_bill_date(self, driver):
        return WebMisc().wait_element(driver, self.bill_date, "bill_date")

    def get_total_kwh(self, driver):
        return WebMisc().wait_element(driver, self.total_kwh, "total_kwh")

    def get_submit(self, driver):
        return WebMisc().wait_element(driver, self.submit, "submit")

    def get_service_text(self, driver):
        return WebMisc().wait_element(driver, self.service_text, "service_text")

    def get_no_bill(self, driver):
        return WebMisc().clickable_element(driver, self.no_bill, "no_bill")

    def get_payment_date(self, driver):
        return WebMisc().wait_element(driver, self.payment_date, "payment_date")

    def get_bill_deposit(self, driver):
        return WebMisc().wait_element(driver, self.bill_deposit, "bill_deposit")
