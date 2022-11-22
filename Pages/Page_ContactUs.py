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
    lastname = "//*[@id='68:2;a']"
    can = "//*[@id='7:199;a']"
    feedback = "//h3[contains(text(), 'Give Feedback')]"
    make_request = "//h3[contains(text(), 'Make a Request')]"
    ok_btn = "//button[contains(text(),'OK')]"
    select_sin = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div[3]/div/div/select"

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
