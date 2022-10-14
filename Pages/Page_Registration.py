
from Utilities.WebMisc import WebMisc
misc = WebMisc()

class RegistrationPage:
    email = "//input[@class = 'slds-input mov-input input' and @inputmode = 'email']"
    first_name = "//input[@class = 'slds-input mov-input input' and @placeholder = 'First Name *']"
    middle_name = "//input[@class = 'slds-input mov-input input' and @placeholder = 'Middle Name ']"
    last_name = "//input[@class = 'slds-input mov-input input' and @placeholder = 'Last Name *']"
    mobile_number = "//input[@class = 'slds-input' and @placeholder = 'Mobile Number *']"
    can = "//input[@class = 'slds-input' and @placeholder = 'Customer Account Number *']"
    total_kwh = "//input[@class = 'slds-input' and @placeholder = 'Total kWh*']"
    bill_date = "//input[@class = 'CXE_billDate slds-input mov-input mov-input_date input']"
    terms_condition = "//div[@class = 'checkbox-custom']"
    register = "//button[contains(text(), 'Register')]"
    create_account_text = "//h3[contains(text(), 'Create a New Account')]"
    confirmation_ok = "//a[contains(text(), 'OK') and @class = 'slds-button mov-button mov-element_max-width-170']"
    confirmation_success = "//p[contains(text(), 'sent you a confirmation email')]"
    sin = "//input[@placeholder = 'Service ID Number *']"
    no_meralco_bill = "//div[@class = 'radio-custom cstom-radio-two']"
    bill_deposit = "//input[@placeholder= 'Bill Deposit*']"
    payment_date = "//input[@class= 'CXE_payDate slds-input mov-input mov-input_date input']"
    google_sign = "//button[@class= 'slds-button slds-button--neutral slds-button mov-button mov-button_gplogin uiButton']"

    def get_create_account_text(self, driver):
        return misc.wait_element(driver, self.create_account_text, "create_account_text")

    def get_email(self, driver):
        return misc.wait_element(driver, self.email, "email")

    def get_first_name(self, driver):
        return misc.wait_element(driver, self.first_name, "first_name")

    def get_middle_name(self, driver):
        return misc.wait_element(driver, self.middle_name, "middle_name")

    def get_last_name(self, driver):
        return misc.wait_element(driver, self.last_name, "last_name")

    def get_mobile_number(self, driver):
        return misc.wait_element(driver, self.mobile_number, "mobile_number")

    def get_can(self, driver):
        return misc.wait_element(driver, self.can, "can")

    def get_total_kwh(self, driver):
        return misc.wait_element(driver, self.total_kwh, "total_kwh")

    def get_bill_date(self, driver):
        return misc.wait_element(driver, self.bill_date, "bill_date")

    def get_terms_condition(self, driver):
        return misc.wait_element(driver, self.terms_condition, "terms_condition")

    def get_register(self, driver):
        return misc.wait_element(driver, self.register, "register")

    def get_confirmation_ok(self, driver):
        return misc.clickable_element(driver, self.confirmation_ok, "confirmation_ok")

    def get_confirmation_success(self, driver):
        return misc.wait_element(driver, self.confirmation_success, "confirmation_success")

    def get_sin(self, driver):
        return misc.wait_element(driver, self.sin, "sin")

    def get_no_meralco_bill(self, driver):
        return misc.wait_element(driver, self.no_meralco_bill, "no_meralco_bill")

    def get_bill_deposit(self, driver):
        return misc.wait_element(driver, self.bill_deposit, "bill_deposit")

    def get_payment_date(self, driver):
        return misc.wait_element(driver, self.payment_date, "payment_date")

    def get_google_sign(self, driver):
        return misc.wait_element(driver, self.google_sign, "google_sign")