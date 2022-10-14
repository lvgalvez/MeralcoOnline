from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class GoogleInboxPage:
    enrollment_mail = "//span[contains(text(), 'Sandbox: Service Enrollment in Meralco Online Account')]"

    def get_enrollment_mail(self, driver):
        return WebMisc().clickable_element(driver, self.enrollment_mail, "enrollment_mail")

