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

def TC147(driver, ts_id):
    test_case = "TC147"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    a = ActionChains(driver)
    a.move_to_element(external_outage.get_tooltip_other_address).perform()
    time.sleep(5)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC149(driver, ts_id):
    test_case = "TC149"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    #click on outage pin // outage element not find.

def TC149(driver, ts_id):
    test_case = "TC149"

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    #Click_Outage_Report(driver)



