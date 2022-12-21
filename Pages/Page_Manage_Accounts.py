from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class ManageAccountsPage:
    manage_accounts_text = "//p[contains(text(), 'Manage your service account here.')]"
    submit = "//button[contains(text(), 'Submit')]"
    change_service = "//span[contains(text(), 'Change Service Details')]"
    change_contract = "//span[contains(text(), 'Change Contract Details')]"
    stop_electric_service = "//span[contains(text(), 'Stop Electric Service')]"
    reactivate_electric_service = "//span[contains(text(), 'Reactivate Electric Service')]"
    select_sin = "//html/body/div[3]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[3]/div/label/input"

    def get_manage_accounts_text(self, driver):
        return WebMisc().wait_element(driver, self.manage_accounts_text, "manage_accounts_text")

    def get_submit(self, driver):
        return WebMisc().wait_element(driver, self.submit, "submit")

    def get_change_service(self, driver):
        return WebMisc().wait_element(driver, self.change_service, "change_service")

    def get_change_contract(self, driver):
        return WebMisc().wait_element(driver, self.change_contract, "change_contract")

    def get_stop_service(self, driver):
        return WebMisc().wait_element(driver, self.stop_electric_service, "stop_electric_service")

    def get_reactivate_service(self, driver):
        return WebMisc().wait_element(driver, self.reactivate_electric_service, "reactivate_electric_service")

    def get_select_sin(self, driver):
        return WebMisc().wait_element(driver, self.select_sin, "select_sin")