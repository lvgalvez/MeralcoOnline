import time

from Pages.Page_CXE_Apply_Home import CXEApplyHomePage
from Pages.Page_CXE_Apply_Reg import CXEApplyRegPage
from Pages.Page_Forgot_Password import ForgotPasswordPage
from Pages.Page_Home import HomePage
from Pages.Page_Login import LoginPage
from Pages.Page_Reset_Password import ResetPasswordPage
from Pages.Page_Yopmail_Home import YopmailHomePage
from Pages.Page_Yopmail_Inbox import YopmailInboxPage
from Pages.Page_Service import PageService
from Pages.Page_CXE_Apply_Business import CXEApplyBusiness
from Pages.Page_CXE_Apply_Business_Reg import CXEApplyBusinessRegPage
from Pages.Page_CXE_Apply_Contractor import CXEApplyContractor
from Pages.Page_CXE_Apply_Contractor_Reg import CXEApplyContractorRegPage
from Pages.Page_CXE_Modification_Business import CXEModificationBusiness
from Pages.Page_CXE_Modification_Individual import CXEModificationIndividual
from Pages.Page_CXE_Modification_Contractor import CXEModificationContractor
from Pages.Page_CXE_Account import CXEAccountPage
from Pages.Page_ES_Business import CXEEsBusiness
from Pages.Page_CXE_Terminate_Individual import CXETerminateIndividual
from Pages.Page_CXE_Terminate_Business import CXETerminateBusiness
from Pages.Page_CXE_Terminate_Contractor import CXETerminateContractor
from Pages.Page_CXE_Reactivate_Business import CXEReactivateBusiness
from Pages.Page_CXE_Reactivate_Contactor import CXEReactivateContractor
from Utilities.Config import *
from Utilities.Data import SSO
from Utilities.Functions import Functions
from Utilities.Utils import Utilities
from Test.Module_Functions.MO_Functions import *
from Pages.Page_Manage_Accounts import ManageAccountsPage
from Pages.Page_Yopmail_Home import YopmailHomePage
from Pages.Page_Home import HomePage
from Pages.Page_ContactUs import ContactUsPage
from Pages.Page_CXE_Home import CXEHomePage

log = Utilities().getlogger()
module = "SAMO"
serviceAppModule = "Release6"
fc = Functions()
yopmail_home = YopmailHomePage()


#Release 6

