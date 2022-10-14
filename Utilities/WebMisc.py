
from selenium.webdriver.support import expected_conditions as EC

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.Config import wait_time
from Utilities.Utils import Utilities

log = Utilities().getlogger()


class WebMisc:

    def wait_element(self, driver, element, name):
        try:
            return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, element)))
        except TimeoutException:
            log.error("Cannot Locate: " + name)
            raise Exception()

    def clickable_element(self, driver, element, name):
        try:
            return WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, element)))
        except TimeoutException:
            log.error("Cannot Locate: " + name)
            raise Exception()

    def optional_wait_element(self, driver, element, name):
        try:
            return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, element)))
        except:
            pass

    def is_enabled(self, element):
        if element.is_enabled():
            pass
        else:
            log.error("element is disabled")
            raise Exception()


