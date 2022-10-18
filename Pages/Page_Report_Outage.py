from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class ReportOutagePage:
    report_outage_text = "//h3[contains(text(), 'Report an Outage or Incident')]"
    no_power_radio = "//span[contains(text(), 'No Power - My house/building only')]"
    no_power_street_radio = "//span[contains(text(), 'No Power - Whole street/block')]"
    select_damage = "//div[@class = 'slds-select_container mov-select_container mov-select_container-left-align']"
    pole_broken = "//option[@label = 'Pole is broken or has fallen']"
    service_id_radio = "//span[contains(text(), 'Service ID Number')]"
    service_id_dropdown = "//select[@class = 'slds-select mov-select-aftersales CXE_selectInvalid select uiInput uiInputSelect uiInput--default uiInput--select']"
    service_select = "//*[@class='slds-select mov-select-aftersales CXE_selectInvalid select uiInput uiInputSelect uiInput--default uiInput--select']/option[2]"
    service_id_number = "//input[@class = 'slds-input mov-input-contact mov-placeholder input-toggle mov-placeholder-bold input uiInput uiInputText uiInput--default uiInput--input']"
    location_map = "//strong[contains(text(), 'Location in Map')]"

    def get_report_outage_text(self, driver):
        return WebMisc().wait_element(driver, self.report_outage_text, "report_outage_text")

    def get_no_power_radio(self, driver):
        return WebMisc().wait_element(driver, self.no_power_radio, "no_power_radio")

    def get_service_id_radio(self, driver):
        return WebMisc().clickable_element(driver, self.service_id_radio, "service_id_radio")

    def get_service_id_number(self, driver):
        return WebMisc().wait_element(driver, self.service_id_number, "service_id_number")

    def get_location_map(self, driver):
        return WebMisc().clickable_element(driver, self.location_map, "location_map")

    def get_service_select(self, driver):
        return WebMisc().clickable_element(driver, self.service_select, "service_select")

    def get_service_id_dropdown(self, driver):
        return WebMisc().clickable_element(driver, self.service_id_dropdown, "service_id_dropdown")

    def get_no_power_street_radio(self, driver):
        return WebMisc().clickable_element(driver, self.no_power_street_radio, "no_power_street_radio")

    def get_select_damage(self, driver):
        return WebMisc().clickable_element(driver, self.select_damage, "select_damage")
