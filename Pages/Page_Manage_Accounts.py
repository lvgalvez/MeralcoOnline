from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class ManageAccountsPage:
    manage_accounts_text = "//p[contains(text(), 'Manage your service account here.')]"
    submit = "//button[contains(text(), 'Submit')]"

    def get_manage_accounts_text(self, driver):
        return WebMisc().wait_element(driver, self.manage_accounts_text, "manage_accounts_text")

    def get_submit(self, driver):
        return WebMisc().wait_element(driver, self.submit, "submit")
