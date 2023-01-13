import time

from Pages.Page_AppleID_Login import AppleLoginPage
from Pages.Page_CXE_Apply_Home import CXEApplyHomePage
from Pages.Page_CXE_Apply_Individual import CXEApplyIndividual
from Pages.Page_CXE_Apply_Reg import CXEApplyRegPage
from Pages.Page_Enroll_Service import EnrollServicePage
from Pages.Page_Forgot_Password import ForgotPasswordPage
from Pages.Page_Google_Login import GoogleLoginPage
from Pages.Page_Home import HomePage
from Pages.Page_Login import LoginPage
from Pages.Page_My_Profile import MyProfilePage
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
def TC002a(driver, ts_id):
    test_case = "TC001a"
    login = LoginPage()
    google = GoogleLoginPage()

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")

    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.click(login.get_google_login(driver))
    fc.input_text(google.get_email(driver), SSO['google_email'])
    fc.click(google.get_next(driver))
    fc.input_text(google.get_password(driver), SSO['google_password'])
    fc.click(google.get_send(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")


def TC003a(driver, ts_id):
    test_case = "TC003a"
    login = LoginPage()
    apple = AppleLoginPage()

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")

    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")
    fc.click(login.get_apple_login(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.input_text(apple.get_apple_id(driver), SSO['appleId'])
    fc.click(apple.get_next_btn(driver))
    fc.input_text(apple.get_password(driver), SSO['apple_password'])
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")
    fc.click(apple.get_sign_in(driver))
    time.sleep(35)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2a")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    fc.input_text(apple.get_phone_number(driver), SAMO['mobileNumberIndividual'])
    fc.modal_click(driver, apple.get_terms_conditions(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")
    fc.modal_click(driver, apple.get_submit(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3a")

def TC005a(driver, ts_id):
    test_case = "TC005a"
    login = LoginPage()
    google = GoogleLoginPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")

    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(login.get_google_login(driver))
    fc.input_text(google.get_email(driver), SSO['google_email'])
    fc.click(google.get_next(driver))
    fc.input_text(google.get_password(driver), SSO['apple_password'])
    fc.click(google.get_send(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC006a(driver, ts_id):
    test_case = "TC006a"
    login = LoginPage()
    apple = AppleLoginPage()

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")

    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")
    fc.click(login.get_apple_login(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.input_text(apple.get_apple_id(driver), SSO['appleId'])
    fc.click(apple.get_next_btn(driver))
    fc.input_text(apple.get_password(driver), SSO['apple_password'])
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")
    fc.click(apple.get_sign_in(driver))
    time.sleep(35)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2a")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    fc.input_text(apple.get_mobile_number(driver), SAMO['mobileNumberIndividual'])
    fc.input_text(apple.get_can(driver), SAMO['CAN_appleid'])
    fc.input_text(apple.get_kwh(driver), SAMO['apple_kwh'])
    fc.input_text(apple.get_bill_date(driver), SAMO['apple_bill_date'])
    fc.modal_click(driver, apple.get_terms_conditions(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")
    fc.modal_click(driver, apple.get_submit(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3a")

def TC008a(driver, ts_id):
    test_case = "TC008a"
    login = LoginPage()
    google = GoogleLoginPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")

    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(login.get_google_login(driver))
    fc.input_text(google.get_email(driver), SSO['google_email'])
    fc.click(google.get_next(driver))
    fc.input_text(google.get_password(driver), SSO['google_password'])
    fc.click(google.get_send(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC009a(driver, ts_id):
    test_case = "TC006a"
    login = LoginPage()
    apple = AppleLoginPage()

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")

    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")
    fc.click(login.get_apple_login(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.input_text(apple.get_apple_id(driver), SSO['appleId'])
    fc.click(apple.get_next_btn(driver))
    fc.input_text(apple.get_password(driver), SSO['apple_password'])
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")
    fc.click(apple.get_sign_in(driver))
    time.sleep(35)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2a")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    fc.input_text(apple.get_mobile_number(driver), SAMO['mobileNumberIndividual'])
    fc.input_text(apple.get_can(driver), SAMO['CAN_appleid'])
    fc.input_text(apple.get_kwh(driver), SAMO['apple_kwh'])
    fc.input_text(apple.get_bill_date(driver), SAMO['apple_bill_date'])
    fc.modal_click(driver, apple.get_terms_conditions(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")
    fc.modal_click(driver, apple.get_submit(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3a")

def TC011a(driver, ts_id):
    test_case = "TC008a"
    login = LoginPage()
    google = GoogleLoginPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")

    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(login.get_google_login(driver))
    fc.input_text(google.get_email(driver), SSO['google_email'])
    fc.click(google.get_next(driver))
    fc.input_text(google.get_password(driver), SSO['google_password'])
    fc.click(google.get_send(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC012a(driver, ts_id):
    test_case = "TC012a"
    login = LoginPage()
    apple = AppleLoginPage()

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")
    fc.click(login.get_apple_login(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.input_text(apple.get_apple_id(driver), SSO['appleId'])
    fc.click(apple.get_next_btn(driver))
    fc.input_text(apple.get_password(driver), SSO['apple_password'])
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")
    fc.click(apple.get_sign_in(driver))
    time.sleep(25)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2a")

def TC039a(driver, ts_id):
    test_case = "TC039a"
    home = HomePage()
    enroll = EnrollServicePage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, Concern['username_single_service'], Concern['password'])
    fc.modal_click(driver, home.get_accounts(driver))
    fc.modal_click(driver, home.get_enroll_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    time.sleep(5)

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(enroll.get_can(driver), Concern['sacxe_single_can'])
    fc.input_text(enroll.get_sin(driver), Concern['sacxe_single_sin'])
    fc.input_text(enroll.get_total_kwh(driver), RFC['total_kwh'])
    fc.input_text(enroll.get_bill_date(driver), RFC['bill_date'])
    #fc.click(enroll.get_submit(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC042a(driver, ts_id):
    test_case = "TC039a"
    home = HomePage()
    profile = MyProfilePage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, Concern['username_single_service'], Concern['password'])
    fc.modal_click(driver, home.get_profile_name(driver))
    fc.modal_click(driver, home.get_my_profile(driver))
    time.sleep(5)
    fc.click(profile.get_landline_edit(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(profile.get_landline(driver), Outage['landline'])
    #fc.scroll_element(driver, profile.get_save_btn(driver))
    fc.click(profile.get_save_btn(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC045a(driver, ts_id):
    test_case = "TC039a"
    home = HomePage()
    profile = MyProfilePage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, Concern['username_single_service'], Concern['password'])
    fc.modal_click(driver, home.get_profile_name(driver))
    fc.modal_click(driver, home.get_my_profile(driver))
    time.sleep(5)
    fc.click(profile.get_landline_edit(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(profile.get_landline(driver), Outage['wrongLandline'])
    fc.click(profile.get_save_btn(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

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
    fc.click(report_outage.get_safety_select(driver))
    fc.click(report_outage.get_safety_pole_broken(driver))
    #fc.click(report_outage.get_pole_value(driver))
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
    fc.modal_click(driver, report_outage.get_yes_option(driver))
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

def TC062(driver, ts_id):
    test_case = "TC062"
    cxe_apply_home = CXEApplyHomePage()

    fc.new_tab(driver, cxe_apply)

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    fc.verify(cxe_apply_home.get_label_service_application(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.click(cxe_apply_home.get_individual(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    fc.click(cxe_apply_home.get_individual_start(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    fc.verify(cxe_apply_home.get_peccbm(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    fc.click(cxe_apply_home.get_popup_yes(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")

def TC063(driver, ts_id):
    test_case = "TC063"
    cxe_apply_home = CXEApplyHomePage()

    fc.new_tab(driver, cxe_apply)

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    fc.verify(cxe_apply_home.get_label_service_application(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.click(cxe_apply_home.get_individual(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    fc.click(cxe_apply_home.get_individual_start(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    fc.verify(cxe_apply_home.get_peccbm(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    fc.click(cxe_apply_home.get_popup_no(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")

def TC064(driver, ts_id):
    test_case = "TC064"
    cxe_apply_home = CXEApplyHomePage()
    cxe_business = CXEApplyBusiness()

    fc.new_tab(driver, cxe_apply)

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    fc.verify(cxe_apply_home.get_label_service_application(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.click(cxe_business.get_business(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    fc.click(cxe_business.get_business_start(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    fc.verify(cxe_apply_home.get_peccbm(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    fc.click(cxe_apply_home.get_popup_yes(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")

def TC065(driver, ts_id):
    test_case = "TC064"
    cxe_apply_home = CXEApplyHomePage()
    cxe_business = CXEApplyBusiness()

    fc.new_tab(driver, cxe_apply)

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    fc.verify(cxe_apply_home.get_label_service_application(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.click(cxe_business.get_business(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    fc.click(cxe_business.get_business_start(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    fc.verify(cxe_apply_home.get_peccbm(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    fc.click(cxe_apply_home.get_popup_no(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")

def TC066(driver, ts_id):
    test_case = "TC064"
    cxe_apply_home = CXEApplyHomePage()
    cxe_contractor = CXEApplyContractor()

    fc.new_tab(driver, cxe_apply)

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    fc.verify(cxe_apply_home.get_label_service_application(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.click(cxe_contractor.get_contractor(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    fc.click(cxe_contractor.get_contractor_start(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    fc.verify(cxe_contractor.get_applying_us(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    fc.click(cxe_contractor.get_peccbm(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")
    fc.click(cxe_contractor.get_submit_btn(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5b")

def TC067(driver, ts_id):
    test_case = "TC064"
    cxe_apply_home = CXEApplyHomePage()
    cxe_contractor = CXEApplyContractor()

    fc.new_tab(driver, cxe_apply)

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    fc.verify(cxe_apply_home.get_label_service_application(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.click(cxe_contractor.get_contractor(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    fc.click(cxe_contractor.get_contractor_start(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    fc.verify(cxe_contractor.get_applying_us(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    fc.click(cxe_contractor.get_submit_btn(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")

def TC068(driver, ts_id):
    test_case = "TC068"
    cxeHome = CXEHomePage()
    cxe_apply_home = CXEApplyHomePage()
    cxe_apply_individual = CXEApplyIndividual()
    yopmail_inbox = YopmailInboxPage()
    resetPass = ResetPasswordPage()
    home = HomePage()
    service = PageService()

    fc.new_tab(driver, cxe_apply)

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    fc.verify(cxe_apply_home.get_label_service_application(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.click(cxe_apply_home.get_individual(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    fc.click(cxe_apply_home.get_individual_start(driver))
    fc.click(cxe_apply_home.get_popup_no(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    fc.input_text(cxe_apply_individual.get_email_attr(driver), Registration['cxe_apply_email'])
    fc.input_text(cxe_apply_individual.get_firstname_attr(driver), Registration['single_service_first_name'])
    fc.input_text(cxe_apply_individual.get_lastname_attr(driver), Registration['single_service_last_name'])
    fc.input_text(cxe_apply_individual.get_mobile_num(driver), Registration['match_bills_mobile_num'])
    fc.click(cxe_apply_individual.get_terms_and_conditions(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")
    fc.click(cxe_apply_individual.get_register_btn(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    fc.new_tab(driver, yopmail)
    fc.input_text(yopmail_home.get_email(driver), Registration['cxe_apply_email'])
    fc.click(yopmail_home.get_check_inbox(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")
    fc.click(yopmail_inbox.get_here_link(driver))
    time.sleep(10)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5b")
    fc.input_text(resetPass.get_new_password(driver), SAMO['business_account_password'])
    fc.input_text(resetPass.get_confirm_password(driver), SAMO['business_account_password'])
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5c")
    fc.click(resetPass.get_set_password(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5d")
    Log_In_Meralco_Online(driver, Registration['cxe_apply_email'], Registration['business_account_password'])
    time.sleep(3)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5e")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    fc.scroll_element(driver, home.get_request_service(driver))
    fc.modal_click(driver, cxeHome.get_peccbm_no(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    fc.scroll_element(driver, service.get_click_next(driver))
    fc.click(service.get_click_next(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 8")
    fc.input_text(service.get_inp_serv_add(driver), Concern['service_address'])
    fc.select_dropdown_element(service.get_province(driver), Concern['province'])
    fc.select_dropdown_element(service.get_city(driver), Concern['city'])
    fc.select_dropdown_element(service.get_ownership(driver), Concern['home_ownership'])
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8")
    fc.click(service.get_clk_next_btn(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 9")
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 9")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 10")
    fc.click(service.get_next_service_btn(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 10")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 11")
    fc.click(service.get_terms_and_conditions_service_details(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 11")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 12")
    time.sleep(5)
    #captcha code
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 12")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 13")
    fc.click(service.get_submit_btn(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 13")


def TC070(driver, ts_id):
    test_case = "TC070"
    cxe_apply_home = CXEApplyHomePage()
    cxe_apply_inidividual = CXEModificationIndividual()

    fc.new_tab(driver, cxe_apply)

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    fc.verify(cxe_apply_home.get_label_service_application(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.click(cxe_apply_home.get_individual(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    fc.click(cxe_apply_home.get_individual_modify(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")
    fc.input_text(cxe_apply_inidividual.get_CAN(driver), SAMO['individual_account_can'])

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    fc.input_text(cxe_apply_inidividual.get_CAN(driver), SAMO['individual_account_can'])
    fc.click(cxe_apply_inidividual.get_change_service_detail(driver))
    fc.click(cxe_apply_inidividual.get_additional_load(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")
    fc.click(cxe_apply_inidividual.get_next1(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    fc.input_text(cxe_apply_inidividual.get_first_name(driver), SAMO['individual_account_first'])
    fc.input_text(cxe_apply_inidividual.get_last_name(driver), SAMO['individual_account_last'])
    fc.input_text(cxe_apply_inidividual.get_emailaddress(driver), SAMO['individual_account_email'])
    fc.input_text(cxe_apply_inidividual.get_mobile_number(driver), SAMO['individual_account_mobile'])
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")
    fc.click(cxe_apply_inidividual.get_next2(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5b")

def TC074(driver, ts_id):
    test_case = "TC074"
    home = HomePage()

    Log_In_Meralco_Online(driver, Concern['username_single_service'], Concern['normal_account_password'])

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    fc.modal_click(driver, home.get_faqs(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")