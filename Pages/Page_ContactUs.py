from selenium.webdriver.common.by import By

from Utilities.WebMisc import WebMisc
from selenium.webdriver.support.ui import Select

class ContactUsPage:

    log_inquiry = "//h3[contains(text(), 'Log an inquiry')]"
    log_inquiry_remarks = "//textarea[@id='1204:0']"
    log_inquiry_concern_type = "//select[@id='1107:0']"
    log_inquiry_submit = "//button[contains(text(), 'Submit')]"
    log_inquiry_reference_number = "//span[contains(@class, 'text-orange')]"

    def get_log_inquiry(self,driver):
        return WebMisc().clickable_element(driver, self.log_inquiry, "log_inquiry")

    def get_log_remarks(self,driver):
        return WebMisc().clickable_element(driver, self.log_inquiry_remarks, "log_inquiry_remarks")

    def enter_remarks(self,driver, remarks):
        return driver.find_element(By.XPATH, self.log_inquiry_remarks).send_keys(remarks)

    def get_log_inquiry_concern_type(self,driver):
        return Select(driver.find_element(By.XPATH, self.log_inquiry_concern_type))

    def get_log_inquiry_submit(self, driver):
        return WebMisc().clickable_element(driver, self.log_inquiry_submit, "log_inquiry_submit")

    def get_log_inquiry_reference_number(self, driver):
        return driver.find_element(By.XPATH, self.log_inquiry_reference_number).text()