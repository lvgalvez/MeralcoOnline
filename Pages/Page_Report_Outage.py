from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class ReportOutagePage:
    report_outage_text = "//h3[contains(text(), 'Report an Outage or Incident')]"
    no_power_radio = "//span[contains(text(), 'No Power - My house/building only')]"
    no_power_street_radio = "//span[contains(text(), 'No Power - Whole street/block')]"
    unstable_power = "//span[contains(text(), 'Unstable Power')]"
    safety_concern = "//span[contains(text(), 'Safety Concern')]"
    select_safety_concern = "//button[@class = 'slds-combobox__input slds-input_faux'] "
    select_damage = "//div[@class = 'slds-select_container mov-select_container mov-select_container-left-align']"
    pole_broken = "//option[@label = 'Pole is broken or has fallen']"
    safety_pole_broken = "//lightning-base-combobox-item[span/span[contains(text(), 'Pole is broken')]]"
    lights_flickering = "//option[@label = 'My lights are flickering']"
    service_id_radio = "//span[contains(text(), 'Service ID Number') and @class = 'slds-form-element__label mov-text_weight-semi-bold']"
    service_id_dropdown = "//select[@class = 'slds-select mov-select-aftersales CXE_selectInvalid select uiInput uiInputSelect uiInput--default uiInput--select']"
    service_select = "//*[@class='slds-select mov-select-aftersales CXE_selectInvalid select uiInput uiInputSelect uiInput--default uiInput--select']/option[2]"
    service_id_number = "//input[@class = 'slds-input mov-input-contact mov-placeholder input-toggle mov-placeholder-bold input uiInput uiInputText uiInput--default uiInput--input']"
    location_map = "//strong[contains(text(), 'Location in Map')]"
    upload_button = "//i[@class = 'fa fa-plus browse-upload']"
    upload_element = "//input[@id = 'file-upload-input-01']"
    landmark_radio = "//strong[contains(text(), 'Landmarks/Directions ')]"
    landmark_text = "//textarea[@class = 'slds-textarea mov-contact-textarea textarea uiInput uiInputTextArea uiInput--default uiInput--textarea']"
    first_name = "//input[@placeholder= 'First Name']"
    middle_name = "//input[@placeholder= 'Middle Name']"
    last_name = "//input[@placeholder= 'Last Name']"
    mobile_number = "//input[@placeholder= '+63xxxxxxxxxx']"
    landline = "//input[@placeholder= '+63(area code)xxxxxxx']"
    email = "//input[@placeholder= 'Email']"
    sms_checkbox = "//span[contains(text(), 'SMS')]"
    email_checkbox = "//span[contains(text(), 'Email')]"
    terms_checkbox = "//span[contains(text(), 'I have read and agree to the Meralco Online')]"
    submit = "//button[contains(text(), 'Submit')]"
    case_number = "//span[@class = 'text-orange mov-text_weight-bold']"
    existing_sin_report = "//li[contains(text(), 'A report has already been made for this Service ID Number.')]"
    province_metro_manila = "//option[@label= 'METRO MANILA']"
    city_pasig = "//option[@label= 'PASIG CITY']"
    barangay_bagong_ilog ="//option[@label= 'BAGONG ILOG']"
    subdivision_kawilihan = "//option[@label= 'KAWILIHAN VILL']"
    street_kabutihan = "//option[@label= 'KABUTIHAN']"
    street_no = "//input[@placeholder= 'Enter House/Unit/Floor/Building Number here*']"

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

    def get_unstable_power(self, driver):
        return WebMisc().clickable_element(driver, self.unstable_power, "unstable_power")

    def get_safety_concern(self, driver):
        return WebMisc().clickable_element(driver, self.safety_concern, "safety_concern")

    def get_select_safety_concern(self, driver):
        return WebMisc().clickable_element(driver, self.select_safety_concern, "select_safety_concern")

    def get_select_damage(self, driver):
        return WebMisc().clickable_element(driver, self.select_damage, "select_damage")

    def get_pole_broken(self, driver):
        return WebMisc().clickable_element(driver, self.pole_broken, "pole_broken")

    def get_safety_pole_broken(self, driver):
        return WebMisc().clickable_element(driver, self.safety_pole_broken, "safety_pole_broken")

    def get_lights_flickering(self, driver):
        return WebMisc().clickable_element(driver, self.lights_flickering, "lights_flickering")

    def get_upload_button(self, driver):
        return WebMisc().clickable_element(driver, self.upload_button, "upload_button")

    def get_upload_element(self, driver):
        return WebMisc().clickable_element(driver, self.upload_element, "upload_element")

    def get_landmark_text(self, driver):
        return WebMisc().clickable_element(driver, self.landmark_text, "landmark_text")

    def get_landmark_radio(self, driver):
        return WebMisc().clickable_element(driver, self.landmark_radio, "landmark_radio")

    def get_first_name(self, driver):
        return WebMisc().clickable_element(driver, self.first_name, "first_name")

    def get_middle_name(self, driver):
        return WebMisc().clickable_element(driver, self.middle_name, "middle_name")

    def get_last_name(self, driver):
        return WebMisc().clickable_element(driver, self.last_name, "last_name")

    def get_mobile_number(self, driver):
        return WebMisc().clickable_element(driver, self.mobile_number, "mobile_number")

    def get_landline(self, driver):
        return WebMisc().clickable_element(driver, self.landline, "landline")

    def get_email(self, driver):
        return WebMisc().clickable_element(driver, self.email, "email")

    def get_sms_checkbox(self, driver):
        return WebMisc().clickable_element(driver, self.sms_checkbox, "sms_checkbox")

    def get_email_checkbox(self, driver):
        return WebMisc().clickable_element(driver, self.email_checkbox, "email_checkbox")

    def get_terms_checkbox(self, driver):
        return WebMisc().clickable_element(driver, self.terms_checkbox, "terms_checkbox")

    def get_submit(self, driver):
        return WebMisc().clickable_element(driver, self.submit, "submit")

    def get_case_number(self, driver):
        return WebMisc().wait_element(driver, self.case_number, "case_number")

    def get_existing_sin_report(self, driver):
        return WebMisc().wait_element(driver, self.existing_sin_report, "existing_sin_report")

    def get_province_metro_manila(self, driver):
        return WebMisc().clickable_element(driver, self.province_metro_manila, "province_metro_manila")

    def get_city_pasig(self, driver):
        return WebMisc().clickable_element(driver, self.city_pasig, "city_pasig")

    def get_barangay_bagong_ilog(self, driver):
        return WebMisc().clickable_element(driver, self.barangay_bagong_ilog, "barangay_bagong_ilog")

    def get_subdivision_kawilihan(self, driver):
        return WebMisc().clickable_element(driver, self.subdivision_kawilihan, "subdivision_kawilihan")

    def get_street_kabutihan(self, driver):
        return WebMisc().clickable_element(driver, self.street_kabutihan, "street_kabutihan")

    def get_street_no(self, driver):
        return WebMisc().wait_element(driver, self.street_no, "street_no")
