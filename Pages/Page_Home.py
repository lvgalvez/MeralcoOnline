
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class HomePage:
    hello_message = "//h3[@class = 'mov-text_size-24 mov-text_weight-bold']"
    request_tile = "//h3[contains(text(), 'REQUEST FOR A SERVICE')]"
    label_start_serv = "//h4[@class = 'slds-m-bottom_large mov-text_size-32 mov-text_weight-semi-bold']"
    account = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[2]/div/div/div[2]/div[6]/div/div/div[2]/div/a[3]"
    popupNO = "//*[@id='modal-content-id-1']/div[2]/a[2]"
    hello_message = "//h3[contains(text(), 'Hello, ')]"
    profile_name = "//span[@class = ' profileName']"
    my_profile = "//a[contains(text(), 'My Profile')]"
    accounts = "//button[contains(text(), 'Accounts')]"
    outage_incidents = "//button[contains(text(), 'Outages & Incidents')]"
    manage_accounts = "/html/body/div[3]/div[1]/div/div[2]/div/div/div/community_navigation-global-navigation-list/div/nav/ul/li[3]/community_navigation-global-navigation-item/ul/li[1]/community_navigation-global-navigation-item/a"
    account_details = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[2]/div/div/div[2]/div[6]/div/div/div[2]/div/a[3]"
    pop_up_text = "//h3[@class='slds-text-heading_medium slds-text-align_left slds-m-bottom_large mov-text_size-32 mov-text_weight-semi-bold']"
    mobile_number = "//input[@placeholder='Mobile Number *']"
    customer_account_number = "//input[@placeholder='Customer Account Number (CAN)*']"
    total_kwh = "//input[@placeholder='Total kWh*']"
    bill_date = "//input[@class='CXE_billDate slds-input mov-input mov-input_date custom-mob-input-width custom-mob-date-layout input']"
    terms = "//div[@class='checkbox-custom']"
    no_bill = "//label[contains(text(), 'eceived my first Meralco bill')]"
    bill_deposit = "//input[@placeholder='Bill Deposit*']"
    payment_date = "//input[@class='CXE_payDate slds-input mov-input mov-input_date custom-date-placeholder custom-mob-input-width custom-mob-date-layout input']"
    submit = "//button[@class='slds-button slds-button--neutral slds-button mov-button mov-button_login custom-btn uiButton']"
    enroll_service = "//a[@href = '/customers/s/manageservice']"
    report_outage = "//a[@href = '/customers/s/outagemap']"
    sin_multiple = "//input[@placeholder='Service ID Number *']"
    contact_us = "//a[@title='Contact Us']"
    bill_and_payments = "//button[contains(text(), 'Bills & Payments')]"
    pay_bills = "//a[@href='/customers/s/paybills']"
    bayadExpress = "//img[@src='/customers/resource/1668042297000/PaymentImages/PaymentImages/BE-Banner.png']"

    def get_popupNO(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, self.popupNO)))

    def get_account(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.account)))

    def get_request_tile(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.request_tile)))

    def get_label_start_serv(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.label_start_serv)))

    def get_hello_message(self, driver):
        return WebMisc().wait_element(driver, self.hello_message, "hello_message")

    def get_profile_name(self, driver):
        return WebMisc().wait_element(driver, self.profile_name, "profile_name")

    def get_my_profile(self, driver):
        return WebMisc().clickable_element(driver, self.my_profile, "my_profile")

    def get_accounts(self, driver):
        return WebMisc().wait_element(driver, self.accounts, "accounts")

    def get_manage_accounts(self, driver):
        return WebMisc().wait_element(driver, self.manage_accounts, "manage_accounts")

    def get_account_details(self, driver):
        return WebMisc().wait_element(driver, self.account_details, "account_details")

    def get_pop_up_text(self, driver):
        return WebMisc().wait_element(driver, self.pop_up_text, "pop_up_text")

    def get_mobile_number(self, driver):
        return WebMisc().wait_element(driver, self.mobile_number, "mobile_number")

    def get_customer_account_number(self, driver):
        return WebMisc().wait_element(driver, self.customer_account_number, "customer_account_number")

    def get_total_kwh(self, driver):
        return WebMisc().wait_element(driver, self.total_kwh, "total_kwh")

    def get_bill_date(self, driver):
        return WebMisc().wait_element(driver, self.bill_date, "bill_date")

    def get_terms(self, driver):
        return driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.terms))))

    def get_no_bill(self, driver):
        return WebMisc().clickable_element(driver, self.no_bill, "no_bill")

    def get_bill_deposit(self, driver):
        return WebMisc().wait_element(driver, self.bill_deposit, "bill_deposit")

    def get_payment_date(self, driver):
        return WebMisc().wait_element(driver, self.payment_date, "payment_date")

    def get_sin_multiple(self, driver):
        return WebMisc().wait_element(driver, self.sin_multiple, "sin_multiple")

    def get_submit(self, driver):
        return driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.submit))))

    def get_enroll_service(self, driver):
        return WebMisc().clickable_element(driver, self.enroll_service, "enroll_service")

    def get_outage_incidents(self, driver):
        return WebMisc().clickable_element(driver, self.outage_incidents, "outage_incidents")

    def get_report_outage(self, driver):
        return WebMisc().clickable_element(driver, self.report_outage, "report_outage")

    def get_contact_us(self, driver):
        return WebMisc().clickable_element(driver, self.contact_us, "contact_us")

    def get_bills_and_payments(self, driver):
        return WebMisc().clickable_element(driver, self.bill_and_payments, "bill_and_payments")

    def get_pay_bills(self, driver):
        return WebMisc().clickable_element(driver, self.pay_bills, "pay_bills")
        #driver.find_element(By.XPATH, self.pay_bills).click()

    def get_bayad_express_ad(self, driver):
        return driver.find_element(By.XPATH, self.bayadExpress)