
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time


class YopmailHomePage:
    email = "//input[@id = 'login']"
    check_inbox = "//button[@title= 'Check Inbox @yopmail.com']"
    here_link = "//a[contains(@href, 'https://uat.online.meralco.com.ph/customers/s/setpassword?id')]"

    def get_email(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.email)))

    def get_check_inbox(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.check_inbox)))

    def get_here_link(self, driver):
        return driver.find_element(By.XPATH, self.here_link)


