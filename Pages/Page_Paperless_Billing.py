
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class PaperlessBillingPage:
    lbl_paperless_billing_xPath = "//h3[contains(text(), 'Paperless Billing')]"
    confirm_password = "//input[@id = '555:2;a']"
    set_password = "//button[@data-aura-rendered-by= '612:2;a']"

    def get_paperless_billing(self, driver):
        return WebMisc().wait_element(driver, self.lbl_paperless_billing_xPath, "lbl_paperless_billing_xPath")
