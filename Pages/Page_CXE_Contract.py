from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class CXEContractPage:
    contract_text = "//div[contains(text(), 'Contract')]"
    services_payor = "//span[@title= 'Services (Payor)' and contains(text(), 'Services (Payor)')]"
    service = "//*[@id='brandBand_3']/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/tbody/tr/th/span/a"
    select_service = "/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section[1]/div/div/section/div/div[2]/div[1]/div[1]/div/div/div/div[1]/div/div[2]/div[2]/div[3]/div/section/div[2]/div/article/div[2]/div/div/div/div/ul/li/article/div/div[1]/h3/div/a"
    contract_tab = "//li[@class= 'oneConsoleTabItem tabItem slds-tabs--default__item slds-sub-tabs__item slds-grid slds-grid--vertical-align-center slds-tabs__item--overflow hideAnimation  navexConsoleTabItem']"
    apple ="//button[@class= 'slds-button slds-button--neutral slds-button mov-button mov-button_aplogin uiButton']"

    def get_contract_text(self, driver):
        return WebMisc().wait_element(driver, self.contract_text, "contract_text")

    def get_services_payor(self, driver):
        return WebMisc().wait_element(driver, self.services_payor, "services_payor")

    def get_service(self, driver):
        return WebMisc().clickable_element(driver, self.services_payor, "service")

    def get_select_service(self, driver):
        return WebMisc().clickable_element(driver, self.select_service, "select_service")

    def get_contract_tab(self, driver):
        return WebMisc().optional_wait_element(driver, self.contract_tab, "contract_tab")

    def get_apple(self, driver):
        return WebMisc().optional_wait_element(driver, self.apple, "apple")


