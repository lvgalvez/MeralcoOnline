from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class GoogleLoginPage:
    use_another_account = "//div[@class = 'BHzsHc']"
    email = "//input[@class = 'whsOnd zHQkBf']"
    next = "//button[@class = 'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']"
    password = "//input[@type = 'password']"
    send = "//button[@class = 'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']"

    def get_use_another_account(self, driver):
        return WebMisc().optional_wait_element(driver, self.use_another_account, "use_another_account")

    def get_email(self, driver):
        return WebMisc().wait_element(driver, self.email, "email")

    def get_next(self, driver):
        return WebMisc().wait_element(driver, self.next, "next")

    def get_password(self, driver):
        return WebMisc().wait_element(driver, self.password, "password")

    def get_send(self, driver):
        return WebMisc().optional_wait_element(driver, self.send, "send")
