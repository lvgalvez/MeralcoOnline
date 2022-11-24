from selenium.webdriver.common.by import By

from Utilities.WebMisc import WebMisc
from selenium.webdriver.support.ui import Select

class ContactUsPage:

    log_inquiry = "//h3[contains(text(), 'Log an Inquiry')]"
    log_inquiry_remarks = "//textarea[@id='1204:0']"
    log_inquiry_concern_type = "//select[@id='1107:0']"
    log_inquiry_submit = "//button[contains(text(), 'Submit')]"
    log_inquiry = "//h3[contains(text(), 'Log an Inquiry')]"
    give_feedback = "//h3[contains(text(), 'Give Feedback')]"
    request = "//h3[contains(text(), 'Make a Request')]"
    log_inquiry_remarks = "//textarea[contains(@class, 'slds-textarea')]"
    log_inquiry_concern_type = "//select[contains(@class, 'slds-select')]"
    submit_btn = "//button[contains(text(), 'Submit')]"
    log_inquiry_reference_number = "//span[contains(@class, 'text-orange')]"
    lastname = "//input[@id='50:199;a']"
    can = "//input[@id='7:199;a']"
    feedback = "//h3[contains(text(), 'Give Feedback')]"
    make_request = "//h3[contains(text(), 'Make a Request')]"
    ok_btn = "//button[contains(text(),'OK')]"
    select_sin = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div[3]/div/div/select"
    firstname = "//input[@id='36:199;a']"
    email = "//input[@id='64:199;a']"
    mobile = "//input[@id='76:199;a']"
    remarks = "//textarea[@id='569:0']"
    sin = "//input[@id='22:199;a']"

    def get_concern_sn(self, driver):
        return WebMisc().clickable_element(driver, self.sin, "sin")
    def get_remarks(self, driver):
        return WebMisc().clickable_element(driver, self.remarks, "remarks")
    def get_mobile(self, driver):
        return WebMisc().clickable_element(driver, self.mobile, "mobile")
    def get_email(self, driver):
        return WebMisc().clickable_element(driver, self.email, "email")
    def get_firstname(self, driver):
        return WebMisc().clickable_element(driver, self.firstname, "firstname")
    def get_make_request(self, driver):
        return WebMisc().clickable_element(driver, self.make_request, "make_request")
    def get_feedback(self, driver):
        return WebMisc().clickable_element(driver, self.feedback, "feedback")
    def get_lastname(self,driver):
        return WebMisc().clickable_element(driver, self.lastname, "lastname")
    def get_CAN(self,driver):
        return WebMisc().clickable_element(driver, self.can, "can")
    def get_log_inquiry(self,driver):
        return WebMisc().clickable_element(driver, self.log_inquiry, "log_inquiry")

    def get_top_page(self,driver, page):
        top_page = "//div//h3[contains(text(), '" + page + "') and contains (@class,'slds-m-bottom_small')]"
        return WebMisc().clickable_element(driver, top_page, "log_inquiry_top_page")

    def get_log_remarks(self,driver):
        return WebMisc().clickable_element(driver, self.log_inquiry_remarks, "log_inquiry_remarks")

    def enter_remarks(self,driver, remarks):
        return driver.find_element(By.XPATH, self.log_inquiry_remarks).send_keys(remarks)

    def get_log_inquiry_concern_type(self,driver):
        return Select(driver.find_element(By.XPATH, self.log_inquiry_concern_type))

    def get_submit(self, driver):
        return WebMisc().clickable_element(driver, self.submit_btn, "submit_btn")

    def get_log_inquiry_reference_number(self, driver):
        return driver.find_element(By.XPATH, self.log_inquiry_reference_number).text

    def get_ok_btn(self,driver):
        return WebMisc().clickable_element(driver, self.ok_btn, "log_inquiry_ok_btn")

    def get_give_feedback(self,driver):
        return WebMisc().clickable_element(driver, self.give_feedback, "give_feedback")

    def get_request(self,driver):
        return WebMisc().clickable_element(driver, self.request, "request")

    def get_sin(self, driver):
        return Select(driver.find_element(By.XPATH, self.select_sin))
