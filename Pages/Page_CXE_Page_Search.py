from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class CXESearchPage:
    searched_can = "//a[contains(@title, 'CONTR-') and @data-refid]"

    def get_searched_can(self, driver):
        return WebMisc().clickable_element(driver, self.searched_can, "searched_can")

