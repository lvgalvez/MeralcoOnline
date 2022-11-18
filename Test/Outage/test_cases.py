import time

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.action_chains import ActionChains

from Pages.Page_CXE_Case import CXECasePage
from Pages.Page_CXE_Customer_Document import CXECustomerDocumentPage
from Pages.Page_CXE_Document import CXEDocumentPage
from Pages.Page_CXE_Home import CXEHomePage
from Pages.Page_CXE_Login import CXELoginPage
from Pages.Page_CXE_Page_Search import CXESearchPage
from Pages.Page_CXE_Question_Response import CXEQuestionResponsePage
from Pages.Page_CXE_Question_Responses import CXEQuestionResponsesPage
from Pages.Page_External_Outage import ExternalOutagePage
from Pages.Page_Internal_Outage import InternalOutagePage
from Pages.Page_Home import HomePage
from Pages.Page_Login import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from Pages.Page_Yopmail_Home import YopmailHomePage
from Test.Module_Functions.MO_Functions import *
from Utilities.Config import *
from Utilities.Functions import *
from Utilities.Utils import Utilities
from Test.Module_Functions import MO_Functions
fc = Functions()
log = Utilities().getlogger()
report_outage = ReportOutagePage()
yopmail_home = YopmailHomePage()
cxe_login = CXELoginPage()
cxe_home = CXEHomePage()
cxe_search = CXESearchPage()
cxe_cases = CXECasePage()
question_responses = CXEQuestionResponsesPage()
question_response = CXEQuestionResponsePage()
customer_document = CXECustomerDocumentPage()
int_outage = InternalOutagePage()
document = CXEDocumentPage()
module = "Outage"


