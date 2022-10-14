from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class CXEServicePage:
    service_text = "//div[contains(text(), 'Service') and @class = 'entityNameTitle slds-line-height--reset']"
    service_enrollments = "//a[@class = 'slds-card__header-link baseCard__header-title-container' and contains(@href, 'Service_Enrollments')]"
    service_enrollments_text = "//h1[@title = 'Service Enrollments']"

    def get_service_text(self, driver):
        return WebMisc().wait_element(driver, self.service_text, "service_text")

    def get_service_enrollments(self, driver):
        return WebMisc().clickable_element(driver, self.service_enrollments, "service_enrollments")

    def get_service_enrollments_text(self, driver):
        return WebMisc().clickable_element(driver, self.service_enrollments_text, "service_enrollments_text")