def TC051(driver, ts_id, companyname, tradename, companyemail, companylandline, firstname, lastname, emailaddress, mobilenumber, designation, serviceaddress):
    test_case = "TC051"
    function = Functions()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_home = CXEApplyHomePage()
    function.verify(cxe_apply_home.get_label_service_application(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1b")

    cxe_apply_business = CXEApplyBusiness()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    function.click(cxe_apply_business.get_business(driver))
    function.verify(cxe_apply_business.get_business_start(driver))
    function.verify(cxe_apply_business.get_business_modify(driver))
    function.verify(cxe_apply_business.get_business_reactivate(driver))
    function.verify(cxe_apply_business.get_business_stop(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    function.click(cxe_apply_business.get_clk_business_start(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    function.click(cxe_apply_business.get_popup_no(driver))
    cxe_apply_business_reg = CXEApplyBusinessRegPage()
    function.verify(cxe_apply_business_reg.get_lbl_start_service(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")


    function.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    function.input_text(cxe_apply_business_reg.get_company_name(driver), companyname)
    function.input_text(cxe_apply_business_reg.get_trade_name(driver), tradename)
    function.input_text(cxe_apply_business_reg.get_company_email(driver), companyemail)
    function.input_text(cxe_apply_business_reg.get_company_landline(driver), companylandline)
    function.input_text(cxe_apply_business_reg.get_first_name(driver), firstname)
    function.input_text(cxe_apply_business_reg.get_last_name(driver), lastname)
    function.input_text(cxe_apply_business_reg.get_email_address(driver), emailaddress)
    function.input_text(cxe_apply_business_reg.get_mobile(driver), mobilenumber)
    function.input_text(cxe_apply_business_reg.get_designation(driver), designation)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")
    function.click(cxe_apply_business_reg.get_next(driver))
    function.verify(cxe_apply_business_reg.get_lbl_new_address(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5b")


    function.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    function.input_text(cxe_apply_business_reg.get_inp_serv_add(driver), serviceaddress)
    function.click(cxe_apply_business_reg.get_clk_province(driver))
    function.click(cxe_apply_business_reg.get_province_value(driver))
    function.click(cxe_apply_business_reg.get_municipality(driver))
    function.click(cxe_apply_business_reg.get_clk_mciplity_val(driver))
    function.click(cxe_apply_business_reg.get_clk_radio(driver))
    function.click(cxe_apply_business_reg.get_next2(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")
    function.verify(cxe_apply_business_reg.get_value_added(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")


    function.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    function.click(cxe_apply_business_reg.get_btn_next3(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 8")
    function.click(cxe_apply_business_reg.get_click_term_condition(driver))
    time.sleep(20)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 9")
    function.verify(cxe_apply_business_reg.get_submit(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 9")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 10")
    function.click(cxe_apply_business_reg.get_submit(driver))
    function.click(cxe_apply_business_reg.get_confirmation(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 10")

    log.info(test_case + " Passed")

def TC054(driver, ts_id, firstname, lastname, middlename, businessname, emailaddress, mobilenumber, birthday, serviceaddress):
    test_case = "TC054"
    function = Functions()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_contractor = CXEApplyHomePage()
    function.verify(cxe_apply_contractor.get_label_service_application(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    cxe_apply_contractor = CXEApplyContractor()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    function.click(cxe_apply_contractor.get_contractor(driver))
    function.verify(cxe_apply_contractor.get_contractor_start(driver))
    function.verify(cxe_apply_contractor.get_contractor_modify(driver))
    function.verify(cxe_apply_contractor.get_contractor_reactivate(driver))
    function.verify(cxe_apply_contractor.get_contractor_stop(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    function.click(cxe_apply_contractor.get_clk_contractor_start(driver))
    function.click(cxe_apply_contractor.get_clk_contractor(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    cxe_apply_contractor_reg = CXEApplyContractorRegPage()
    function.verify(cxe_apply_contractor_reg.get_lbl_start_service(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    function.input_text(cxe_apply_contractor_reg.get_first_name(driver), firstname)
    function.input_text(cxe_apply_contractor_reg.get_last_name(driver), lastname)
    function.input_text(cxe_apply_contractor_reg.get_businessName(driver), businessname)
    function.input_text(cxe_apply_contractor_reg.get_email_address(driver), emailaddress)
    function.input_text(cxe_apply_contractor_reg.get_mobile(driver), mobilenumber)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")
    function.click(cxe_apply_contractor_reg.get_next(driver))
    function.verify(cxe_apply_contractor_reg.get_lbl_new_address(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4b")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    function.input_text(cxe_apply_contractor_reg.get_first_name_cus(driver), firstname)
    function.input_text(cxe_apply_contractor_reg.get_last_name_cus(driver), lastname)
    function.input_text(cxe_apply_contractor_reg.get_middle_name(driver), middlename)
    function.input_text(cxe_apply_contractor_reg.get_email_address_cus(driver), emailaddress)
    function.input_text(cxe_apply_contractor_reg.get_birthday(driver), birthday)
    function.input_text(cxe_apply_contractor_reg.get_mobile_cus(driver), mobilenumber)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")
    function.click(cxe_apply_contractor_reg.get_next2(driver))
    function.verify(cxe_apply_contractor_reg.get_lbl_new_address(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5b")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    function.input_text(cxe_apply_contractor_reg.get_inp_serv_add(driver), serviceaddress)
    function.click(cxe_apply_contractor_reg.get_clk_province(driver))
    function.click(cxe_apply_contractor_reg.get_province_value(driver))
    function.click(cxe_apply_contractor_reg.get_municipality(driver))
    function.click(cxe_apply_contractor_reg.get_clk_mciplity_val(driver))
    function.click(cxe_apply_contractor_reg.get_clk_ownership(driver))
    function.click(cxe_apply_contractor_reg.get_clk_ownership_value(driver))
    function.click(cxe_apply_contractor_reg.get_clk_radio(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")
    function.click(cxe_apply_contractor_reg.get_btn_next3(driver))
    function.verify(cxe_apply_contractor_reg.get_terms_condition(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6b")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    function.click(cxe_apply_contractor_reg.get_click_term_condition(driver))
    time.sleep(20)
    function.verify(cxe_apply_contractor_reg.get_submit(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 8")
    function.click(cxe_apply_contractor_reg.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8")
    function.click(cxe_apply_contractor_reg.get_confirmation(driver))

    log.info(test_case + " Passed")

def TC048(driver, ts_id, first_name, middle_name, last_name, mobile_number, landline, email):
    test_case = "TC048"

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Report_Outage(driver)
    fc.click(report_outage.get_no_power_myhouse(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.click(report_outage.get_address(driver))
    fc.click(report_outage.get_province_metro_manila(driver))
    fc.click(report_outage.get_city_pasig(driver))
    fc.click(report_outage.get_barangay_bagong_ilog(driver))
    fc.click(report_outage.get_subdivision_kawilihan(driver))
    fc.click(report_outage.get_street_kabutihan(driver))
    fc.input_text(report_outage.get_street_no(driver), "123")


    fc.click(report_outage.get_landmark_radio(driver))
    fc.click(report_outage.get_landmark_radio(driver))
    fc.input_text(report_outage.get_landmark_text(driver), "Sample Text")
    fc.input_text(report_outage.get_first_name(driver), first_name)
    fc.input_text(report_outage.get_middle_name(driver), middle_name)
    fc.input_text(report_outage.get_last_name(driver), last_name)
    fc.input_text(report_outage.get_mobile_number(driver), mobile_number)
    fc.input_text(report_outage.get_landline(driver), landline)
    fc.input_text(report_outage.get_email(driver), email)
    fc.click(report_outage.get_sms_checkbox(driver))
    fc.click(report_outage.get_email_checkbox(driver))

    fc.click(report_outage.get_terms_checkbox(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    fc.click(report_outage.get_submit(driver))
    time.sleep(6)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2b")
def TC048a(driver, ts_id, first_name, middle_name, last_name, mobile_number, landline, email):
    test_case = "TC048"

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Report_Outage(driver)
    fc.click(report_outage.get_no_power_street_radio(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.click(report_outage.get_address(driver))
    fc.click(report_outage.get_province_metro_manila(driver))
    fc.click(report_outage.get_city_pasig(driver))
    fc.click(report_outage.get_barangay_bagong_ilog(driver))
    fc.click(report_outage.get_subdivision_kawilihan(driver))
    fc.click(report_outage.get_street_kabutihan(driver))
    fc.input_text(report_outage.get_street_no(driver), "123")


    fc.click(report_outage.get_landmark_radio(driver))
    fc.click(report_outage.get_landmark_radio(driver))
    fc.input_text(report_outage.get_landmark_text(driver), "Sample Text")
    fc.input_text(report_outage.get_first_name(driver), first_name)
    fc.input_text(report_outage.get_middle_name(driver), middle_name)
    fc.input_text(report_outage.get_last_name(driver), last_name)
    fc.input_text(report_outage.get_mobile_number(driver), mobile_number)
    fc.input_text(report_outage.get_landline(driver), landline)
    fc.input_text(report_outage.get_email(driver), email)
    fc.click(report_outage.get_sms_checkbox(driver))
    fc.click(report_outage.get_email_checkbox(driver))

    fc.click(report_outage.get_terms_checkbox(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    fc.click(report_outage.get_submit(driver))
    time.sleep(6)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2b")

def TC048b(driver, ts_id, first_name, middle_name, last_name, mobile_number, landline, email):
    test_case = "TC048"

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Report_Outage(driver)
    fc.click(report_outage.get_unstable_power(driver))
    fc.click(report_outage.get_lights_flickering(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.click(report_outage.get_address(driver))
    fc.click(report_outage.get_province_metro_manila(driver))
    fc.click(report_outage.get_city_pasig(driver))
    fc.click(report_outage.get_barangay_bagong_ilog(driver))
    fc.click(report_outage.get_subdivision_kawilihan(driver))
    fc.click(report_outage.get_street_kabutihan(driver))
    fc.input_text(report_outage.get_street_no(driver), "123")


    fc.click(report_outage.get_landmark_radio(driver))
    fc.click(report_outage.get_landmark_radio(driver))
    fc.input_text(report_outage.get_landmark_text(driver), "Sample Text")
    fc.input_text(report_outage.get_first_name(driver), first_name)
    fc.input_text(report_outage.get_middle_name(driver), middle_name)
    fc.input_text(report_outage.get_last_name(driver), last_name)
    fc.input_text(report_outage.get_mobile_number(driver), mobile_number)
    fc.input_text(report_outage.get_landline(driver), landline)
    fc.input_text(report_outage.get_email(driver), email)
    fc.click(report_outage.get_sms_checkbox(driver))
    fc.click(report_outage.get_email_checkbox(driver))

    fc.click(report_outage.get_terms_checkbox(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    fc.click(report_outage.get_submit(driver))
    time.sleep(6)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2b")

def TC048c(driver, ts_id, first_name, middle_name, last_name, mobile_number, landline, email):
    test_case = "TC048"

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Report_Outage(driver)
    fc.click(report_outage.get_street_concern(driver))
    fc.click(report_outage.get_street_yes(driver))
    fc.click(report_outage.get_dropdown_value(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    #fc.click(report_outage.get_address(driver))
    fc.click(report_outage.get_province_metro_manila(driver))
    fc.click(report_outage.get_city_pasig(driver))
    fc.click(report_outage.get_barangay_bagong_ilog(driver))
    fc.click(report_outage.get_subdivision_kawilihan(driver))
    fc.click(report_outage.get_street_kabutihan(driver))
    fc.input_text(report_outage.get_street_no(driver), "123")


    fc.click(report_outage.get_landmark_radio(driver))
    fc.click(report_outage.get_landmark_radio(driver))
    fc.input_text(report_outage.get_landmark_text(driver), "Sample Text")
    fc.input_text(report_outage.get_first_name(driver), first_name)
    fc.input_text(report_outage.get_middle_name(driver), middle_name)
    fc.input_text(report_outage.get_last_name(driver), last_name)
    fc.input_text(report_outage.get_mobile_number(driver), mobile_number)
    fc.input_text(report_outage.get_landline(driver), landline)
    fc.input_text(report_outage.get_email(driver), email)
    fc.click(report_outage.get_sms_checkbox(driver))
    fc.click(report_outage.get_email_checkbox(driver))

    fc.click(report_outage.get_terms_checkbox(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    fc.click(report_outage.get_submit(driver))
    time.sleep(6)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2b")

def TC048d(driver, ts_id, first_name, middle_name, last_name, mobile_number, landline, email):
    test_case = "TC048"

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    fc.new_tab(driver, outage_external_guest)
    external_outage = ExternalOutagePage()
    external_outage.get_switch_frame(driver)
    Verify_GPS_Prompt(driver)
    Handle_GPS_Prompt(driver, "Disagree")
    Click_Report_Outage(driver)
    fc.click(report_outage.get_safety_concern(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.click(report_outage.get_address(driver))
    fc.click(report_outage.get_province_metro_manila(driver))
    fc.click(report_outage.get_city_pasig(driver))
    fc.click(report_outage.get_barangay_bagong_ilog(driver))
    fc.click(report_outage.get_subdivision_kawilihan(driver))
    fc.click(report_outage.get_street_kabutihan(driver))
    fc.input_text(report_outage.get_street_no(driver), "123")


    fc.click(report_outage.get_landmark_radio(driver))
    fc.click(report_outage.get_landmark_radio(driver))
    fc.input_text(report_outage.get_landmark_text(driver), "Sample Text")
    fc.input_text(report_outage.get_first_name(driver), first_name)
    fc.input_text(report_outage.get_middle_name(driver), middle_name)
    fc.input_text(report_outage.get_last_name(driver), last_name)
    fc.input_text(report_outage.get_mobile_number(driver), mobile_number)
    fc.input_text(report_outage.get_landline(driver), landline)
    fc.input_text(report_outage.get_email(driver), email)
    fc.click(report_outage.get_sms_checkbox(driver))
    fc.click(report_outage.get_email_checkbox(driver))

    fc.click(report_outage.get_terms_checkbox(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    fc.click(report_outage.get_submit(driver))
    time.sleep(6)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2b")