def TC053(driver, ts_id, sin, first_name, middle_name, last_name, mobile_number, landline, email, cxe_email, cxe_password):
    test_case = "TC053"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Report_Outage(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(report_outage.get_no_power_street_radio(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    #
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(report_outage.get_select_damage(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    #
    fc.bookmark(module, ts_id, test_case, "Step 4")
    fc.click(report_outage.get_pole_broken(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")
    #
    fc.bookmark(module, ts_id, test_case, "Step 5")
    report_outage.get_upload_element(driver).send_keys(f"C:\\Users\\LouisVincentGalvez\\MeralcoOnlinePortal\\Data Files\\Sample Image.jpg")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")
    #
    fc.bookmark(module, ts_id, test_case, "Step 6")
    fc.click(report_outage.get_service_id_radio(driver))
    fc.input_text(report_outage.get_service_id_number(driver), sin)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 6")
    #
    fc.bookmark(module, ts_id, test_case, "Step 7")
    fc.click(report_outage.get_landmark_radio(driver))
    fc.input_text(report_outage.get_landmark_text(driver), "Sample Text")
    time.sleep(5)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 7")
    #
    fc.bookmark(module, ts_id, test_case, "Step 8")
    Tick_Location_Map(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 8")
    #
    fc.bookmark(module, ts_id, test_case, "Step 9")
    fc.input_text(report_outage.get_first_name(driver), first_name)
    fc.input_text(report_outage.get_middle_name(driver), middle_name)
    fc.input_text(report_outage.get_last_name(driver), last_name)
    fc.input_text(report_outage.get_mobile_number(driver), mobile_number)
    fc.input_text(report_outage.get_landline(driver), landline)
    fc.input_text(report_outage.get_email(driver), email)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 9")
    #
    fc.bookmark(module, ts_id, test_case, "Step 10")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 10")
    #
    fc.bookmark(module, ts_id, test_case, "Step 11")
    fc.click(report_outage.get_sms_checkbox(driver))
    fc.click(report_outage.get_email_checkbox(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 11")
    #
    fc.bookmark(module, ts_id, test_case, "Step 12")
    fc.click(report_outage.get_terms_checkbox(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 12")
    #
    fc.bookmark(module, ts_id, test_case, "Step 13")
    time.sleep(10)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 13")
    #
    fc.bookmark(module, ts_id, test_case, "Step 14")
    fc.click(report_outage.get_submit(driver))
    time.sleep(15)
    case_number = report_outage.get_case_number(driver).text
    #case_number = "22102250686"
    fc.screen_capture(driver, module, ts_id, test_case, "Step 14")

    fc.bookmark(module, ts_id, test_case, "Step 15")
    #
    fc.bookmark(module, ts_id, test_case, "Step 16")
    fc.new_tab(driver, yopmail)
    fc.input_text(yopmail_home.get_email(driver), email)
    fc.click(yopmail_home.get_check_inbox(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 16")

    fc.bookmark(module, ts_id, test_case, "Step 17")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Report_Outage(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 17")
    #
    fc.bookmark(module, ts_id, test_case, "Step 18")
    fc.click(report_outage.get_no_power_street_radio(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 18")
    #
    fc.bookmark(module, ts_id, test_case, "Step 19")
    fc.click(report_outage.get_select_damage(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 19")
    #
    fc.bookmark(module, ts_id, test_case, "Step 20")
    fc.click(report_outage.get_pole_broken(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 20")
    #
    fc.bookmark(module, ts_id, test_case, "Step 21")
    fc.page_down(driver, 1)
    fc.click(report_outage.get_service_id_radio(driver))
    fc.input_text(report_outage.get_service_id_number(driver), sin)
    fc.click(report_outage.get_service_id_radio(driver))
    sin_text = "A report has already been made for this Service ID Number."
    fc.verify_text(report_outage.get_existing_sin_report(driver), sin_text)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 21")

    fc.bookmark(module, ts_id, test_case, "Step 22")
    fc.new_tab(driver, cxe)
    fc.click(cxe_login.get_meralco_user_id(driver))
    # function.click(cxe_login.get_use_another_account(driver))
    fc.input_text(cxe_login.get_email(driver), cxe_email)
    fc.click(cxe_login.get_next(driver))
    fc.input_text(cxe_login.get_password(driver), cxe_password)
    fc.click(cxe_login.get_sign_in(driver))
    time.sleep(25)
    fc.click(cxe_login.get_stay_sign_no(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 22")

    fc.bookmark(module, ts_id, test_case, "Step 23")
    fc.click(cxe_home.get_search_button(driver))
    fc.input_text(cxe_home.get_search_input(driver), case_number)
    time.sleep(5)
    fc.click(cxe_home.get_suggestion_case(driver))
    fc.verify(cxe_cases.get_cases_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 23")

    fc.bookmark(module, ts_id, test_case, "Step 24")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 24")

    fc.bookmark(module, ts_id, test_case, "Step 25")
    fc.page_down(driver, 1)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 25")

    fc.bookmark(module, ts_id, test_case, "Step 26")
    fc.page_down(driver, 1)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 26")

    fc.bookmark(module, ts_id, test_case, "Step 27")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 27")

    fc.bookmark(module, ts_id, test_case, "Step 28")
    fc.modal_click(driver, cxe_cases.get_question_responses(driver))
    fc.verify(question_responses.get_question_responses_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 28")

    fc.bookmark(module, ts_id, test_case, "Step 29")
    fc.click(question_responses.get_question_first(driver))
    fc.verify(question_response.get_question_responses_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 29")

    fc.bookmark(module, ts_id, test_case, "Step 30")
    fc.click(question_response.get_close_tab(driver))
    fc.click(question_responses.get_question_second(driver))
    fc.verify(question_response.get_question_responses_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 30")

    fc.bookmark(module, ts_id, test_case, "Step 31")
    fc.click(question_response.get_close_tab(driver))
    fc.click(question_responses.get_close_tab(driver))
    fc.modal_click(driver, cxe_cases.get_customer_documents(driver))
    fc.verify(customer_document.get_question_response_text(driver))
    fc.click(customer_document.get_document_first(driver))
    fc.verify(document.get_document_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 31")

    fc.bookmark(module, ts_id, test_case, "Step 32")
    fc.page_down(driver, 1)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 32")

    fc.bookmark(module, ts_id, test_case, "Step 33")
    fc.click(document.get_document_url(driver))
    time.sleep(10)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 33")
    fc.click(cxe_cases.get_close_case(driver))

    #ADMS Steps
    fc.bookmark(module, ts_id, test_case, "Step 34")
    fc.bookmark(module, ts_id, test_case, "Step 35")
    fc.bookmark(module, ts_id, test_case, "Step 36")
    fc.bookmark(module, ts_id, test_case, "Step 37")
    fc.bookmark(module, ts_id, test_case, "Step 38")
    fc.bookmark(module, ts_id, test_case, "Step 39")


def TC054(driver, ts_id, sin, first_name, middle_name, last_name, mobile_number, landline, email, cxe_email,
          cxe_password):
    test_case = "TC054"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage.get_switch_frame(driver)
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Report_Outage(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(report_outage.get_unstable_power(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(report_outage.get_select_damage(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    fc.click(report_outage.get_lights_flickering(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")

    fc.bookmark(module, ts_id, test_case, "Step 5")
    report_outage.get_upload_element(driver).send_keys(
        f"C:\\Users\\LouisVincentGalvez\\MeralcoOnlinePortal\\Data Files\\Sample Image.jpg")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")

    fc.bookmark(module, ts_id, test_case, "Step 6")
    fc.click(report_outage.get_service_id_radio(driver))
    fc.input_text(report_outage.get_service_id_number(driver), sin)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 6")

    fc.bookmark(module, ts_id, test_case, "Step 7")
    fc.click(report_outage.get_landmark_radio(driver))
    fc.input_text(report_outage.get_landmark_text(driver), "Sample Text")
    time.sleep(5)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 7")

    fc.bookmark(module, ts_id, test_case, "Step 8")
    Tick_Location_Map(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 8")

    fc.bookmark(module, ts_id, test_case, "Step 9")
    fc.input_text(report_outage.get_first_name(driver), first_name)
    fc.input_text(report_outage.get_middle_name(driver), middle_name)
    fc.input_text(report_outage.get_last_name(driver), last_name)
    fc.input_text(report_outage.get_mobile_number(driver), mobile_number)
    fc.input_text(report_outage.get_landline(driver), landline)
    fc.input_text(report_outage.get_email(driver), email)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 9")

    fc.bookmark(module, ts_id, test_case, "Step 10")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 10")

    fc.bookmark(module, ts_id, test_case, "Step 11")
    fc.click(report_outage.get_sms_checkbox(driver))
    fc.click(report_outage.get_email_checkbox(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 11")

    fc.bookmark(module, ts_id, test_case, "Step 12")
    fc.click(report_outage.get_terms_checkbox(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 12")

    fc.bookmark(module, ts_id, test_case, "Step 13")
    time.sleep(10)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 13")

    fc.bookmark(module, ts_id, test_case, "Step 14")
    fc.click(report_outage.get_submit(driver))
    time.sleep(15)
    case_number = report_outage.get_case_number(driver).text
    #case_number = "22102250711"
    fc.screen_capture(driver, module, ts_id, test_case, "Step 14")

    fc.bookmark(module, ts_id, test_case, "Step 15")

    fc.bookmark(module, ts_id, test_case, "Step 16")
    fc.new_tab(driver, yopmail)
    fc.input_text(yopmail_home.get_email(driver), email)
    fc.click(yopmail_home.get_check_inbox(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 16")

    fc.bookmark(module, ts_id, test_case, "Step 17")
    fc.new_tab(driver, outage_external_guest)
    external_outage.get_switch_frame(driver)
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Report_Outage(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 17")

    fc.bookmark(module, ts_id, test_case, "Step 18")
    fc.click(report_outage.get_unstable_power(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 18")

    fc.bookmark(module, ts_id, test_case, "Step 19")
    fc.click(report_outage.get_select_damage(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 19")

    fc.bookmark(module, ts_id, test_case, "Step 20")
    fc.click(report_outage.get_lights_flickering(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 20")

    fc.bookmark(module, ts_id, test_case, "Step 21")
    fc.page_down(driver, 1)
    fc.click(report_outage.get_service_id_radio(driver))
    fc.input_text(report_outage.get_service_id_number(driver), sin)
    fc.click(report_outage.get_service_id_radio(driver))
    sin_text = "A report has already been made for this Service ID Number."
    fc.verify_text(report_outage.get_existing_sin_report(driver), sin_text)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 21")

    fc.bookmark(module, ts_id, test_case, "Step 22")
    fc.new_tab(driver, cxe)
    fc.click(cxe_login.get_meralco_user_id(driver))
    # function.click(cxe_login.get_use_another_account(driver))
    fc.input_text(cxe_login.get_email(driver), cxe_email)
    fc.click(cxe_login.get_next(driver))
    fc.input_text(cxe_login.get_password(driver), cxe_password)
    fc.click(cxe_login.get_sign_in(driver))
    time.sleep(25)
    fc.click(cxe_login.get_stay_sign_no(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 22")

    fc.bookmark(module, ts_id, test_case, "Step 23")
    fc.click(cxe_home.get_search_button(driver))
    fc.input_text(cxe_home.get_search_input(driver), case_number)
    time.sleep(5)
    fc.click(cxe_home.get_suggestion_case(driver))
    fc.verify(cxe_cases.get_cases_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 23")

    fc.bookmark(module, ts_id, test_case, "Step 24")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 24")

    fc.bookmark(module, ts_id, test_case, "Step 25")
    fc.page_down(driver, 1)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 25")

    fc.bookmark(module, ts_id, test_case, "Step 26")
    fc.page_down(driver, 1)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 26")

    fc.bookmark(module, ts_id, test_case, "Step 27")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 27")

    fc.bookmark(module, ts_id, test_case, "Step 28")
    fc.modal_click(driver, cxe_cases.get_question_responses(driver))
    fc.verify(question_responses.get_question_responses_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 28")

    fc.bookmark(module, ts_id, test_case, "Step 29")
    fc.click(question_responses.get_question_first(driver))
    fc.verify(question_response.get_question_responses_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 29")

    fc.bookmark(module, ts_id, test_case, "Step 30")
    fc.click(question_response.get_close_tab(driver))
    fc.click(question_responses.get_question_second(driver))
    fc.verify(question_response.get_question_responses_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 30")

    fc.bookmark(module, ts_id, test_case, "Step 31")
    fc.click(question_response.get_close_tab(driver))
    fc.click(question_responses.get_close_tab(driver))
    fc.modal_click(driver, cxe_cases.get_customer_documents(driver))
    fc.verify(customer_document.get_question_response_text(driver))
    fc.click(customer_document.get_document_first(driver))
    fc.verify(document.get_document_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 31")

    fc.bookmark(module, ts_id, test_case, "Step 32")
    fc.page_down(driver, 1)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 32")

    fc.bookmark(module, ts_id, test_case, "Step 33")
    fc.click(document.get_document_url(driver))
    time.sleep(10)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 33")
    fc.click(cxe_cases.get_close_case(driver))

    # ADMS Steps
    fc.bookmark(module, ts_id, test_case, "Step 34")
    fc.bookmark(module, ts_id, test_case, "Step 35")
    fc.bookmark(module, ts_id, test_case, "Step 36")
    fc.bookmark(module, ts_id, test_case, "Step 37")

def TC055(driver, ts_id, sin, first_name, middle_name, last_name, mobile_number, landline, email, cxe_email,
          cxe_password):
    test_case = "TC055"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage.get_switch_frame(driver)
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Report_Outage(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(report_outage.get_safety_concern(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(report_outage.get_select_safety_concern(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    fc.click(report_outage.get_safety_pole_broken(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")

    fc.bookmark(module, ts_id, test_case, "Step 5")
    report_outage.get_upload_element(driver).send_keys(
        f"C:\\Users\\LouisVincentGalvez\\MeralcoOnlinePortal\\Data Files\\Sample Image.jpg")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")

    fc.bookmark(module, ts_id, test_case, "Step 6")
    fc.click(report_outage.get_province_metro_manila(driver))
    fc.click(report_outage.get_city_pasig(driver))
    fc.click(report_outage.get_barangay_bagong_ilog(driver))
    fc.click(report_outage.get_subdivision_kawilihan(driver))
    fc.click(report_outage.get_street_kabutihan(driver))
    fc.input_text(report_outage.get_street_no(driver), "123")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 6")

    fc.bookmark(module, ts_id, test_case, "Step 7")
    fc.click(report_outage.get_landmark_radio(driver))
    fc.click(report_outage.get_landmark_radio(driver))
    fc.input_text(report_outage.get_landmark_text(driver), "Sample Text")
    time.sleep(5)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 7")

    fc.bookmark(module, ts_id, test_case, "Step 8")
    Tick_Location_Map(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 8")

    fc.bookmark(module, ts_id, test_case, "Step 9")
    fc.input_text(report_outage.get_first_name(driver), first_name)
    fc.input_text(report_outage.get_middle_name(driver), middle_name)
    fc.input_text(report_outage.get_last_name(driver), last_name)
    fc.input_text(report_outage.get_mobile_number(driver), mobile_number)
    fc.input_text(report_outage.get_landline(driver), landline)
    fc.input_text(report_outage.get_email(driver), email)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 9")

    fc.bookmark(module, ts_id, test_case, "Step 10")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 10")

    fc.bookmark(module, ts_id, test_case, "Step 11")
    fc.click(report_outage.get_sms_checkbox(driver))
    fc.click(report_outage.get_email_checkbox(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 11")

    fc.bookmark(module, ts_id, test_case, "Step 12")
    fc.click(report_outage.get_terms_checkbox(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 12")

    fc.bookmark(module, ts_id, test_case, "Step 13")
    time.sleep(10)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 13")

    fc.bookmark(module, ts_id, test_case, "Step 14")
    fc.click(report_outage.get_submit(driver))
    time.sleep(15)
    case_number = report_outage.get_case_number(driver).text
    # case_number = "22102250711"
    fc.screen_capture(driver, module, ts_id, test_case, "Step 14")

    fc.bookmark(module, ts_id, test_case, "Step 15")

    fc.bookmark(module, ts_id, test_case, "Step 16")
    fc.new_tab(driver, yopmail)
    fc.input_text(yopmail_home.get_email(driver), email)
    fc.click(yopmail_home.get_check_inbox(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 16")

    fc.bookmark(module, ts_id, test_case, "Step 17")
    fc.new_tab(driver, cxe)
    fc.click(cxe_login.get_meralco_user_id(driver))
    # function.click(cxe_login.get_use_another_account(driver))
    fc.input_text(cxe_login.get_email(driver), cxe_email)
    fc.click(cxe_login.get_next(driver))
    fc.input_text(cxe_login.get_password(driver), cxe_password)
    fc.click(cxe_login.get_sign_in(driver))
    time.sleep(25)
    fc.click(cxe_login.get_stay_sign_no(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 17")

    fc.bookmark(module, ts_id, test_case, "Step 18")
    fc.click(cxe_home.get_search_button(driver))
    fc.input_text(cxe_home.get_search_input(driver), case_number)
    time.sleep(5)
    fc.click(cxe_home.get_suggestion_case(driver))
    fc.verify(cxe_cases.get_cases_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 18")

    fc.bookmark(module, ts_id, test_case, "Step 19")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 19")

    fc.bookmark(module, ts_id, test_case, "Step 20")
    fc.page_down(driver, 1)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 20")

    fc.bookmark(module, ts_id, test_case, "Step 21")
    fc.page_down(driver, 1)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 21")

    fc.bookmark(module, ts_id, test_case, "Step 22")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 22")

    fc.bookmark(module, ts_id, test_case, "Step 23")
    fc.modal_click(driver, cxe_cases.get_question_responses(driver))
    fc.verify(question_responses.get_question_responses_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 23")

    fc.bookmark(module, ts_id, test_case, "Step 24")
    fc.click(question_responses.get_question_first(driver))
    fc.verify(question_response.get_question_responses_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 24")

    fc.bookmark(module, ts_id, test_case, "Step 25")
    fc.click(question_response.get_close_tab(driver))
    fc.click(question_responses.get_question_second(driver))
    fc.verify(question_response.get_question_responses_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 25")

    fc.bookmark(module, ts_id, test_case, "Step 26")
    fc.click(question_response.get_close_tab(driver))
    fc.click(question_responses.get_question_third(driver))
    fc.verify(question_response.get_question_responses_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 26")

    fc.bookmark(module, ts_id, test_case, "Step 27")
    fc.click(question_response.get_close_tab(driver))
    fc.click(question_responses.get_close_tab(driver))
    fc.modal_click(driver, cxe_cases.get_customer_documents(driver))
    fc.verify(customer_document.get_question_response_text(driver))
    fc.click(customer_document.get_document_first(driver))
    fc.verify(document.get_document_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 27")

    fc.bookmark(module, ts_id, test_case, "Step 28")
    fc.page_down(driver, 1)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 28")

    fc.bookmark(module, ts_id, test_case, "Step 29")
    fc.click(document.get_document_url(driver))
    time.sleep(10)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 29")
    fc.click(cxe_cases.get_close_case(driver))

    # ADMS Steps
    fc.bookmark(module, ts_id, test_case, "Step 30")
    fc.bookmark(module, ts_id, test_case, "Step 31")
    fc.bookmark(module, ts_id, test_case, "Step 32")
    fc.bookmark(module, ts_id, test_case, "Step 33")

def TC057(driver, ts_id, sin, first_name, middle_name, last_name, mobile_number, landline, email):
    test_case = "TC057"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Report_Outage(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(report_outage.get_no_power_radio(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(report_outage.get_report_dropdown(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    fc.click(report_outage.get_none(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")

    fc.bookmark(module, ts_id, test_case, "Step 5")
    fc.click(report_outage.get_service_id_radio(driver))
    fc.input_text(report_outage.get_service_id_number(driver), sin)
    fc.click(report_outage.get_service_id_radio(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")

    fc.bookmark(module, ts_id, test_case, "Step 6")
    # fc.click(report_outage.get_no_option(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 6")

    fc.bookmark(module, ts_id, test_case, "Step 7")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Report_Outage(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 7")

    fc.bookmark(module, ts_id, test_case, "Step 8")
    fc.click(report_outage.get_no_power_radio(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 8")

    fc.bookmark(module, ts_id, test_case, "Step 9")
    fc.click(report_outage.get_report_dropdown(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 9")

    fc.bookmark(module, ts_id, test_case, "Step 10")
    fc.click(report_outage.get_none(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 10")

    fc.bookmark(module, ts_id, test_case, "Step 11")
    fc.click(report_outage.get_service_id_radio(driver))
    fc.input_text(report_outage.get_service_id_number(driver), sin)
    fc.click(report_outage.get_service_id_radio(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 11")

    fc.bookmark(module, ts_id, test_case, "Step 12")
    # fc.click(report_outage.get_no_option(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 12")

    fc.bookmark(module, ts_id, test_case, "Step 13")
    fc.click(report_outage.get_landmark_radio(driver))
    # fc.click(report_outage.get_landmark_radio(driver))
    fc.input_text(report_outage.get_landmark_text(driver), "Sample Text")
    time.sleep(5)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 13")

    fc.bookmark(module, ts_id, test_case, "Step 14")
    fc.input_text(report_outage.get_first_name(driver), first_name)
    fc.input_text(report_outage.get_middle_name(driver), middle_name)
    fc.input_text(report_outage.get_last_name(driver), last_name)
    fc.input_text(report_outage.get_mobile_number(driver), mobile_number)
    fc.input_text(report_outage.get_landline(driver), landline)
    fc.input_text(report_outage.get_email(driver), email)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 14")

    fc.bookmark(module, ts_id, test_case, "Step 15")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 15")
    #
    fc.bookmark(module, ts_id, test_case, "Step 16")
    fc.click(report_outage.get_sms_checkbox(driver))
    fc.click(report_outage.get_email_checkbox(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 16")

    fc.bookmark(module, ts_id, test_case, "Step 17")
    fc.click(report_outage.get_terms_checkbox(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 17")

    #
    fc.bookmark(module, ts_id, test_case, "Step 18")
    fc.click(report_outage.get_submit(driver))
    time.sleep(15)
    case_number = report_outage.get_case_number(driver).text
    # case_number = "22102250686"
    fc.screen_capture(driver, module, ts_id, test_case, "Step 18")

    fc.bookmark(module, ts_id, test_case, "Step 19")
    #
    fc.bookmark(module, ts_id, test_case, "Step 20")
    fc.new_tab(driver, yopmail)
    fc.input_text(yopmail_home.get_email(driver), email)
    fc.click(yopmail_home.get_check_inbox(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 20")


def TC058(driver, ts_id, first_name, middle_name, last_name, mobile_number, landline, email):
    test_case = "TC058"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Report_Outage(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(report_outage.get_streelight_power(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    #
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(report_outage.get_select_yes(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    #
    fc.bookmark(module, ts_id, test_case, "Step 4")
    fc.click(report_outage.get_dropdown(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")
    #
    fc.bookmark(module, ts_id, test_case, "Step 5")
    fc.click(report_outage.get_dropdown_value(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")
    #
    fc.bookmark(module, ts_id, test_case, "Step 6")
    fc.click(report_outage.get_province_metro_manila(driver))
    fc.click(report_outage.get_city_pasig(driver))
    fc.click(report_outage.get_barangay_bagong_ilog(driver))
    fc.click(report_outage.get_subdivision_kawilihan(driver))
    fc.click(report_outage.get_street_kabutihan(driver))
    fc.input_text(report_outage.get_street_no(driver), "123")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 6")

    #
    fc.bookmark(module, ts_id, test_case, "Step 7")
    fc.input_text(report_outage.get_pole_number(driver), "52")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 7")
    #
    fc.bookmark(module, ts_id, test_case, "Step 8")
    fc.click(report_outage.get_landmark_radio(driver))
    fc.click(report_outage.get_landmark_radio(driver))
    # fc.click(report_outage.get_landmark_radio(driver))
    fc.input_text(report_outage.get_landmark_text(driver), "Sample Text")
    time.sleep(5)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 8")
    #
    fc.bookmark(module, ts_id, test_case, "Step 9")
    fc.input_text(report_outage.get_first_name(driver), first_name)
    fc.input_text(report_outage.get_middle_name(driver), middle_name)
    fc.input_text(report_outage.get_last_name(driver), last_name)
    fc.input_text(report_outage.get_mobile_number(driver), mobile_number)
    fc.input_text(report_outage.get_landline(driver), landline)
    fc.input_text(report_outage.get_email(driver), email)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 9")
    #
    fc.bookmark(module, ts_id, test_case, "Step 10")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 10")
    #
    fc.bookmark(module, ts_id, test_case, "Step 11")
    fc.click(report_outage.get_sms_checkbox(driver))
    fc.click(report_outage.get_email_checkbox(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 11")
    #
    fc.bookmark(module, ts_id, test_case, "Step 12")
    fc.click(report_outage.get_terms_checkbox(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 12")
    #
    fc.bookmark(module, ts_id, test_case, "Step 13")
    fc.click(report_outage.get_submit(driver))
    time.sleep(15)
    case_number = report_outage.get_case_number(driver).text
    # case_number = "22102250686"
    fc.screen_capture(driver, module, ts_id, test_case, "Step 13")

    fc.bookmark(module, ts_id, test_case, "Step 14")
    #
    fc.bookmark(module, ts_id, test_case, "Step 15")
    fc.new_tab(driver, yopmail)
    fc.input_text(yopmail_home.get_email(driver), email)
    fc.click(yopmail_home.get_check_inbox(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 15")

    fc.bookmark(module, ts_id, test_case, "Step 16")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Report_Outage(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 16")
    #
    fc.bookmark(module, ts_id, test_case, "Step 17")
    fc.click(report_outage.get_streelight_power(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 17")
    #
    fc.bookmark(module, ts_id, test_case, "Step 18")
    fc.click(report_outage.get_select_yes(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 18")
    #
    fc.bookmark(module, ts_id, test_case, "Step 19")
    fc.click(report_outage.get_dropdown(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 19")
    #
    fc.bookmark(module, ts_id, test_case, "Step 20")
    fc.click(report_outage.get_dropdown_value_flickering(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 20")

    fc.bookmark(module, ts_id, test_case, "Step 21")
    fc.click(report_outage.get_province_metro_manila(driver))
    fc.click(report_outage.get_city_pasig(driver))
    fc.click(report_outage.get_barangay_bagong_ilog(driver))
    fc.click(report_outage.get_subdivision_kawilihan(driver))
    fc.click(report_outage.get_street_kabutihan(driver))
    fc.input_text(report_outage.get_street_no(driver), "123")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 21")
    #
    fc.bookmark(module, ts_id, test_case, "Step 22")
    fc.input_text(report_outage.get_pole_number(driver), "52")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 22")
    # function.click(cxe_login.get_use_another_account(driver))

    fc.bookmark(module, ts_id, test_case, "Step 23")
    fc.click(report_outage.get_landmark_radio(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 23")

    time.sleep(4)
    fc.bookmark(module, ts_id, test_case, "Step 24")
    fc.modal_click(driver, report_outage.get_no_option(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 24")

    fc.bookmark(module, ts_id, test_case, "Step 25")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Report_Outage(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 25")
    #
    fc.bookmark(module, ts_id, test_case, "Step 26")
    fc.click(report_outage.get_streelight_power(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 26")
    #
    fc.bookmark(module, ts_id, test_case, "Step 27")
    fc.click(report_outage.get_select_yes(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 27")
    #
    fc.bookmark(module, ts_id, test_case, "Step 28")
    fc.click(report_outage.get_dropdown(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 28")
    #
    fc.bookmark(module, ts_id, test_case, "Step 29")
    fc.click(report_outage.get_value_streetlightisnot(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 29")

    fc.bookmark(module, ts_id, test_case, "Step 30")
    fc.click(report_outage.get_province_metro_manila(driver))
    fc.click(report_outage.get_city_pasig(driver))
    fc.click(report_outage.get_barangay_bagong_ilog(driver))
    fc.click(report_outage.get_subdivision_kawilihan(driver))
    fc.click(report_outage.get_street_kabutihan(driver))
    fc.input_text(report_outage.get_street_no(driver), "123")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 30")
    #
    fc.bookmark(module, ts_id, test_case, "Step 31")
    fc.input_text(report_outage.get_pole_number(driver), "52")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 31")
    # function.click(cxe_login.get_use_another_account(driver))

    fc.bookmark(module, ts_id, test_case, "Step 32")
    fc.click(report_outage.get_label(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 32")

    fc.bookmark(module, ts_id, test_case, "Step 33")
    fc.modal_click(driver, report_outage.get_yes_option(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 33")
    time.sleep(4)

    fc.bookmark(module, ts_id, test_case, "Step 34")
    fc.click(report_outage.get_landmark_radio(driver))
    fc.click(report_outage.get_landmark_radio(driver))
    # fc.click(report_outage.get_landmark_radio(driver))
    fc.input_text(report_outage.get_landmark_text(driver), "Sample Text")
    time.sleep(5)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 34")
    #
    fc.bookmark(module, ts_id, test_case, "Step 35")
    fc.input_text(report_outage.get_first_name(driver), first_name)
    fc.input_text(report_outage.get_middle_name(driver), middle_name)
    fc.input_text(report_outage.get_last_name(driver), last_name)
    fc.input_text(report_outage.get_mobile_number(driver), mobile_number)
    fc.input_text(report_outage.get_landline(driver), landline)
    fc.input_text(report_outage.get_email(driver), email)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 35")
    #
    fc.bookmark(module, ts_id, test_case, "Step 36")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 36")
    #
    fc.bookmark(module, ts_id, test_case, "Step 37")
    fc.click(report_outage.get_sms_checkbox(driver))
    fc.click(report_outage.get_email_checkbox(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 37")

    fc.bookmark(module, ts_id, test_case, "Step 38")
    fc.click(report_outage.get_terms_checkbox(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 38")

    #
    fc.bookmark(module, ts_id, test_case, "Step 39")
    fc.click(report_outage.get_submit(driver))
    time.sleep(15)
    case_number = report_outage.get_case_number(driver).text
    # case_number = "22102250686"
    fc.screen_capture(driver, module, ts_id, test_case, "Step 39")

    fc.bookmark(module, ts_id, test_case, "Step 40")
    #
    fc.bookmark(module, ts_id, test_case, "Step 41")
    fc.new_tab(driver, yopmail)
    fc.input_text(yopmail_home.get_email(driver), email)
    fc.click(yopmail_home.get_check_inbox(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 41")


def TC059(driver, ts_id):
    test_case = "TC059"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage.get_switch_frame(driver)
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Report_Outage(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(report_outage.get_streelight_power(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(report_outage.get_no(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    fc.click(report_outage.get_learn_more(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")


def TC060(driver, ts_id, email, password, weather, zoom_level):
    test_case = "TC060"
    default_zoom = 9
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, internal_outage)
    fc.input_text(cxe_login.get_email(driver), email)
    fc.click(cxe_login.get_next(driver))
    fc.input_text(cxe_login.get_password(driver), password)
    fc.click(cxe_login.get_sign_in(driver))
    fc.click(cxe_login.get_sms(driver))
    time.sleep(25)
    fc.click(cxe_login.get_stay_sign_no(driver))
    internaloutage = InternalOutagePage()
    # internaloutage.get_switch_frame(driver)
    time.sleep(4)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.modal_click(driver, internaloutage.get_menu(driver))
    fc.modal_click(driver, internaloutage.get_map_display(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.modal_click(driver, internaloutage.get_weather_click(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.modal_click(driver, internaloutage.get_internal_modal(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    # internaloutage.get_switch_frame(driver)
    fc.bookmark(module, ts_id, test_case, "Step 4")
    Adjust_Zoom_Level_Internal(driver, default_zoom, zoom_level)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")

    fc.bookmark(module, ts_id, test_case, "Step 5")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")


def TC061a(driver, ts_id, email, password, weather, zoom_level):
    test_case = "TC061"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    Navigate_Outage(driver)
    default_zoom = Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    Select_Weather_Information(driver, weather)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Adjust_Zoom_Level(driver, default_zoom, zoom_level)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")


def TC061b(driver, ts_id, weather, zoom_level):
    test_case = "TC061"
    default_zoom = 9
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    Select_Weather_Information(driver, weather)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Adjust_Zoom_Level(driver, default_zoom, zoom_level)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")

def TC062(driver, ts_id, email, password):
    test_case = "TC062"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, internal_outage)
    fc.input_text(cxe_login.get_email(driver), email)
    fc.click(cxe_login.get_next(driver))
    fc.input_text(cxe_login.get_password(driver), password)
    fc.click(cxe_login.get_sign_in(driver))
    fc.click(cxe_login.get_sms(driver))
    time.sleep(25)
    fc.click(cxe_login.get_stay_sign_no(driver))
    internaloutage = InternalOutagePage()
   # internaloutage.get_switch_frame(driver)
    time.sleep(4)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

def TC063(driver, ts_id):
    test_case = "TC063"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, internal_outage)
    Login_CXE(driver)
    time.sleep(1000)

    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    print("Done")


def TC064(driver, ts_id):
    test_case = "TC064"
    fc.bookmark(module, ts_id, test_case, "Step 1")

def TC065(driver, ts_id):
    test_case = "TC065"
    fc.bookmark(module, ts_id, test_case, "Step 1")

    homepage = CXEHomePage()
    homepage.get_profile_options(driver)
    fc.click(homepage.logout_account(driver))
    fc.accept_alert(driver)

    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

def TC066(driver, ts_id):
    test_case = "TC066"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, internal_outage)

    Login_CXE(driver)
    homepage = CXEHomePage()
    internaloutage = InternalOutagePage()
   # internaloutage.get_switch_frame(driver)
    time.sleep(15)
    internaloutage.get_meralco_header(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")


def TC067(driver, ts_id):
    test_case = "TC067"
    fc.bookmark(module, ts_id, test_case, "Step 1")

    internaloutage = InternalOutagePage()
    fc.click(internaloutage.get_faq_header(driver))
    time.sleep(5)
    FAQ_Page = driver.window_handles[1]
    fc.switch_window_tab(driver,FAQ_Page)
    time.sleep(10)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    driver.close()

def TC068(driver, ts_id):
    test_case = "TC068"
    outagePage = InternalOutagePage()

    fc.bookmark(module, ts_id, test_case, "Step 1")

    Outage_Page = driver.window_handles[0]
    fc.switch_window_tab(driver, Outage_Page)

    fc.click(outagePage.get_qrg_header(driver))
    time.sleep(5)

    QRG_Page = driver.window_handles[1]
    fc.switch_window_tab(driver, QRG_Page)
    time.sleep(10)

    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    driver.close()

def TC069(driver, ts_id):
    test_case = "TC069"
    outagePage = InternalOutagePage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, internal_outage)

    Login_CXE(driver)

    #fc.click(outagePage.get_menu(driver))
    outagePage.get_menu(driver).click()
    time.sleep(5)
    outagePage.get_quick_links(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")


    fc.bookmark(module, ts_id, test_case, "Step 2")
    outagePage.get_bfp_link(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")



    time.sleep(5)
    print("Done of execution")

def TC070(driver, ts_id, email, password):
    test_case = "TC070"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, internal_outage)
    fc.input_text(cxe_login.get_email(driver), email)
    fc.click(cxe_login.get_next(driver))
    fc.input_text(cxe_login.get_password(driver), password)
    fc.click(cxe_login.get_sign_in(driver))
    fc.click(cxe_login.get_sms(driver))
    time.sleep(25)
    fc.click(cxe_login.get_stay_sign_no(driver))
    internaloutage = InternalOutagePage()
   # internaloutage.get_switch_frame(driver)
    time.sleep(4)
    fc.click(internaloutage.get_center_map(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

def TC071(driver, ts_id):
    test_case = "TC071"
    outagePage = InternalOutagePage()

    fc.bookmark(module, ts_id, test_case, "Step 1")

    Outage_tab = driver.window_handles[0]
    fc.switch_window_tab(driver, Outage_tab)

    outagePage.enter_search(driver,Outage['auto-search-data'])
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    outagePage.get_auto_suggest(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    time.sleep(5)
    print("Done of execution")

def TC072(driver, ts_id, email, password):
    test_case = "TC072"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, internal_outage)
    fc.input_text(cxe_login.get_email(driver), email)
    fc.click(cxe_login.get_next(driver))
    fc.input_text(cxe_login.get_password(driver), password)
    fc.click(cxe_login.get_sign_in(driver))
    fc.click(cxe_login.get_sms(driver))
    time.sleep(25)
    fc.click(cxe_login.get_stay_sign_no(driver))
    internaloutage = InternalOutagePage()
   # internaloutage.get_switch_frame(driver)
    time.sleep(4)
    fc.click(internaloutage.get_refresh_button(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")


def TC073(driver, ts_id, email, password):
    test_case = "TC073"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, internal_outage)
    fc.input_text(cxe_login.get_email(driver), email)
    fc.click(cxe_login.get_next(driver))
    fc.input_text(cxe_login.get_password(driver), password)
    fc.click(cxe_login.get_sign_in(driver))
    fc.click(cxe_login.get_sms(driver))
    time.sleep(25)
    fc.click(cxe_login.get_stay_sign_no(driver))
    internaloutage = InternalOutagePage()
   # internaloutage.get_switch_frame(driver)
    time.sleep(4)

    fc.modal_click(driver, internaloutage.get_menu(driver))
    fc.modal_click(driver, internaloutage.get_admin(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

def TC076(driver, ts_id, email, password):
    test_case = "TC076"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, internal_outage)
    fc.input_text(cxe_login.get_email(driver), email)
    fc.click(cxe_login.get_next(driver))
    fc.input_text(cxe_login.get_password(driver), password)
    fc.click(cxe_login.get_sign_in(driver))
    fc.click(cxe_login.get_sms(driver))
    time.sleep(25)
    fc.click(cxe_login.get_stay_sign_no(driver))
    internaloutage = InternalOutagePage()
   # internaloutage.get_switch_frame(driver)
    time.sleep(4)
    fc.modal_click(driver, internaloutage.get_map_view_internal(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

def TC077(driver, ts_id, email, password):
    test_case = "TC077"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, internal_outage)
    fc.input_text(cxe_login.get_email(driver), email)
    fc.click(cxe_login.get_next(driver))
    fc.input_text(cxe_login.get_password(driver), password)
    fc.click(cxe_login.get_sign_in(driver))
    fc.click(cxe_login.get_sms(driver))
    time.sleep(25)
    fc.click(cxe_login.get_stay_sign_no(driver))
    internaloutage = InternalOutagePage()
   # internaloutage.get_switch_frame(driver)
    time.sleep(4)
    fc.modal_click(driver, internaloutage.get_map_view_internal(driver))
    fc.modal_click(driver, internaloutage.get_sattelite(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

def TC078(driver, ts_id, email, password):
    test_case = "TC078"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, internal_outage)
    fc.input_text(cxe_login.get_email(driver), email)
    fc.click(cxe_login.get_next(driver))
    fc.input_text(cxe_login.get_password(driver), password)
    fc.click(cxe_login.get_sign_in(driver))
    fc.click(cxe_login.get_sms(driver))
    time.sleep(25)
    fc.click(cxe_login.get_stay_sign_no(driver))
    internaloutage = InternalOutagePage()
   # internaloutage.get_switch_frame(driver)
    time.sleep(4)
    fc.modal_click(driver, internaloutage.get_map_view_internal(driver))
    fc.modal_click(driver, internaloutage.get_sattelite(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

def TC085(driver, ts_id):
    test_case = "TC085"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, internal_outage)

    Login_CXE(driver)

    internaloutage = InternalOutagePage()

    fc.modal_click(driver, internaloutage.get_menu(driver))
    fc.modal_click(driver, internaloutage.get_outage_area(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.modal_click(driver, internaloutage.get_sector(driver))
    fc.modal_click(driver, internaloutage.get_sector_value(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    time.sleep(2)
    fc.modal_click(driver, internaloutage.get_outage_area(driver))
    internaloutage.close_burger_menu(driver)

def TC086(driver, ts_id):
    test_case = "TC086"
    fc.bookmark(module, ts_id, test_case, "Step 1")

    internaloutage = InternalOutagePage()
   # internaloutage.get_switch_frame(driver)
    time.sleep(4)

    fc.modal_click(driver, internaloutage.get_menu(driver))
    fc.modal_click(driver, internaloutage.get_outage_area(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.modal_click(driver, internaloutage.get_area_level(driver))
    fc.modal_click(driver, internaloutage.get_area_value(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC087(driver, ts_id):
    test_case = "TC087"
    fc.bookmark(module, ts_id, test_case, "Step 1")

    internaloutage = InternalOutagePage()
   # internaloutage.get_switch_frame(driver)
    time.sleep(4)

    fc.modal_click(driver, internaloutage.get_menu(driver))
    fc.modal_click(driver, internaloutage.get_outage_area(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.modal_click(driver, internaloutage.get_sector(driver))
    fc.modal_click(driver, internaloutage.get_sector_value(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.modal_click(driver, internaloutage.get_political_boundary(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")


def TC088(driver, ts_id, email, password):
    test_case = "TC088"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, "https://outage-api.meralco.com.ph/")
    Login_Internal_Outage(driver, email, password)
    #fc.click(int_outage.get_refresh_button(driver))
    time.sleep(20)
    fc.click(int_outage.get_hamburger_menu(driver))
    time.sleep(2)
    fc.click(int_outage.get_map_display(driver))
    time.sleep(2)
    fc.click(int_outage.get_outage_pins_filter(driver))
    fc.scroll_element(driver, int_outage.get_scheduled_interruption(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(int_outage.get_incident_type(driver))
    fc.scroll_element(driver, int_outage.get_scheduled_interruption(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.scroll_element(driver, int_outage.get_outage_load_shedding(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2b")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(int_outage.get_date_restoration(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    fc.click(int_outage.get_restoration_today(driver))
    time.sleep(5)
    fc.modal_click(driver, int_outage.get_alert_modal(driver))
    fc.click(int_outage.get_calendar_show(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")

    fc.bookmark(module, ts_id, test_case, "Step 5")
    fc.click(int_outage.get_affected_facility_type(driver))
    fc.scroll_element(driver, int_outage.get_scheduled_interruption(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")
    fc.scroll_element(driver, int_outage.get_type_no_device(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5b")

def TC089(driver, ts_id):
    test_case = "TC089"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.click(int_outage.get_incident_type(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

def TC090(driver, ts_id):
    test_case = "TC090"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.click(int_outage.get_incident_type(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(int_outage.get_menu_affected_areas(driver))
    time.sleep(10)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.click(int_outage.get_by_percentage(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2b")
def TC091(driver, ts_id):
    test_case = "TC091"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    #Select Outage PIN
    time.sleep(15)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

def TC093(driver, ts_id):
    test_case = "TC093"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.click(int_outage.get_main_affected_facility(driver))
    time.sleep(5)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

def TC094(driver, ts_id):
    test_case = "TC094"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.click(int_outage.get_affected_areas(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(int_outage.get_interruption_back(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")

def TC095(driver, ts_id):
    test_case = "TC095"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.click(int_outage.get_incident_status_history(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    time.sleep(5)
    fc.click(int_outage.get_interruption_back(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")

def TC096(driver, ts_id):
    test_case = "TC096"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.click(int_outage.get_get_directions(driver))
    #fc.accept_alert(driver)
    time.sleep(15)
    driver.switch_to.window(driver.window_handles[1])
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    driver.switch_to.window(driver.window_handles[0])
    #driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
    #fc.close_tab(driver)
    time.sleep(5)

def TC097(driver, ts_id):
    test_case = "TC097"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.click(int_outage.get_menu_affected_areas(driver))
    time.sleep(2)
    fc.click(int_outage.get_menu_affected_areas(driver))
    time.sleep(10)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

def TC098(driver, ts_id):
    test_case = "TC098"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.click(int_outage.get_by_percentage(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")

def TC099(driver, ts_id):
    test_case = "TC099"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.click(int_outage.get_by_count(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

def TC100(driver, ts_id):
    test_case = "TC0100"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.click(int_outage.get_outage_pins_filter(driver))
    #SELECT OUTAGE PIN
    time.sleep(10)
    fc.click(int_outage.get_affected_areas(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

def TC115(driver, ts_id):
    test_case = "TC0115"
    internalOutage = InternalOutagePage()
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, internal_outage)

    Login_CXE(driver)



    fc.modal_click(driver, internalOutage.get_menu(driver))
    internalOutage.get_search_locations(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")


    fc.bookmark(module, ts_id, test_case, "Step 2")
    internalOutage.search_by_sin(driver, Outage['search_loc_sin'])
    time.sleep(5)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    internalOutage.get_search_locations(driver)
    internalOutage.close_burger_menu(driver)

def TC116(driver, ts_id):
    test_case = "TC0116"
    internaloutage = InternalOutagePage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.modal_click(driver, internaloutage.get_menu(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    internaloutage.get_search_locations(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    internaloutage.get_search_locations(driver)
    internaloutage.close_burger_menu(driver)


def TC117(driver, ts_id):
    time.sleep(5)
    test_case = "TC0117"
    internalOutage = InternalOutagePage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.modal_click(driver, internalOutage.get_menu(driver))
    internalOutage.get_search_locations(driver)
    internalOutage.search_by_sin(driver, Outage['search_loc_sin'])
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    internalOutage.get_search_locations(driver)
    internalOutage.close_burger_menu(driver)

def TC118(driver, ts_id):
    test_case = "TC0118"
    internalOutage = InternalOutagePage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.modal_click(driver, internalOutage.get_menu(driver))
    internalOutage.get_search_locations(driver)
    fc.modal_click(internalOutage.search_select_services(driver))
    fc.modal_click(internalOutage.get_search_service(driver,'Facility'))
    internalOutage.search_by_facility(driver, Outage['search_loc_facility'])
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

def TC119(driver, ts_id):
    test_case = "TC0118"
    internalOutage = InternalOutagePage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.modal_click(internalOutage.search_select_services(driver))
    fc.modal_click(internalOutage.get_search_service(driver, 'Incident ID'))

def TC108(driver, ts_id, email, password):
    test_case = "TC108"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, "https://outage-api.meralco.com.ph/")
    Login_Internal_Outage(driver, email, password)
    #fc.click(int_outage.get_refresh_button(driver))
    time.sleep(20)
    fc.click(int_outage.get_hamburger_menu(driver))
    time.sleep(2)
    fc.click(int_outage.get_map_display(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    time.sleep(2)
    fc.click(int_outage.get_concern_reported_chk(driver))
    time.sleep(10)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(int_outage.get_concern_reported_filter(driver))
    fc.scroll_element(driver, int_outage.get_scheduled_interruption(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(int_outage.get_concern_type(driver))
    fc.scroll_element(driver, int_outage.get_scheduled_interruption(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(int_outage.get_case_status(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    fc.click(int_outage.get_reported_date(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")

    fc.bookmark(module, ts_id, test_case, "Step 5")
    fc.click(int_outage.get_date_highlight(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")

    fc.bookmark(module, ts_id, test_case, "Step 6")
    time.sleep(40)
    #Manual click of concern
    fc.screen_capture(driver, module, ts_id, test_case, "Step 6")


def TC109(driver, ts_id,):
    test_case = "TC109"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.click(int_outage.get_outage_pins_filter(driver))
    time.sleep(2)
    fc.scroll_element(driver, int_outage.get_scheduled_interruption(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(int_outage.get_incident_type(driver))
    fc.scroll_element(driver, int_outage.get_scheduled_interruption(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.scroll_element(driver, int_outage.get_outage_load_shedding(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2b")

def TC110(driver, ts_id,):
    test_case = "TC110"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.click(int_outage.get_incident_type(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(int_outage.get_date_restoration(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(int_outage.get_restoration_today(driver))
    time.sleep(5)
    fc.modal_click(driver, int_outage.get_alert_modal(driver))
    fc.click(int_outage.get_calendar_show(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

def TC111(driver, ts_id,):
    test_case = "TC111"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.click(int_outage.get_date_restoration(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(int_outage.get_affected_facility_type(driver))
    fc.scroll_element(driver, int_outage.get_scheduled_interruption(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.scroll_element(driver, int_outage.get_type_no_device(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2b")

def TC112(driver, ts_id, email, password):
    test_case = "TC112"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, "https://outage-api.meralco.com.ph/")
    Login_Internal_Outage(driver, email, password)
    #fc.click(int_outage.get_refresh_button(driver))
    time.sleep(20)
    fc.click(int_outage.get_hamburger_menu(driver))
    time.sleep(2)
    fc.click(int_outage.get_map_display(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    time.sleep(2)
    fc.click(int_outage.get_sector_office(driver))
    time.sleep(5)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.coordinates_click(driver, 150, 150)
    time.sleep(20)
    fc.verify(int_outage.get_sector_office(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC113(driver, ts_id):
    test_case = "TC113"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.modal_click(driver, int_outage.get_election_center(driver))
    time.sleep(20)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.coordinates_click(driver, 150, 150)
    time.sleep(20)
    fc.verify(int_outage.get_election_center(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC114(driver, ts_id):
    test_case = "TC114"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.modal_click(driver, int_outage.get_vital_custom(driver))
    time.sleep(20)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.modal_click(driver, int_outage.get_vital_pin(driver))
    time.sleep(20)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC124(driver, ts_id):
    test_case = "TC124"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Verify_GPS_Prompt(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    Handle_GPS_Prompt(driver, "Agree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")


def TC125(driver, ts_id):
    test_case = "TC125"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Verify_GPS_Prompt(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    Handle_GPS_Prompt(driver, "Disagree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")


def TC126(driver, ts_id, email, password):
    test_case = "TC126"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Navigate_Outage(driver)
    Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    Tick_Current_Address(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Verify_GPS_Prompt(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    Handle_GPS_Prompt(driver, "Agree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")


def TC127(driver, ts_id, email, password):
    test_case = "TC127"
    fc.new_tab(driver, meralco_online)

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Navigate_Outage(driver)
    Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    Tick_Current_Address(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Verify_GPS_Prompt(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    Handle_GPS_Prompt(driver, "Disagree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")


def TC143(driver, ts_id):
    test_case = "TC143"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Adjust_Zoom_Level(driver, 8, 9)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    Adjust_Zoom_Level(driver, 9, 8)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")


def TC144(driver, ts_id, email, password):
    test_case = "TC144"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, meralco_online)
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Navigate_Outage(driver)
    Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    Adjust_Zoom_Level(driver, 8, 9)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")

    fc.bookmark(module, ts_id, test_case, "Step 5")
    Adjust_Zoom_Level(driver, 9, 8)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")

def TC145(driver, ts_id):
    test_case = "TC145"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Click_Current_Location(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC146(driver, ts_id, email, password):
    test_case = "TC146"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, meralco_online)
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Navigate_Outage(driver)
    Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Click_Current_Location(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

def TC147(driver, ts_id):
    test_case = "TC145"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Click_Outage_Pin(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")


def TC128(driver, ts_id, email, password):
    test_case = "TC128"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Handle_GPS_Prompt(driver, "Disagree")
    Verify_Yellow_Banner(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.new_tab(driver, meralco_online)
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    Navigate_Outage(driver)
    Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")

    fc.bookmark(module, ts_id, test_case, "Step 5")
    Verify_Yellow_Banner(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")


def TC129(driver, ts_id, sin):
    test_case = "TC129"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Click_Report_Outage(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Required_Field_Population(driver, sin)
    Tick_Location_Map(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")


def TC130(driver, ts_id, sin, email, password):
    test_case = "TC130"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, meralco_online)
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Navigate_Outage(driver)
    Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Click_Report_Outage(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    Required_Field_Population_User(driver, sin)
    Tick_Location_Map_User(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")



def TC131(driver, ts_id):
    test_case = "TC131"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Click_Refresh_Button(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")


def TC132(driver, ts_id, email, password):
    test_case = "TC132"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, meralco_online)
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Navigate_Outage(driver)
    Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Click_Refresh_Button(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")


def TC133(driver, ts_id):
    test_case = "TC133"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Click_Legends_Guest(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")


def TC134(driver, ts_id, email, password):
    test_case = "TC134"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, meralco_online)
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Navigate_Outage(driver)
    Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Click_Legends_User(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")


def TC135(driver, ts_id):
    test_case = "TC135"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    Select_Map_Type(driver, "Default")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")


def TC136(driver, ts_id):
    test_case = "TC136"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    Select_Map_Type(driver, "Satellite")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")


def TC137(driver, ts_id):
    test_case = "TC137"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    Select_Map_Type(driver, "Terrain")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")


def TC138(driver, ts_id, email, password):
    test_case = "TC138"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, meralco_online)
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Navigate_Outage(driver)
    Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    Select_Map_Type(driver, "Default")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")


def TC139(driver, ts_id, email, password):
    test_case = "TC139"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, meralco_online)
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Navigate_Outage(driver)
    Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    Select_Map_Type(driver, "Satellite")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")


def TC140(driver, ts_id, email, password):
    test_case = "TC140"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, meralco_online)
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Navigate_Outage(driver)
    Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    Select_Map_Type(driver, "Terrain")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")


def TC141(driver, ts_id):
    test_case = "TC141"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Agree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Click_Other_Address(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    Click_Anywhere_Map(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")


def TC142(driver, ts_id, email, password):
    test_case = "TC142"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, meralco_online)
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Navigate_Outage(driver)
    Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.verify(external_outage.get_address_radio(driver))
    fc.verify(external_outage.get_service_radio(driver))
    fc.verify(external_outage.get_reports_radio(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")

    fc.bookmark(module, ts_id, test_case, "Step 5")
    fc.click(external_outage.get_address_radio(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")

    fc.bookmark(module, ts_id, test_case, "Step 6")
    Click_Anywhere_Map(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 6")

    fc.bookmark(module, ts_id, test_case, "Step 7")
    fc.click(external_outage.get_current_address_radio(driver))
    Verify_GPS_Prompt(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 7")
    Handle_GPS_Prompt(driver, "Agree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 7")

    fc.bookmark(module, ts_id, test_case, "Step 8")
    fc.click(external_outage.get_reports_radio(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 8")

    fc.bookmark(module, ts_id, test_case, "Step 9")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 9")

def TC147(driver, ts_id):
    test_case = "TC147"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    time.sleep(3)
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    time.sleep(3)
    fc.click(external_outage.get_other_address_radio(driver))
    a = ActionChains(driver)
    hover = a.move_to_element_with_offset(external_outage.get_tooltip_other_address(driver), 0, 0)
    hover = a.drag_and_drop_by_offset(external_outage.get_tooltip_other_address(driver), .2, .2)
    #hover = a.move_to_element(external_outage.get_tooltip_other_address(driver), 1, 1)
    hover = a.move_by_offset(.1, .1)
    hover.click().perform()
    time.sleep(5)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC148(driver, ts_id, email, password):
    test_case = "TC148"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, meralco_online)
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Navigate_Outage(driver)
    default_zoom = Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Click_Address(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    time.sleep(3)
    fc.click(external_outage.get_other_address_radio(driver))
    a = ActionChains(driver)
    hover = a.move_to_element_with_offset(external_outage.get_tooltip_other_address(driver), 0, 0)
    hover = a.drag_and_drop_by_offset(external_outage.get_tooltip_other_address(driver), .2, .2)
    # hover = a.move_to_element(external_outage.get_tooltip_other_address(driver), 1, 1)
    hover = a.move_by_offset(.1, .1)
    hover.click().perform()
    time.sleep(5)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")

def TC149(driver, ts_id):
    test_case = "TC149"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    #click on outage pin // outage element not find.

def TC151(driver, ts_id, referencenumber, lastname):
    test_case = "TC151"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    Click_Outage_Report(driver)
    fc.accept_alert(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Inp_Reference_Number(driver, referencenumber)
    Inp_Last_Name(driver, lastname)
    Click_Submit(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

def TC152(driver, ts_id, email, password):
    test_case = "TC152"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Navigate_Outage(driver)
    default_zoom = Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    Select_Outage_Type(driver, "selectall")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    Close_Outage_Modal(driver)

    fc.bookmark(module, ts_id, test_case, "Step 5")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")
    Click_Select_Unplanned(driver, "unplanned")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")
    Close_Outage_Modal(driver)

    fc.bookmark(module, ts_id, test_case, "Step 7")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 7")
    Click_Select_Planned(driver, "planned")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 7")
    Close_Outage_Modal(driver)

def TC153(driver, ts_id):
    test_case = "TC153"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")



def TC154(driver, ts_id, email, password):
    test_case = "TC154"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Navigate_Outage(driver)
    default_zoom = Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    Select_Meralco_BusinessCenter(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    Close_BusinessOutage_Modal(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")

def TC155(driver, ts_id):
    test_case = "TC155"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    Select_Meralco_BusinessCenter(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    time.sleep(3)

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Close_BusinessOutage_Modal(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")


def TC156(driver, ts_id, email, password):
    test_case = "TC156"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, email, password)
    Verify_Successful_Login(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Navigate_Outage(driver)
    default_zoom = Check_Service_Located(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    Select_Weather_Information(driver, "temperature")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")


    fc.bookmark(module, ts_id, test_case, "Step 4")
    Close_Weather_Modal(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")


    fc.bookmark(module, ts_id, test_case, "Step 5")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")
    Select_Weather_Information(driver, "wind_speed")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")

def TC157(driver, ts_id):
    test_case = "TC157"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")



    fc.bookmark(module, ts_id, test_case, "Step 3")
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    Select_Weather_Information(driver, "temperature")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    Close_Weather_Modal(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")

    fc.bookmark(module, ts_id, test_case, "Step 5")
    Click_Outage_Map_Views(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")
    Select_Weather_Information(driver, "wind_speed")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")

def TC123(driver, ts_id, email, password):
    test_case = "TC123"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, internal_outage)
    fc.input_text(cxe_login.get_email(driver), email)
    fc.click(cxe_login.get_next(driver))
    fc.input_text(cxe_login.get_password(driver), password)
    fc.click(cxe_login.get_sign_in(driver))
    fc.click(cxe_login.get_sms(driver))
    time.sleep(25)
    fc.click(cxe_login.get_stay_sign_no(driver))
    internaloutage = InternalOutagePage()
   # internaloutage.get_switch_frame(driver)
    time.sleep(4)

    fc.modal_click(driver, internaloutage.get_menu(driver))
    fc.modal_click(driver, internaloutage.get_legends(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")


def TC122(driver, ts_id, email, password):
    test_case = "TC122"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, internal_outage)
    fc.input_text(cxe_login.get_email(driver), email)
    fc.click(cxe_login.get_next(driver))
    fc.input_text(cxe_login.get_password(driver), password)
    fc.click(cxe_login.get_sign_in(driver))
    fc.click(cxe_login.get_sms(driver))
    time.sleep(25)
    fc.click(cxe_login.get_stay_sign_no(driver))
    internaloutage = InternalOutagePage()
   # internaloutage.get_switch_frame(driver)
    time.sleep(4)

    fc.modal_click(driver, internaloutage.get_menu(driver))
    fc.modal_click(driver, internaloutage.get_legends(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")











