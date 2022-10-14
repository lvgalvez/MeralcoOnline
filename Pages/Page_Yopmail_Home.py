
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class YopmailHomePage:
    email = "//input[@id = 'login']"
    check_inbox = "//button[@title= 'Check Inbox @yopmail.com']"
    here_link = "//a[contains(@href, 'https://uat.online.meralco.com.ph/customers/s/setpassword?id')]"

    def get_email(self, driver):
        return WebMisc().wait_element(driver, self.email, "email")

    def get_check_inbox(self, driver):
        return WebMisc().wait_element(driver, self.check_inbox, "check_inbox")

    def get_here_link(self, driver):
        return WebMisc().wait_element(driver, self.here_link, "here_link")

