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
    reference_number = "//*[@id='54:2;a']"
    submit = "//*[@id='ServiceCommunityTemplate']/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div[1]/button[2]"
    lastname = "//*[@id='68:2;a']"
    selectall = "/html/body/div[2]/div[11]/div[3]/div/div[2]/div[1]/img"
    unplanned = "/html/body/div[2]/div[11]/div[3]/div/div[2]/div[2]"
    planned = "//html/body/div[2]/div[11]/div[3]/div/div[2]/div[3]"
    streelight = "//span[contains(text(), 'Streetlight Concern')]"
    clkno = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div[1]/div[1]/div[1]/div[5]/div/div[1]/div[2]/label/span[2]"
    learnmore = "//button[contains(text(), 'Learn More')]"


    def get_learn_more(self, driver):
        return WebMisc().wait_element(driver, self.learnmore, "learnmore")
    def get_no(self, driver):
        return WebMisc().wait_element(driver, self.clkno, "clkno")
    def get_streelight_power(self, driver):
        return WebMisc().wait_element(driver, self.streelight, "streelight")
    def get_planned(self, driver):
        return WebMisc().wait_element(driver, self.planned, "planned")
    def get_selectall(self, driver):
        return WebMisc().wait_element(driver, self.selectall, "selectall")

    def get_unplanned(self, driver):
        return WebMisc().wait_element(driver, self.unplanned, "unplanned")
    def get_last_name(self, driver):
        return WebMisc().wait_element(driver, self.lastname, "lastname")
    def get_submit(self, driver):
        return WebMisc().wait_element(driver, self.submit, "submit")
    def get_reference_number(self, driver):
        return WebMisc().wait_element(driver, self.reference_number, "reference_number")

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
