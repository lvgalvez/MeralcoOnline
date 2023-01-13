import time

from selenium.webdriver import Keys

from Pages.Page_CXE_Apply_Home import CXEApplyHomePage
from Pages.Page_CXE_Apply_Individual import CXEApplyIndividual
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
serviceAppModule = "Release5"
fc = Functions()
yopmail_home = YopmailHomePage()


def TC002(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, password, birthday):
    test_case = "TC002"
    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_home = CXEApplyHomePage()
    function.verify(cxe_apply_home.get_label_service_application(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1")
    function.bookmark(module, ts_id, test_case, "Step 2")
    function.click(cxe_apply_home.get_individual(driver))
    function.verify(cxe_apply_home.get_individual_start(driver))
    function.verify(cxe_apply_home.get_individual_modify(driver))
    function.verify(cxe_apply_home.get_individual_reactivate(driver))
    function.verify(cxe_apply_home.get_individual_stop(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 2")

    function.bookmark(module, ts_id, test_case, "Step 3")
    function.click(cxe_apply_home.get_individual_start(driver))
    function.click(cxe_apply_home.get_popup_no(driver))
    cxe_apply_reg = CXEApplyRegPage()
    function.verify(cxe_apply_reg.get_new_account(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3")

    function.bookmark(module, ts_id, test_case, "Step 4")
    function.input_text(cxe_apply_reg.get_email(driver), email)
    function.input_text(cxe_apply_reg.get_first_name(driver), first_name)
    function.input_text(cxe_apply_reg.get_middle_name(driver), middle_name)
    function.input_text(cxe_apply_reg.get_last_name(driver), last_name)
    function.input_text(cxe_apply_reg.get_mobile_number(driver), mobile_number)
    #function.input_text(cxe_apply_reg.get_birthday(driver), birthday)
    function.click(cxe_apply_reg.get_terms_condition(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 4")
    function.click(cxe_apply_reg.get_register(driver))
    time.sleep(30)
    function.verify(cxe_apply_reg.get_confirmation(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 4b")

    function.bookmark(module, ts_id, test_case, "Step 5")
    function.new_tab(driver, yopmail)
    yopmail_home = YopmailHomePage()
    function.input_text(yopmail_home.get_email(driver), email)
    function.click(yopmail_home.get_check_inbox(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 5")

    function.bookmark(module, ts_id, test_case, "Step 6")
    yopmail_inbox = YopmailInboxPage()
    yopmail_inbox.get_here_link(driver)
    reset_password = ResetPasswordPage()
    function.screen_capture(driver, module, ts_id, test_case, "Step 6")

    function.bookmark(module, ts_id, test_case, "Step 7")
    function.input_text(reset_password.get_new_password(driver), password)
    function.input_text(reset_password.get_confirm_password(driver), password)
    function.screen_capture(driver, module, ts_id, test_case, "Step 7")
    function.click(reset_password.get_set_password(driver))
    login = LoginPage()
    function.verify(login.get_new_password_confirmation(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 7b")
    function.input_text(login.get_email(driver), email)
    function.input_text(login.get_password(driver), password)
    function.screen_capture(driver, module, ts_id, test_case, "Step 7c")
    function.click(login.get_log_in(driver))
    home = HomePage()
    function.verify(home.get_hello_message(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 7d")
    log.info(test_case + " Passed")

def TC001(driver, ts_id, email, password, serviceaddress, birthday):
    test_case = "TC001"
    log.info("==========Log in==========")

    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    login = LoginPage()
    function.input_text(login.get_email(driver), email)
    function.input_text(login.get_password(driver), password)
    function.click(login.get_log_in(driver))
    home = HomePage()
    function.verify(home.get_hello_message(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1")

    function.bookmark(module, ts_id, test_case, "Step 2")
    #function.click(home.get_popupNO(driver))
    function.click(home.get_request_tile(driver))
    function.verify(home.get_label_start_serv(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 2")

    pageservice = PageService()

    function.bookmark(module, ts_id, test_case, "Step 3")
    function.input_text(pageservice.get_birthday(driver), birthday)
    function.screen_capture(driver, module, ts_id, test_case, "Step 3")
    function.click(pageservice.get_click_next(driver))
    function.verify(pageservice.get_label_serv_add(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3b")

    function.bookmark(module, ts_id, test_case, "Step 4")
    function.input_text(pageservice.get_inp_serv_add(driver), serviceaddress)
    function.click(pageservice.get_clk_province(driver))
    function.click(pageservice.get_province_value(driver))
    function.click(pageservice.get_municipality(driver))
    function.click(pageservice.get_clk_mciplity_val(driver))
    function.click(pageservice.get_clk_ownership(driver))
    function.click(pageservice.get_clk_ownership_value(driver))
    function.click(pageservice.get_clk_ownership(driver))
    function.click(pageservice.get_clk_radio(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 4")
    function.click(pageservice.get_next(driver))
    function.verify(pageservice.get_value_added(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 4b")

    function.bookmark(module, ts_id, test_case, "Step 5")
    function.click(pageservice.get_automatic_payment(driver))
    #function.click(pageservice.get_attach_docu(driver)) #upload file to be follow
    function.screen_capture(driver, module, ts_id, test_case, "Step 5")
    function.click(pageservice.get_clk_next_2(driver))
    function.verify(pageservice.get_term_condition(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 5b")

    function.bookmark(module, ts_id, test_case, "Step 6")
    function.click(pageservice.get_click_term_condition(driver))
    #function.click(pageservice.get_iam_not_robot(driver)) #for manual only
    time.sleep(20)
    function.screen_capture(driver, module, ts_id, test_case, "Step 6")

    function.bookmark(module, ts_id, test_case, "Step 7")
    function.click(pageservice.get_submit(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 7")
    #to be continued
    log.info(test_case + " Passed")

def TC001a(driver, ts_id, email, password, serviceaddress):
    test_case = "TC001"
    log.info("==========Log in==========")

    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    login = LoginPage()
    function.input_text(login.get_email(driver), email)
    function.input_text(login.get_password(driver), password)
    function.click(login.get_log_in(driver))
    home = HomePage()
    function.verify(home.get_hello_message(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1")

    function.bookmark(module, ts_id, test_case, "Step 2")
    #function.click(home.get_popupNO(driver))
    function.click(home.get_request_tile(driver))
    function.verify(home.get_label_start_serv(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 2")

    pageservice = PageService()

    function.bookmark(module, ts_id, test_case, "Step 3")
   # function.input_text(pageservice.get_birthday(driver), birthday)
    function.screen_capture(driver, module, ts_id, test_case, "Step 3")
    function.click(pageservice.get_click_next(driver))
    function.verify(pageservice.get_label_serv_add(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3b")

    function.bookmark(module, ts_id, test_case, "Step 4")
    function.input_text(pageservice.get_inp_serv_add(driver), serviceaddress)
    function.click(pageservice.get_clk_province(driver))
    function.click(pageservice.get_province_value(driver))
    function.click(pageservice.get_municipality(driver))
    function.click(pageservice.get_clk_mciplity_val(driver))
    function.click(pageservice.get_clk_ownership(driver))
    function.click(pageservice.get_clk_ownership_value(driver))
    function.click(pageservice.get_clk_ownership(driver))
    function.click(pageservice.get_clk_radio(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 4")
    function.click(pageservice.get_next(driver))
    function.verify(pageservice.get_value_added(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 4b")

    function.bookmark(module, ts_id, test_case, "Step 5")
    function.click(pageservice.get_automatic_payment(driver))
    #function.click(pageservice.get_attach_docu(driver)) #upload file to be follow
    function.screen_capture(driver, module, ts_id, test_case, "Step 5")
    function.click(pageservice.get_clk_next_2(driver))
    function.verify(pageservice.get_term_condition(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 5b")

    function.bookmark(module, ts_id, test_case, "Step 6")
    function.click(pageservice.get_click_term_condition(driver))
    #function.click(pageservice.get_iam_not_robot(driver)) #for manual only
    time.sleep(20)
    function.screen_capture(driver, module, ts_id, test_case, "Step 6")

    function.bookmark(module, ts_id, test_case, "Step 7")
    function.click(pageservice.get_submit(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 7")
    #to be continued
    log.info(test_case + " Passed")

def TC003(driver, ts_id, companyname, tradename, companyemail, companylandline, firstname, lastname, emailaddress, mobilenumber, designation, serviceaddress):
    test_case = "TC003"
    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_home = CXEApplyHomePage()
    function.verify(cxe_apply_home.get_label_service_application(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1b")

    cxe_apply_business = CXEApplyBusiness()
    function.bookmark(module, ts_id, test_case, "Step 2")
    function.click(cxe_apply_business.get_business(driver))
    function.verify(cxe_apply_business.get_business_start(driver))
    function.verify(cxe_apply_business.get_business_modify(driver))
    function.verify(cxe_apply_business.get_business_reactivate(driver))
    function.verify(cxe_apply_business.get_business_stop(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 2")

    function.bookmark(module, ts_id, test_case, "Step 3")
    function.click(cxe_apply_business.get_clk_business_start(driver))
    function.click(cxe_apply_business.get_popup_no(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3")

    cxe_apply_business_reg = CXEApplyBusinessRegPage()
    function.verify(cxe_apply_business_reg.get_lbl_start_service(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3")

    function.bookmark(module, ts_id, test_case, "Step 4")
    function.input_text(cxe_apply_business_reg.get_company_name(driver), companyname)
    function.input_text(cxe_apply_business_reg.get_trade_name(driver), tradename)
    function.input_text(cxe_apply_business_reg.get_company_email(driver), companyemail)
    function.input_text(cxe_apply_business_reg.get_company_landline(driver), companylandline)
    function.input_text(cxe_apply_business_reg.get_first_name(driver), firstname)
    function.input_text(cxe_apply_business_reg.get_last_name(driver), lastname)
    function.input_text(cxe_apply_business_reg.get_email_address(driver), emailaddress)
    function.input_text(cxe_apply_business_reg.get_mobile(driver), mobilenumber)
    function.input_text(cxe_apply_business_reg.get_designation(driver), designation)
    function.screen_capture(driver, module, ts_id, test_case, "Step 4")
    function.click(cxe_apply_business_reg.get_next(driver))
    function.verify(cxe_apply_business_reg.get_lbl_new_address(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 4b")


    function.bookmark(module, ts_id, test_case, "Step 5")
    function.input_text(cxe_apply_business_reg.get_inp_serv_add(driver), serviceaddress)
    function.click(cxe_apply_business_reg.get_clk_province(driver))
    function.click(cxe_apply_business_reg.get_province_value(driver))
    function.click(cxe_apply_business_reg.get_municipality(driver))
    function.click(cxe_apply_business_reg.get_clk_mciplity_val(driver))
    function.click(cxe_apply_business_reg.get_clk_radio(driver))
    function.click(cxe_apply_business_reg.get_next2(driver))
    function.verify(cxe_apply_business_reg.get_value_added(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 5")


    function.bookmark(module, ts_id, test_case, "Step 6")
    function.click(cxe_apply_business_reg.get_btn_next3(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 6")

    function.bookmark(module, ts_id, test_case, "Step 7")
    function.click(cxe_apply_business_reg.get_click_term_condition(driver))
    time.sleep(20)
    function.verify(cxe_apply_business_reg.get_submit(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 7")

    function.bookmark(module, ts_id, test_case, "Step 8")
    function.click(cxe_apply_business_reg.get_submit(driver))
    function.click(cxe_apply_business_reg.get_confirmation(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 8")

    log.info(test_case + " Passed")
def TC004(driver, ts_id, firstname, lastname, middlename, businessname, emailaddress, mobilenumber, birthday, serviceaddress):
    test_case = "TC004"
    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_contractor = CXEApplyHomePage()
    function.verify(cxe_apply_contractor.get_label_service_application(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1")

    cxe_apply_contractor = CXEApplyContractor()
    function.bookmark(module, ts_id, test_case, "Step 2")
    function.click(cxe_apply_contractor.get_contractor(driver))
    function.verify(cxe_apply_contractor.get_contractor_start(driver))
    function.verify(cxe_apply_contractor.get_contractor_modify(driver))
    function.verify(cxe_apply_contractor.get_contractor_reactivate(driver))
    function.verify(cxe_apply_contractor.get_contractor_stop(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 2")

    function.bookmark(module, ts_id, test_case, "Step 3")
    function.click(cxe_apply_contractor.get_clk_contractor_start(driver))
    function.click(cxe_apply_contractor.get_clk_contractor(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3")

    cxe_apply_contractor_reg = CXEApplyContractorRegPage()
    function.verify(cxe_apply_contractor_reg.get_lbl_start_service(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3")

    function.bookmark(module, ts_id, test_case, "Step 4")
    function.input_text(cxe_apply_contractor_reg.get_first_name(driver), firstname)
    function.input_text(cxe_apply_contractor_reg.get_last_name(driver), lastname)
    function.input_text(cxe_apply_contractor_reg.get_businessName(driver), businessname)
    function.input_text(cxe_apply_contractor_reg.get_email_address(driver), emailaddress)
    function.input_text(cxe_apply_contractor_reg.get_mobile(driver), mobilenumber)
    function.screen_capture(driver, module, ts_id, test_case, "Step 4")
    function.click(cxe_apply_contractor_reg.get_next(driver))
    function.verify(cxe_apply_contractor_reg.get_lbl_new_address(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 4b")

    function.bookmark(module, ts_id, test_case, "Step 5")
    function.input_text(cxe_apply_contractor_reg.get_first_name_cus(driver), firstname)
    function.input_text(cxe_apply_contractor_reg.get_last_name_cus(driver), lastname)
    function.input_text(cxe_apply_contractor_reg.get_middle_name(driver), middlename)
    function.input_text(cxe_apply_contractor_reg.get_email_address_cus(driver), emailaddress)
    function.input_text(cxe_apply_contractor_reg.get_birthday(driver), birthday)
    function.input_text(cxe_apply_contractor_reg.get_mobile_cus(driver), mobilenumber)
    function.screen_capture(driver, module, ts_id, test_case, "Step 5")
    function.click(cxe_apply_contractor_reg.get_next2(driver))
    function.verify(cxe_apply_contractor_reg.get_lbl_new_address(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 5b")

    function.bookmark(module, ts_id, test_case, "Step 6")
    function.input_text(cxe_apply_contractor_reg.get_inp_serv_add(driver), serviceaddress)
    function.click(cxe_apply_contractor_reg.get_clk_province(driver))
    function.click(cxe_apply_contractor_reg.get_province_value(driver))
    function.click(cxe_apply_contractor_reg.get_municipality(driver))
    function.click(cxe_apply_contractor_reg.get_clk_mciplity_val(driver))
    function.click(cxe_apply_contractor_reg.get_clk_ownership(driver))
    function.click(cxe_apply_contractor_reg.get_clk_ownership_value(driver))
    function.click(cxe_apply_contractor_reg.get_clk_radio(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 6")
    function.click(cxe_apply_contractor_reg.get_btn_next3(driver))
    function.verify(cxe_apply_contractor_reg.get_terms_condition(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 6b")

    function.bookmark(module, ts_id, test_case, "Step 7")
    function.click(cxe_apply_contractor_reg.get_click_term_condition(driver))
    time.sleep(20)
    function.verify(cxe_apply_contractor_reg.get_submit(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 7")

    function.bookmark(module, ts_id, test_case, "Step 8")
    function.click(cxe_apply_contractor_reg.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, module, ts_id, test_case, "Step 8")
    function.click(cxe_apply_contractor_reg.get_confirmation(driver))

    log.info(test_case + " Passed")

def TC006(driver, ts_id, email, password, serviceaddress):
    test_case = "TC006"
    log.info("==========Log in==========")

    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    login = LoginPage()
    function.input_text(login.get_email(driver), email)
    function.input_text(login.get_password(driver), password)
    function.click(login.get_log_in(driver))
    home = HomePage()
    function.verify(home.get_hello_message(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1")

    function.bookmark(module, ts_id, test_case, "Step 2")
    function.click(home.get_account(driver))

    cxe_account = CXEAccountPage()
    function.verify(cxe_account.get_account_page(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 2")

    function.bookmark(module, ts_id, test_case, "Step 3")
    function.click(cxe_account.get_submit_account(driver))
    function.click(cxe_account.get_clk_account(driver))
    function.click(cxe_account.get_service_details(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3")

    function.bookmark(module, ts_id, test_case, "Step 4")
    function.click(cxe_account.get_change_name(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 4")
    function.click(cxe_account.get_change_contract_name(driver))
    function.click(cxe_account.get_click_next(driver))
    function.verify(cxe_account.get_value_added(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 4b")

    function.bookmark(module, ts_id, test_case, "Step 5")
    function.click(cxe_account.get_click_amc(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 5")
    function.click(cxe_account.get_click_next2(driver))
    function.verify(cxe_account.get_terms_condition(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 5b")

    function.bookmark(module, ts_id, test_case, "Step 6")
    function.click(cxe_account.get_click_term_condition(driver))
    time.sleep(20)
    function.verify(cxe_account.get_submit(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 6")

    function.bookmark(module, ts_id, test_case, "Step 7")
    function.click(cxe_account.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, module, ts_id, test_case, "Step 7")
   # function.click(cxe_account.get_confirmation(driver))

    log.info(test_case + " Passed")

def TC007(driver, ts_id):
    test_case = "TC007"
    home = HomePage()
    account = ManageAccountsPage()
    service = PageService()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, SAMO['normal_account_email'], SAMO['normal_account_password'])
    time.sleep(10)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.modal_click(driver, home.get_accounts(driver))
    fc.modal_click(driver, home.get_manage_accounts(driver))
    time.sleep(5)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    time.sleep(5)
    fc.click(account.get_submit(driver))
    time.sleep(5)
    fc.click(account.get_account(driver))
    fc.scroll_element(driver, account.get_change_contract(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(account.get_change_contract(driver))
    time.sleep(5)

    fc.bookmark(module, ts_id, test_case, "Step 4")
    fc.click(service.get_change_contract_radio_btn(driver))
    fc.scroll_element(driver, service.get_next_button(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")
    fc.click(service.get_next_button(driver))
    time.sleep(5)

    fc.bookmark(module, ts_id, test_case, "Step 5")
    fc.scroll_element(driver, service.get_next_modify_button(driver))
    time.sleep(5)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")
    fc.click(service.get_next_modify_button(driver))

    fc.bookmark(module, ts_id, test_case, "Step 6")
    fc.scroll_element(driver, service.get_submit_modify_contract(driver))
    time.sleep(3)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 6")
    fc.click(account.get_terms(driver))
    time.sleep(10)
    fc.click(service.get_submit_modify_contract(driver))

    fc.bookmark(module, ts_id, test_case, "Step 7")
    time.sleep(2)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 7")

def TC008(driver, ts_id):
    test_case = "TC008"
    home = HomePage()
    account = ManageAccountsPage()
    service = PageService()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, SAMO['normal_account_email'], SAMO['normal_account_password'])
    time.sleep(10)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.modal_click(driver, home.get_accounts(driver))
    fc.modal_click(driver, home.get_manage_accounts(driver))
    time.sleep(5)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    time.sleep(5)
    fc.click(account.get_submit(driver))
    time.sleep(5)
    fc.click(account.get_account(driver))
    fc.scroll_element(driver, account.get_change_contract(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(account.get_change_contract(driver))
    time.sleep(5)

    fc.bookmark(module, ts_id, test_case, "Step 4")
    fc.click(account.get_transfer(driver))
    fc.scroll_element(driver, service.get_next_button(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")
    fc.click(service.get_next_button(driver))
    time.sleep(5)

    fc.bookmark(module, ts_id, test_case, "Step 5")
    fc.scroll_element(driver, service.get_next_modify_button(driver))
    time.sleep(5)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")
    fc.click(service.get_next_modify_button(driver))

    fc.bookmark(module, ts_id, test_case, "Step 6")
    fc.scroll_element(driver, service.get_submit_modify_contract(driver))
    time.sleep(3)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 6")
    fc.click(account.get_terms(driver))
    time.sleep(10)
    fc.click(service.get_submit_modify_contract(driver))

    fc.bookmark(module, ts_id, test_case, "Step 7")
    time.sleep(2)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 7")

def TC009(driver, ts_id, email, password):
    test_case = "TC009"
    log.info("==========Log in==========")

    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    login = LoginPage()
    function.input_text(login.get_email(driver), email)
    function.input_text(login.get_password(driver), password)
    function.click(login.get_log_in(driver))
    home = HomePage()
    function.verify(home.get_hello_message(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1")

    cxeterminateSA = CXEAccountPage()
    function.bookmark(module, ts_id, test_case, "Step 2")
    function.click(cxeterminateSA.get_view_details(driver))
    function.verify(cxeterminateSA.get_account_page(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 2")

    function.bookmark(module, ts_id, test_case, "Step 3")
    function.click(cxeterminateSA.get_submit_term(driver))
    function.click(cxeterminateSA.get_account_clk(driver))
    function.click(cxeterminateSA.get_stop_service(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3")
    function.verify(cxeterminateSA.get_request_page(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3b")

    function.bookmark(module, ts_id, test_case, "Step 4")
    function.click(cxeterminateSA.get_submit_next(driver))
    time.sleep(3)
    function.screen_capture(driver, module, ts_id, test_case, "Step 4")

def TC011(driver, ts_id, can, companyname, landline, firstname, lastname, emailaddress, designation, mobilenumber):
    test_case = "TC011"
    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_home = CXEApplyHomePage()
    function.verify(cxe_apply_home.get_label_service_application(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1b")

    cxemodifybusiness = CXEModificationBusiness()
    function.bookmark(module, ts_id, test_case, "Step 2")
    function.click(cxemodifybusiness.get_business(driver))
    function.verify(cxemodifybusiness.get_start_service(driver))
    function.verify(cxemodifybusiness.get_modify_service(driver))
    function.verify(cxemodifybusiness.get_reactivate_service(driver))
    function.verify(cxemodifybusiness.get_stop_service(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 2")

    function.bookmark(module, ts_id, test_case, "Step 3")
    function.click(cxemodifybusiness.get_modify_service_clk(driver))
    function.verify(cxemodifybusiness.get_request(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3")

    function.bookmark(module, ts_id, test_case, "Step 4")
    function.verify(cxemodifybusiness.get_CAN(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 4")

    function.bookmark(module, ts_id, test_case, "Step 5")
    function.input_text(cxemodifybusiness.get_CAN(driver), can)
    function.screen_capture(driver, module, ts_id, test_case, "Step 5")

    function.bookmark(module, ts_id, test_case, "Step 6")
    function.click(cxemodifybusiness.get_change_contract_details(driver))
    function.click(cxemodifybusiness.get_change_contract_name(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 6")

    function.bookmark(module, ts_id, test_case, "Step 7")
    function.input_text(cxemodifybusiness.get_company_name(driver), companyname)
    function.input_text(cxemodifybusiness.get_landline(driver), landline)
    function.input_text(cxemodifybusiness.get_first_name(driver), firstname)
    function.input_text(cxemodifybusiness.get_last_name(driver), lastname)
    function.input_text(cxemodifybusiness.get_emailaddress(driver), emailaddress)
    function.input_text(cxemodifybusiness.get_mobile_number(driver), mobilenumber)
    function.input_text(cxemodifybusiness.get_designation(driver), designation)
    function.screen_capture(driver, module, ts_id, test_case, "Step 7")
    function.click(cxemodifybusiness.get_next1(driver))
    function.verify(cxemodifybusiness.get_contact_info(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 7b")

    function.bookmark(module, ts_id, test_case, "Step 8")
    function.input_text(cxemodifybusiness.get_first_name_mod(driver), firstname)
    function.input_text(cxemodifybusiness.get_last_name_mod(driver), lastname)
    function.input_text(cxemodifybusiness.get_emailddress_mod(driver), emailaddress)
    function.input_text(cxemodifybusiness.get_mobile_number_mod(driver), mobilenumber)
    function.screen_capture(driver, module, ts_id, test_case, "Step 8")
    function.click(cxemodifybusiness.get_next2(driver))
    function.verify(cxemodifybusiness.get_value_added(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 8b")

    function.bookmark(module, ts_id, test_case, "Step 9")
    function.click(cxemodifybusiness.get_yes(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 9")
    function.click(cxemodifybusiness.get_next3(driver))
    function.verify(cxemodifybusiness.get_terms_condition(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 9b")

    function.bookmark(module, ts_id, test_case, "Step 10")
    function.click(cxemodifybusiness.get_click_term_condition(driver))
    time.sleep(20)
    function.verify(cxemodifybusiness.get_submit(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 10")

    function.bookmark(module, ts_id, test_case, "Step 11")
    function.click(cxemodifybusiness.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, module, ts_id, test_case, "Step 11")
    function.verify(cxemodifybusiness.get_confirmation(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 11b")

    log.info(test_case + " Passed")


def TC012(driver, ts_id, can, companyname, landline, firstname, lastname, emailaddress, designation, mobilenumber):
    test_case = "TC012"
    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_home = CXEApplyHomePage()
    function.verify(cxe_apply_home.get_label_service_application(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1b")

    cxemodifybusiness = CXEModificationBusiness()
    function.bookmark(module, ts_id, test_case, "Step 2")
    function.click(cxemodifybusiness.get_business(driver))
    function.verify(cxemodifybusiness.get_start_service(driver))
    function.verify(cxemodifybusiness.get_modify_service(driver))
    function.verify(cxemodifybusiness.get_reactivate_service(driver))
    function.verify(cxemodifybusiness.get_stop_service(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 2")

    function.bookmark(module, ts_id, test_case, "Step 3")
    function.click(cxemodifybusiness.get_modify_service_clk(driver))
    function.verify(cxemodifybusiness.get_request(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3")

    function.bookmark(module, ts_id, test_case, "Step 4")
    function.verify(cxemodifybusiness.get_CAN(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 4")

    function.bookmark(module, ts_id, test_case, "Step 5")
    function.input_text(cxemodifybusiness.get_CAN(driver), can)
    function.screen_capture(driver, module, ts_id, test_case, "Step 5")

    function.bookmark(module, ts_id, test_case, "Step 6")
    function.click(cxemodifybusiness.get_change_contract_details(driver))
    function.click(cxemodifybusiness.get_change_contract_name(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 6")

    function.bookmark(module, ts_id, test_case, "Step 7")
    function.input_text(cxemodifybusiness.get_company_name(driver), companyname)
    function.input_text(cxemodifybusiness.get_landline(driver), landline)
    function.input_text(cxemodifybusiness.get_first_name(driver), firstname)
    function.input_text(cxemodifybusiness.get_last_name(driver), lastname)
    function.input_text(cxemodifybusiness.get_emailaddress(driver), emailaddress)
    function.input_text(cxemodifybusiness.get_mobile_number(driver), mobilenumber)
    function.input_text(cxemodifybusiness.get_designation(driver), designation)
    function.screen_capture(driver, module, ts_id, test_case, "Step 7")
    function.click(cxemodifybusiness.get_next1(driver))
    function.verify(cxemodifybusiness.get_contact_info(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 7b")

    function.bookmark(module, ts_id, test_case, "Step 8")
    function.input_text(cxemodifybusiness.get_first_name_mod(driver), firstname)
    function.input_text(cxemodifybusiness.get_last_name_mod(driver), lastname)
    function.input_text(cxemodifybusiness.get_emailddress_mod(driver), emailaddress)
    function.input_text(cxemodifybusiness.get_mobile_number_mod(driver), mobilenumber)
    function.screen_capture(driver, module, ts_id, test_case, "Step 8")
    function.click(cxemodifybusiness.get_next2(driver))
    function.verify(cxemodifybusiness.get_value_added(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 8b")

    function.bookmark(module, ts_id, test_case, "Step 9")
    function.click(cxemodifybusiness.get_yes(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 9")
    function.click(cxemodifybusiness.get_next3(driver))
    function.verify(cxemodifybusiness.get_terms_condition(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 9b")

    function.bookmark(module, ts_id, test_case, "Step 10")
    function.click(cxemodifybusiness.get_click_term_condition(driver))
    time.sleep(10)
    function.verify(cxemodifybusiness.get_submit(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 10")

    function.bookmark(module, ts_id, test_case, "Step 11")
    function.click(cxemodifybusiness.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, module, ts_id, test_case, "Step 11")
    function.verify(cxemodifybusiness.get_confirmation(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 11b")

    log.info(test_case + " Passed")

def TC012a(driver, ts_id, email):
    test_case = "TC012"
    home = HomePage()
    cxeHome = CXEHomePage()
    service = PageService()

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, email, SAMO['business_account_password'])
    time.sleep(10)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.scroll_element(driver, home.get_request_service(driver))
    fc.click(home.get_request_service(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2b")
    fc.modal_click(driver, cxeHome.get_peccbm_no(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2c")

    time.sleep(5)
    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    fc.scroll_element(driver, service.get_click_next(driver))
    time.sleep(3)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")
    fc.click(service.get_click_next(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    fc.input_text(service.get_inp_serv_add(driver), Concern['service_address'])
    fc.select_dropdown_element(service.get_province(driver), Concern['province'])
    fc.select_dropdown_element(service.get_city(driver), Concern['city'])
    fc.select_dropdown_element(service.get_ownership(driver), Concern['home_ownership'])
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")
    fc.click(service.get_clk_next_btn(driver))
    time.sleep(5)

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")
    #fc.click(cxemodifybusiness.get_next2(driver))
    fc.click(service.get_next_service_btn(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    time.sleep(20)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")

    fc.click(service.get_submit_btn(driver))
    time.sleep(5)

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    fc.scroll_element(driver, home.get_search(driver))
    time.sleep(2)
    fc.scroll_element(driver, service.get_ok_btn(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7")
    fc.click(service.get_ok_btn(driver))

def TC013(driver, ts_id, can, companyname, landline, firstname, lastname, emailaddress, designation, mobilenumber):
    test_case = "TC013"
    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_home = CXEApplyHomePage()
    function.verify(cxe_apply_home.get_label_service_application(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1b")

    cxemodifycontractor = CXEModificationContractor()
    function.bookmark(module, ts_id, test_case, "Step 2")
    function.click(cxemodifycontractor.get_contractor(driver))
    function.verify(cxemodifycontractor.get_start_service_cn(driver))
    function.verify(cxemodifycontractor.get_modify_service_cn(driver))
    function.verify(cxemodifycontractor.get_reactivate_service_cn(driver))
    function.verify(cxemodifycontractor.get_stop_service_cn(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 2")

    function.bookmark(module, ts_id, test_case, "Step 3")
    function.click(cxemodifycontractor.get_modify_service_clk(driver))
    function.verify(cxemodifycontractor.get_request(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3")

    function.bookmark(module, ts_id, test_case, "Step 4")
    function.verify(cxemodifycontractor.get_CAN(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 4")

    function.bookmark(module, ts_id, test_case, "Step 5")
    function.input_text(cxemodifycontractor.get_CAN(driver), can)
    function.screen_capture(driver, module, ts_id, test_case, "Step 5")

    function.bookmark(module, ts_id, test_case, "Step 6")
    function.click(cxemodifycontractor.get_change_service_details(driver))
    function.click(cxemodifycontractor.get_change_downgrade_electrical(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 6")
    function.click(cxemodifycontractor.get_click_nxtcont(driver))


    function.bookmark(module, ts_id, test_case, "Step 7")
    function.input_text(cxemodifycontractor.get_first_name(driver), firstname)
    function.input_text(cxemodifycontractor.get_last_name(driver), lastname)
    function.input_text(cxemodifycontractor.get_business(driver), companyname)
    function.input_text(cxemodifycontractor.get_emailaddress(driver), emailaddress)
    function.input_text(cxemodifycontractor.get_mobile_number(driver), mobilenumber)
    #function.input_text(cxemodifycontractor.get_designation(driver), designation)
    function.screen_capture(driver, module, ts_id, test_case, "Step 7")
    function.click(cxemodifycontractor.get_next1(driver))
    #function.verify(cxemodifycontractor.get_contact_info(driver))
    function.verify(cxemodifycontractor.get_terms_condition(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 7b")


    function.bookmark(module, ts_id, test_case, "Step 8")
    function.click(cxemodifycontractor.get_click_term_condition(driver))
    time.sleep(10)
    function.verify(cxemodifycontractor.get_submit(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 8")

    function.bookmark(module, ts_id, test_case, "Step 9")
    function.click(cxemodifycontractor.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, module, ts_id, test_case, "Step 9")
    function.verify(cxemodifycontractor.get_confirmation(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 9b")

    log.info(test_case + " Passed")

def TC013a(driver, ts_id):
    test_case = "TC013"
    home = HomePage()

    fc.modal_click(driver, home.get_overview(driver))
    time.sleep(5)

    fc.scroll_element(driver, home.get_activity_tracker(driver))
    fc.click(home.get_activity_tracker(driver))
    time.sleep(2)
    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

def TC014a(driver, ts_id, email):
    test_case = "TC014"
    contactUsPage = ContactUsPage()

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    fc.new_tab(driver, yopmail)
    fc.input_text(yopmail_home.get_email(driver), email)
    fc.click(yopmail_home.get_check_inbox(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")
    #insert Assert for validation

def TC014(driver, ts_id, firstname, lastname, emailaddress, mobilenumber, can):
    test_case = "TC014"
    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_home = CXEApplyHomePage()
    function.verify(cxe_apply_home.get_label_service_application(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1b")

    cxetermindividual = CXETerminateIndividual()
    function.bookmark(module, ts_id, test_case, "Step 2")
    function.click(cxetermindividual.get_individual(driver))
    function.verify(cxetermindividual.get_start_service(driver))
    function.verify(cxetermindividual.get_modify_service(driver))
    function.verify(cxetermindividual.get_reactivate_service(driver))
    function.verify(cxetermindividual.get_stop_service(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 2")

    function.bookmark(module, ts_id, test_case, "Step 3")
    function.click(cxetermindividual.get_stop_service_clk(driver))
    function.verify(cxetermindividual.get_stop_lbl(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3")

    function.bookmark(module, ts_id, test_case, "Step 4")
    function.verify(cxetermindividual.get_CAN(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 4")

    function.bookmark(module, ts_id, test_case, "Step 5")
    function.input_text(cxetermindividual.get_CAN(driver), can)
    function.screen_capture(driver, module, ts_id, test_case, "Step 5")

    function.bookmark(module, ts_id, test_case, "Step 6")
    function.input_text(cxetermindividual.get_firstname(driver), firstname)
    function.input_text(cxetermindividual.get_lastname(driver), lastname)
    function.input_text(cxetermindividual.get_emailaddress(driver), emailaddress)
    function.input_text(cxetermindividual.get_mobile_number(driver), mobilenumber)
    function.screen_capture(driver, module, ts_id, test_case, "Step 6")
    function.click(cxetermindividual.get_next1(driver))
    function.verify(cxetermindividual.get_terms_cond(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 6b")

    function.bookmark(module, ts_id, test_case, "Step 7")
    function.click(cxetermindividual.get_yes(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 7")
    #function.click(cxetermindividual.get_next3(driver))
    function.verify(cxetermindividual.get_terms_cond(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 7b")

    function.bookmark(module, ts_id, test_case, "Step 10")
    function.click(cxetermindividual.get_terms_cond(driver))
    time.sleep(15)
    function.verify(cxetermindividual.get_submit(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 10")

    function.bookmark(module, ts_id, test_case, "Step 11")
    function.click(cxetermindividual.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, module, ts_id, test_case, "Step 11")
    #function.verify(cxetermindividual.get_confirmation(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 11b")

    log.info(test_case + " Passed")


def TC015(driver, ts_id, firstname, lastname, emailaddress, mobilenumber, can):
    test_case = "TC015"
    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_home = CXEApplyHomePage()
    function.verify(cxe_apply_home.get_label_service_application(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1b")

    cxetermindividual = CXETerminateBusiness()
    function.bookmark(module, ts_id, test_case, "Step 2")
    function.click(cxetermindividual.get_business(driver))
    function.verify(cxetermindividual.get_start_service(driver))
    function.verify(cxetermindividual.get_modify_service(driver))
    function.verify(cxetermindividual.get_reactivate_service(driver))
    function.verify(cxetermindividual.get_stop_service(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 2")

    function.bookmark(module, ts_id, test_case, "Step 3")
    function.click(cxetermindividual.get_stop_service_clk(driver))
    function.verify(cxetermindividual.get_stop_lbl(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3")

    function.bookmark(module, ts_id, test_case, "Step 4")
    function.verify(cxetermindividual.get_CAN(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 4")

    function.bookmark(module, ts_id, test_case, "Step 5")
    function.input_text(cxetermindividual.get_CAN(driver), can)
    function.screen_capture(driver, module, ts_id, test_case, "Step 5")

    function.bookmark(module, ts_id, test_case, "Step 6")
    function.input_text(cxetermindividual.get_firstname(driver), firstname)
    function.input_text(cxetermindividual.get_lastname(driver), lastname)
    function.input_text(cxetermindividual.get_emailaddress(driver), emailaddress)
    function.input_text(cxetermindividual.get_mobile_number(driver), mobilenumber)
    function.screen_capture(driver, module, ts_id, test_case, "Step 6")
    function.click(cxetermindividual.get_next1(driver))
    function.verify(cxetermindividual.get_terms_cond(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 6b")

    function.bookmark(module, ts_id, test_case, "Step 7")
    function.click(cxetermindividual.get_yes(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 7")
    #function.click(cxetermindividual.get_next3(driver))
    function.verify(cxetermindividual.get_terms_cond(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 7b")

    function.bookmark(module, ts_id, test_case, "Step 10")
    function.click(cxetermindividual.get_terms_cond(driver))
    time.sleep(15)
    function.verify(cxetermindividual.get_submit(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 10")

    function.bookmark(module, ts_id, test_case, "Step 11")
    function.click(cxetermindividual.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, module, ts_id, test_case, "Step 11")
    #function.verify(cxetermindividual.get_confirmation(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 11b")

    log.info(test_case + " Passed")

def TC015(driver, ts_id):
    test_case = "TC015"
    cxe_apply_case = CXELoginPage()
    cxe_home = CXEHomePage()

    fc.new_tab(driver, cxe)

    fc.click(cxe_apply_case.get_meralco_user_id(driver))
    fc.input_text(cxe_apply_case.get_email(driver), Registration['cxe_email'])
    fc.click(cxe_apply_case.get_next(driver))
    fc.input_text(cxe_apply_case.get_password(driver), Registration['cxe_password'])
    fc.click(cxe_apply_case.get_sign_in(driver))
    fc.click(cxe_apply_case.get_sms(driver))
    time.sleep(15)

    fc.click(cxe_apply_case.get_stay_sign_no(driver))
    time.sleep(10)

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_cxe_search(driver))
    fc.input_text(cxe_home.get_cxe_search_case(driver), SAMO['caseNumber'])
    cxe_home.get_cxe_search_case(driver).send_keys(Keys.ENTER)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.click(cxe_home.get_cxe_change_owner(driver))
    fc.input_text(cxe_home.get_cxe_assign_new_owner(driver), SAMO['newOwner'])
    fc.click(cxe_home.get_cxe_case_owner(driver))
    fc.click(cxe_home.get_cxe_case_submit(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    #Step #3

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    fc.click(cxe_home.get_cxe_edit_case(driver))
    fc.click(cxe_home.get_case_status(driver))
    fc.click(cxe_home.get_application_validated_stat(driver))
    fc.scroll_element(driver,cxe_home.get_energization_date(driver))
    fc.input_text(cxe_home.get_energization_date(driver), SAMO['energizationDate'])
    time.sleep(10)
    #fc.click(cxe_home.get_case_status_save(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 10")
    fc.click(cxe_home.get_cxe_edit_case(driver))
    fc.click(cxe_home.get_case_status(driver))
    fc.click(cxe_home.get_meter_socket_stat(driver))
    fc.input_text(cxe_home.get_energization_date(driver), SAMO['energizationDate'])
    fc.click(cxe_home.get_cxe_customer_type(driver))
    fc.click(cxe_home.get_cxe_customer_private(driver))
    fc.click(cxe_home.get_case_status_save(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 10")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 13")
    fc.click(cxe_home.get_cxe_edit_case(driver))
    fc.click(cxe_home.get_case_status(driver))
    fc.click(cxe_home.get_meter_socket_stat(driver))
    fc.input_text(cxe_home.get_energization_date(driver), SAMO['energizationDate'])
    fc.click(cxe_home.get_cxe_customer_type(driver))
    fc.click(cxe_home.get_cxe_customer_private(driver))
    fc.click(cxe_home.get_case_status_save(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 13")

    fc.click(cxe_home.get_cxe_search(driver))
    fc.input_text(cxe_home.get_cxe_search_case(driver), SAMO['caseNumber'])
    cxe_home.get_cxe_search_case(driver).send_keys(Keys.ENTER)
    fc.click(cxe_home.get_case_number_table(driver, SAMO['caseNumber']))


def TC016(driver, ts_id, firstname, lastname, emailaddress, mobilenumber, can, businessname):
    test_case = "TC016"
    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_home = CXEApplyHomePage()
    function.verify(cxe_apply_home.get_label_service_application(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1b")

    cxetermcontractor = CXETerminateContractor()
    function.bookmark(module, ts_id, test_case, "Step 2")
    function.click(cxetermcontractor.get_contractor(driver))
    function.verify(cxetermcontractor.get_start_service(driver))
    function.verify(cxetermcontractor.get_modify_service(driver))
    function.verify(cxetermcontractor.get_reactivate_service(driver))
    function.verify(cxetermcontractor.get_stop_service(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 2")

    function.bookmark(module, ts_id, test_case, "Step 3")
    function.click(cxetermcontractor.get_stop_service_clk(driver))
    function.verify(cxetermcontractor.get_stop_lbl(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3")

    function.bookmark(module, ts_id, test_case, "Step 4")
    function.verify(cxetermcontractor.get_CAN(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 4")

    function.bookmark(module, ts_id, test_case, "Step 5")
    function.input_text(cxetermcontractor.get_CAN(driver), can)
    function.screen_capture(driver, module, ts_id, test_case, "Step 5")

    function.bookmark(module, ts_id, test_case, "Step 6")
    function.input_text(cxetermcontractor.get_firstname(driver), firstname)
    function.input_text(cxetermcontractor.get_lastname(driver), lastname)
    function.input_text(cxetermcontractor.get_emailaddress(driver), emailaddress)
    function.input_text(cxetermcontractor.get_mobile_number(driver), mobilenumber)
    function.input_text(cxetermcontractor.get_businessname(driver), businessname)
    function.screen_capture(driver, module, ts_id, test_case, "Step 6")
    function.click(cxetermcontractor.get_next1(driver))
    function.verify(cxetermcontractor.get_terms_cond(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 6b")



    function.bookmark(module, ts_id, test_case, "Step 7")
    function.click(cxetermcontractor.get_terms_cond(driver))
    time.sleep(15)
    function.verify(cxetermcontractor.get_submit(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 10")

    function.bookmark(module, ts_id, test_case, "Step 8")
    function.click(cxetermcontractor.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, module, ts_id, test_case, "Step 8")
    #function.verify(cxetermindividual.get_confirmation(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 8b")

    log.info(test_case + " Passed")


def TC017(driver, ts_id, firstname, lastname, emailaddress, businessname, mobilenumber, can, sin, servadd):
    test_case = "TC017"
    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_home = CXEApplyHomePage()
    function.verify(cxe_apply_home.get_label_service_application(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1b")

    cxereactivatecontractor = CXEReactivateContractor()
    function.bookmark(module, ts_id, test_case, "Step 2")

    function.click(cxereactivatecontractor.get_contractor(driver))
    function.verify(cxereactivatecontractor.get_start_service(driver))
    function.verify(cxereactivatecontractor.get_modify_service(driver))
    function.verify(cxereactivatecontractor.get_reactivate_service(driver))
    function.verify(cxereactivatecontractor.get_stop_service(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 2")

    function.bookmark(module, ts_id, test_case, "Step 3")
    function.click(cxereactivatecontractor.get_reactivate_service(driver))
    function.verify(cxereactivatecontractor.get_reactivate_page(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3")

    function.bookmark(module, ts_id, test_case, "Step 4")
    function.input_text(cxereactivatecontractor.get_firstname(driver), firstname)
    function.input_text(cxereactivatecontractor.get_lastname(driver), lastname)
    function.input_text(cxereactivatecontractor.get_emailaddress(driver), emailaddress)
    function.input_text(cxereactivatecontractor.get_businessname(driver), businessname)
    function.input_text(cxereactivatecontractor.get_mobile_number(driver), mobilenumber)
    #function.input_text(cxereactivatecontractor.get_companyname(driver), companyname)
    #function.input_text(cxereactivatecontractor.get_landline(driver), landline)
    function.screen_capture(driver, module, ts_id, test_case, "Step 4")
    function.click(cxereactivatecontractor.get_next1(driver))
    function.verify(cxereactivatecontractor.get_cust_info(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 4b")

    function.bookmark(module, ts_id, test_case, "Step 5")
    function.verify(cxereactivatecontractor.get_CAN(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 5")


    function.bookmark(module, ts_id, test_case, "Step 6")
    function.input_text(cxereactivatecontractor.get_CAN(driver), can)
    function.screen_capture(driver, module, ts_id, test_case, "Step 6")


    function.bookmark(module, ts_id, test_case, "Step 7")
    function.input_text(cxereactivatecontractor.get_firstname_cust(driver), firstname)
    function.input_text(cxereactivatecontractor.get_lastname_cust(driver), lastname)
    function.input_text(cxereactivatecontractor.get_emailaddress_cust(driver), emailaddress)
    function.input_text(cxereactivatecontractor.get_mobile_number_cust(driver), mobilenumber)
    function.screen_capture(driver, module, ts_id, test_case, "Step 7")
    function.click(cxereactivatecontractor.get_next2(driver))
    function.verify(cxereactivatecontractor.get_new_address(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 7b")

    function.bookmark(module, ts_id, test_case, "Step 8")
    function.click(cxereactivatecontractor.get_no(driver))
    function.input_text(cxereactivatecontractor.get_serv_add(driver), servadd)
    function.click(cxereactivatecontractor.get_province(driver))
    function.click(cxereactivatecontractor.get_province_val(driver))
    function.click(cxereactivatecontractor.get_city(driver))
    function.click(cxereactivatecontractor.get_city_val(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 8")
    function.click(cxereactivatecontractor.get_next3(driver))

    function.bookmark(module, ts_id, test_case, "Step 9")
    function.click(cxereactivatecontractor.get_terms_cond_clk(driver))
    time.sleep(15)
    function.verify(cxereactivatecontractor.get_submit(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 9")

    function.bookmark(module, ts_id, test_case, "Step 10")
    function.click(cxereactivatecontractor.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, module, ts_id, test_case, "Step 10")
    #function.verify(cxetermindividual.get_confirmation(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 10b")

    log.info(test_case + " Passed")

def TC010(driver, ts_id, email, password, birthday):
    test_case = "TC010"
    log.info("==========Log in==========")

    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    login = LoginPage()
    function.input_text(login.get_email(driver), email)
    function.input_text(login.get_password(driver), password)
    function.click(login.get_log_in(driver))
    home = HomePage()
    function.verify(home.get_hello_message(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1")

    cxeterminateSA = CXEAccountPage()
    function.bookmark(module, ts_id, test_case, "Step 2")
    function.click(cxeterminateSA.get_view_details(driver))
    function.verify(cxeterminateSA.get_account_page(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 2")

    function.bookmark(module, ts_id, test_case, "Step 3")
    function.click(cxeterminateSA.get_submit_term(driver))
    function.click(cxeterminateSA.get_account_clk(driver))
    function.click(cxeterminateSA.get_reactivate_service(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3")
    function.verify(cxeterminateSA.get_request_page(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3b")

    function.bookmark(module, ts_id, test_case, "Step 4")
    function.screen_capture(driver, module, ts_id, test_case, "Step 4")
    function.input_text(cxeterminateSA.get_birthday(driver), birthday)
    function.screen_capture(driver, module, ts_id, test_case, "Step 4")
    function.click(cxeterminateSA.get_click_next(driver))
    function.verify(cxeterminateSA.get_new_address(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 4b")

    function.bookmark(module, ts_id, test_case, "Step 5")
    function.click(cxeterminateSA.get_ownership(driver))
    function.click(cxeterminateSA.get_ownership_value(driver))
    function.click(cxeterminateSA.get_click_next2(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 5")
    function.verify(cxeterminateSA.get_value_added(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 5b")

    function.bookmark(module, ts_id, test_case, "Step 6")
    function.screen_capture(driver, module, ts_id, test_case, "Step 6")
    function.click(cxeterminateSA.get_click_next3(driver))
    function.verify(cxeterminateSA.get_terms_cond(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 6b")

    function.bookmark(module, ts_id, test_case, "Step 7")
    function.click(cxeterminateSA.get_terms_cond(driver))
    time.sleep(15)
    function.verify(cxeterminateSA.get_submit(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 7")

    function.bookmark(module, ts_id, test_case, "Step 8")
    function.click(cxeterminateSA.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, module, ts_id, test_case, "Step 8")
    # function.verify(cxetermindividual.get_confirmation(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 8b")

    log.info(test_case + " Passed")

def TC016(driver, ts_id, firstname, lastname, emailaddress, mobilenumber, can, designation, companyname, landline):
    test_case = "TC016"
    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_home = CXEApplyHomePage()
    function.verify(cxe_apply_home.get_label_service_application(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1b")

    cxereactivatebusiness = CXEReactivateBusiness()
    function.bookmark(module, ts_id, test_case, "Step 2")
    function.click(cxereactivatebusiness.get_business(driver))
    function.verify(cxereactivatebusiness.get_start_service(driver))
    function.verify(cxereactivatebusiness.get_modify_service(driver))
    function.verify(cxereactivatebusiness.get_reactivate_service(driver))
    function.verify(cxereactivatebusiness.get_stop_service(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 2")

    function.bookmark(module, ts_id, test_case, "Step 3")
    function.click(cxereactivatebusiness.get_reactivate_service(driver))
    function.verify(cxereactivatebusiness.get_stop_lbl(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3")

    function.bookmark(module, ts_id, test_case, "Step 4")
    function.verify(cxereactivatebusiness.get_CAN(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 4")

    function.bookmark(module, ts_id, test_case, "Step 5")
    function.input_text(cxereactivatebusiness.get_CAN(driver), can)
    function.screen_capture(driver, module, ts_id, test_case, "Step 5")

    function.bookmark(module, ts_id, test_case, "Step 6")
    function.input_text(cxereactivatebusiness.get_firstname(driver), firstname)
    function.input_text(cxereactivatebusiness.get_lastname(driver), lastname)
    function.input_text(cxereactivatebusiness.get_emailaddress(driver), emailaddress)
    function.input_text(cxereactivatebusiness.get_mobile_number(driver), mobilenumber)
    function.input_text(cxereactivatebusiness.get_designation(driver), designation)
    function.input_text(cxereactivatebusiness.get_companyname(driver), companyname)
    function.input_text(cxereactivatebusiness.get_landline(driver), landline)
    function.screen_capture(driver, module, ts_id, test_case, "Step 6")
    function.click(cxereactivatebusiness.get_next1(driver))
    function.verify(cxereactivatebusiness.get_value_add(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 6b")

    function.bookmark(module, ts_id, test_case, "Step 7")
    function.click(cxereactivatebusiness.get_yes(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 7")
    #function.click(cxetermindividual.get_next3(driver))
    function.verify(cxereactivatebusiness.get_terms_cond(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 7b")

    function.bookmark(module, ts_id, test_case, "Step 8")
    function.click(cxereactivatebusiness.get_terms_cond_clk(driver))
    time.sleep(15)
    function.verify(cxereactivatebusiness.get_submit(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 8")

    function.bookmark(module, ts_id, test_case, "Step 9")
    function.click(cxereactivatebusiness.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, module, ts_id, test_case, "Step 9")
    #function.verify(cxetermindividual.get_confirmation(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 9b")

    log.info(test_case + " Passed")

def TC020(driver, ts_id):
    test_case = "TC020"
    home = HomePage()
    account = ManageAccountsPage()
    service = PageService()

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, Concern['username_multiple_service'], Concern['password'])
    time.sleep(10)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.modal_click(driver, home.get_accounts(driver))
    fc.modal_click(driver, home.get_manage_accounts(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    fc.click(account.get_submit(driver))
    #fc.modal_click(driver, account.get_select_sin(driver))
    fc.scroll_element(driver, account.get_change_service(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")
    fc.click(account.get_change_service(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    fc.click(service.get_change_service(driver))
    fc.scroll_element(driver, service.get_next_button(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")
    fc.click(service.get_next_button(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4b")
    fc.scroll_element(driver, home.get_search(driver))
    time.sleep(3)

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    fc.scroll_element(driver, service.get_next_modify_button(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")
    fc.click(service.get_next_modify_button(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    fc.scroll_element(driver, service.get_submit_modify_button(driver))
    time.sleep(10)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")
    fc.click(service.get_submit_modify_button(driver))

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    fc.scroll_element(driver, home.get_search(driver))
    time.sleep(2)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7")
    fc.click(service.get_back_to_home(driver))
    time.sleep(5)

def TC021(driver, ts_id):
    test_case = "TC021"
    home = HomePage()
    account = ManageAccountsPage()
    service = PageService()

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, SAMO['business_account_email'], Concern['password'])
    time.sleep(10)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.modal_click(driver, home.get_accounts(driver))
    fc.modal_click(driver, home.get_manage_accounts(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    fc.click(account.get_submit(driver))
    time.sleep(5)
    fc.scroll_element(driver, account.get_change_contract(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")
    fc.click(account.get_change_contract(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    fc.click(service.get_change_contract_radio_btn(driver))
    fc.scroll_element(driver, service.get_next_button(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")
    fc.click(service.get_next_button(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    fc.scroll_element(driver, service.get_next_modify_button(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")
    fc.click(service.get_next_modify_button(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    fc.scroll_element(driver, service.get_submit_modify_contract(driver))
    time.sleep(3)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")
    time.sleep(10)

    fc.click(service.get_submit_modify_contract(driver))

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    fc.scroll_element(driver, home.get_search(driver))
    time.sleep(2)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7")
    fc.click(service.get_back_to_home(driver))

def TC022(driver, ts_id):
    test_case = "TC022"
    home = HomePage()
    account = ManageAccountsPage()
    service = PageService()

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, Concern['username_single_service'], Concern['password'])
    time.sleep(10)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.modal_click(driver, home.get_accounts(driver))
    fc.modal_click(driver, home.get_manage_accounts(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    fc.click(account.get_submit(driver))
    time.sleep(3)
    fc.scroll_element(driver, account.get_change_contract(driver))
    fc.click(account.get_change_contract(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    fc.click(service.get_transfer_service(driver))
    fc.scroll_element(driver, service.get_next_button(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")
    fc.click(service.get_next_button(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    fc.scroll_element(driver, service.get_next_modify_button(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")
    fc.click(service.get_next_modify_button(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    fc.scroll_element(driver, service.get_submit_modify_contract(driver))
    time.sleep(3)
    time.sleep(20)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")

    fc.click(service.get_submit_modify_contract(driver))

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    fc.scroll_element(driver, home.get_search(driver))
    time.sleep(2)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7")
    fc.click(service.get_back_to_home(driver))

def TC023(driver, ts_id, email):
    test_case = "TC023"
    home = HomePage()
    account = ManageAccountsPage()
    service = PageService()

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, email, Concern['password'])
    time.sleep(10)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.modal_click(driver, home.get_accounts(driver))
    fc.modal_click(driver, home.get_manage_accounts(driver))
    time.sleep(10)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")


    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    fc.click(account.get_submit(driver))
    time.sleep(3)
    fc.scroll_element(driver, account.get_stop_service(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")
    fc.click(account.get_stop_service(driver))

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    time.sleep(20)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")
    fc.click(service.get_next_button(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4b")

def TC024(driver, ts_id, email):
    test_case = "TC024"
    home = HomePage()
    account = ManageAccountsPage()
    service = PageService()

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, email, Concern['password'])
    time.sleep(10)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.modal_click(driver, home.get_accounts(driver))
    fc.modal_click(driver, home.get_manage_accounts(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    fc.click(account.get_submit(driver))
    time.sleep(5)
    fc.scroll_element(driver, account.get_reactivate_service(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")
    fc.click(account.get_reactivate_service(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3b")

    time.sleep(5)
    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    fc.scroll_element(driver, service.get_next_button(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")
    fc.click(service.get_next_button(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    fc.select_dropdown_element(service.get_reconnect_ownership(driver), Concern['home_ownership'])
    time.sleep(3)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")
    fc.click(service.get_next_recconect(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    fc.scroll_element(driver, service.get_second_next_reconnect(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")
    fc.click(service.get_second_next_reconnect(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    time.sleep(20)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7")
    fc.click(service.get_submit_recconect(driver))

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 8")
    fc.scroll_element(driver, home.get_search(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8")
    time.sleep(5)

def TC025(driver, ts_id):
    test_case = "TC025"
    cxe_apply_home = CXEApplyHomePage()
    cxeHome = CXEHomePage()
    cxe_apply_reg = CXEApplyIndividual()
    yopmail_inbox = YopmailInboxPage()
    resetPass = ResetPasswordPage()

    fc.new_tab(driver, cxe_apply)

    time.sleep(5)
    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    fc.verify(cxe_apply_home.get_label_service_application(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.click(cxe_apply_home.get_individual(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    fc.click(cxe_apply_home.get_individual_start(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    time.sleep(5)
    fc.modal_click(driver, cxeHome.get_peccbm_no(driver))
    time.sleep(5)

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    fc.input_text(cxe_apply_reg.get_email_attr(driver), SAMO['newemail'])
    fc.input_text(cxe_apply_reg.get_firstname_attr(driver), SAMO['individual_account_first'])
    #fc.input_text(cxe_apply_reg.get_middle_name(driver), SAMO['individual_account_middle'])
    fc.input_text(cxe_apply_reg.get_lastname_attr(driver), SAMO['individual_account_last'])
    fc.input_text(cxe_apply_reg.get_mobile_num(driver), SAMO['mobileNumberIndividual'])

    fc.click(cxe_apply_reg.get_terms_and_conditions(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")

    fc.click(cxe_apply_reg.get_register_btn(driver))

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    fc.new_tab(driver, yopmail)
    fc.input_text(yopmail_home.get_email(driver), SAMO['newemail'])
    fc.click(yopmail_home.get_check_inbox(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    yopmail_inbox.get_here_link(driver)
    time.sleep(10)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    fc.input_text(resetPass.get_new_password(driver), SAMO['business_account_password'])
    fc.input_text(resetPass.get_confirm_password(driver), SAMO['business_account_password'])
    fc.click(resetPass.get_set_password(driver))

    time.sleep(5)

    Log_In_Meralco_Online(driver, SAMO['newemail'], SAMO['business_account_password'])
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7")

def TC026(driver, ts_id):
    test_case = "TC026"
    cxe_apply_home = CXEApplyHomePage()
    cxe_apply_business = CXEApplyBusiness()
    cxeHome = CXEHomePage()
    cxe_apply_reg = CXEApplyBusinessRegPage()
    home = HomePage()

    fc.new_tab(driver, cxe_apply)

    time.sleep(5)
    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    fc.verify(cxe_apply_home.get_label_service_application(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.click(cxe_apply_business.get_business(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    fc.click(cxe_apply_business.get_clk_business_start(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    time.sleep(5)
    fc.modal_click(driver, cxeHome.get_peccbm_no(driver))
    time.sleep(5)

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    fc.input_text(cxe_apply_reg.get_company_name(driver), SAMO['business_company_name'])
    fc.input_text(cxe_apply_reg.get_company_landline(driver), SAMO['business_company_landline'])
    fc.input_text(cxe_apply_reg.get_first_name(driver), SAMO['business_first_name'])
    fc.input_text(cxe_apply_reg.get_last_name(driver), SAMO['business_last_name'])
    fc.input_text(cxe_apply_reg.get_email_address(driver), SAMO['business_emailaddress'])
    fc.input_text(cxe_apply_reg.get_mobile(driver), SAMO['business_mobile_number'])
    fc.input_text(cxe_apply_reg.get_designation(driver), SAMO['business_designation'])
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")
    fc.click(cxe_apply_reg.get_next(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4b")

    fc.scroll_element(driver, home.get_search(driver))

    time.sleep(5)
    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    fc.input_text(cxe_apply_reg.get_inp_serv_add(driver), SAMO['service_add'])
    fc.click(cxe_apply_reg.get_clk_province(driver))
    fc.click(cxe_apply_reg.get_province_value(driver))
    fc.click(cxe_apply_reg.get_municipality(driver))
    fc.click(cxe_apply_reg.get_clk_mciplity_val(driver))
    fc.click(cxe_apply_reg.get_next2(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    fc.click(cxe_apply_reg.get_btn_next3(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    fc.click(cxe_apply_reg.get_click_term_condition(driver))
    time.sleep(20)
    fc.verify(cxe_apply_reg.get_submit(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 8")
    fc.click(cxe_apply_reg.get_submit(driver))
    fc.click(cxe_apply_reg.get_confirmation(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8")

def TC027(driver, ts_id):
    test_case = "TC026"
    cxe_apply_home = CXEApplyHomePage()
    cxe_apply_business = CXEApplyBusiness()
    cxeHome = CXEHomePage()
    cxe_apply_reg = CXEApplyBusinessRegPage()
    home = HomePage()

    fc.new_tab(driver, cxe_apply)

    time.sleep(5)
    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    fc.verify(cxe_apply_home.get_label_service_application(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.click(cxe_apply_business.get_business(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    fc.click(cxe_apply_business.get_business_modify(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    fc.verify(cxe_apply_reg.get_can_cxe_modify(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    fc.input_text(cxe_apply_reg.get_can_cxe_modify(driver), SAMO['business_can'])
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    fc.click(cxe_apply_reg.get_change_contract(driver))
    fc.click(cxe_apply_reg.get_change_contract_name(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    fc.input_text(cxe_apply_reg.get_company_name(driver), SAMO['business_company_name'])
    fc.input_text(cxe_apply_reg.get_landline(driver), SAMO['business_company_landline'])
    fc.input_text(cxe_apply_reg.get_firstname(driver), SAMO['business_first_name'])
    fc.input_text(cxe_apply_reg.get_lastname(driver), SAMO['business_last_name'])
    fc.input_text(cxe_apply_reg.get_email(driver), SAMO['business_emailaddress'])
    fc.input_text(cxe_apply_reg.get_mobile_num(driver), SAMO['business_mobile_number'])
    fc.input_text(cxe_apply_reg.get_cxe_designation(driver), SAMO['business_designation'])
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7")
    fc.click(cxe_apply_reg.get_modify_next_btn(driver))
    fc.scroll_element(driver, cxe_apply_reg.get_modify_contact_firstname(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 8")
    fc.input_text(cxe_apply_reg.get_modify_contact_firstname(driver), SAMO['business_first_name'])
    fc.input_text(cxe_apply_reg.get_modify_contact_lastname(driver), SAMO['business_last_name'])
    fc.input_text(cxe_apply_reg.get_modify_contact_email(driver), SAMO['business_emailaddress'])
    fc.input_text(cxe_apply_reg.get_modify_contact_mobilenum(driver), SAMO['business_mobile_number'])
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8")
    fc.click(cxe_apply_reg.get_modify_contact_next_btn(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 9")
    fc.click(cxe_apply_reg.get_modify_addedServ_next_btn(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 9")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 10")
    fc.click(cxe_apply_reg.get_modify_terms_conditions)
    time.sleep(15)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 10")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 11")
    fc.click(cxe_apply_reg.get_modify_submit(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 11")

def TC028(driver, ts_id, can, companyname, landline, firstname, lastname, emailaddress, designation, mobilenumber):
    test_case = "TC028"
    function = Functions()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_home = CXEApplyHomePage()
    function.verify(cxe_apply_home.get_label_service_application(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1b")

    cxemodifybusiness = CXEModificationBusiness()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    function.click(cxemodifybusiness.get_business(driver))
    function.verify(cxemodifybusiness.get_start_service(driver))
    function.verify(cxemodifybusiness.get_modify_service(driver))
    function.verify(cxemodifybusiness.get_reactivate_service(driver))
    function.verify(cxemodifybusiness.get_stop_service(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    function.click(cxemodifybusiness.get_modify_service_clk(driver))
    function.verify(cxemodifybusiness.get_request(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    function.verify(cxemodifybusiness.get_CAN(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    function.input_text(cxemodifybusiness.get_CAN(driver), can)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    function.click(cxemodifybusiness.get_change_contract_details(driver))
    function.click(cxemodifybusiness.get_change_contract_name(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    function.input_text(cxemodifybusiness.get_company_name(driver), companyname)
    function.input_text(cxemodifybusiness.get_landline(driver), landline)
    function.input_text(cxemodifybusiness.get_first_name(driver), firstname)
    function.input_text(cxemodifybusiness.get_last_name(driver), lastname)
    function.input_text(cxemodifybusiness.get_emailaddress(driver), emailaddress)
    function.input_text(cxemodifybusiness.get_mobile_number(driver), mobilenumber)
    function.input_text(cxemodifybusiness.get_designation(driver), designation)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7")
    function.click(cxemodifybusiness.get_next1(driver))
    function.verify(cxemodifybusiness.get_contact_info(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7b")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 8")
    function.input_text(cxemodifybusiness.get_first_name_mod(driver), firstname)
    function.input_text(cxemodifybusiness.get_last_name_mod(driver), lastname)
    function.input_text(cxemodifybusiness.get_emailddress_mod(driver), emailaddress)
    function.input_text(cxemodifybusiness.get_mobile_number_mod(driver), mobilenumber)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8")
    function.click(cxemodifybusiness.get_next2(driver))
    function.verify(cxemodifybusiness.get_value_added(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8b")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 9")
    function.click(cxemodifybusiness.get_yes(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 9")
    function.click(cxemodifybusiness.get_next3(driver))
    function.verify(cxemodifybusiness.get_terms_condition(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 9b")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 10")
    function.click(cxemodifybusiness.get_click_term_condition(driver))
    time.sleep(20)
    function.verify(cxemodifybusiness.get_submit(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 10")
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 11")
    function.click(cxemodifybusiness.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 11")
    function.verify(cxemodifybusiness.get_confirmation(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 11b")

    log.info(test_case + " Passed")
    

def TC029(driver, ts_id, can, companyname, firstname, lastname, emailaddress, mobilenumber):
    test_case = "TC029"
    function = Functions()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_home = CXEApplyHomePage()
    function.verify(cxe_apply_home.get_label_service_application(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1b")

    cxemodifycontractor = CXEModificationContractor()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    function.click(cxemodifycontractor.get_contractor(driver))
    function.verify(cxemodifycontractor.get_start_service_cn(driver))
    function.verify(cxemodifycontractor.get_modify_service_cn(driver))
    function.verify(cxemodifycontractor.get_reactivate_service_cn(driver))
    function.verify(cxemodifycontractor.get_stop_service_cn(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    function.click(cxemodifycontractor.get_modify_service_clk(driver))
    function.verify(cxemodifycontractor.get_request(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    function.verify(cxemodifycontractor.get_CAN(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    function.input_text(cxemodifycontractor.get_CAN(driver), can)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    function.click(cxemodifycontractor.get_change_service_details(driver))
    function.click(cxemodifycontractor.get_change_downgrade_electrical(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")
    function.click(cxemodifycontractor.get_click_nxtcont(driver))


    function.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    function.input_text(cxemodifycontractor.get_company_name(driver), companyname)
    function.input_text(cxemodifycontractor.get_first_name(driver), firstname)
    function.input_text(cxemodifycontractor.get_last_name(driver), lastname)
    function.input_text(cxemodifycontractor.get_emailaddress(driver), emailaddress)
    function.input_text(cxemodifycontractor.get_mobile_number(driver), mobilenumber)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7")
    function.click(cxemodifycontractor.get_next1(driver))
    function.verify(cxemodifycontractor.get_terms_condition(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7b")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 8")
    function.click(cxemodifycontractor.get_click_term_condition(driver))
    time.sleep(10)
    function.verify(cxemodifycontractor.get_submit(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 9")
    function.click(cxemodifycontractor.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 9")
    function.verify(cxemodifycontractor.get_confirmation(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 9b")

    log.info(test_case + " Passed")

def TC031(driver, ts_id):
    test_case = "TC032"
    fc = Functions()
    cxe_apply_home = CXEApplyHomePage()
    cxe_terminate = CXETerminateIndividual()

    fc.new_tab(driver, cxe_apply)

    fc.click(cxe_apply_home.get_individual(driver))
    fc.click(cxe_apply_home.get_individual_stop(driver))

    fc.input_text(cxe_terminate.get_CAN(driver), SAMO['individual_account_can'])
    fc.input_text(cxe_terminate.get_firstname(driver), SAMO['individual_account_first'])
    fc.input_text(cxe_terminate.get_lastname(driver), SAMO['individual_account_last'])
    fc.input_text(cxe_terminate.get_emailaddress(driver), SAMO['individual_account_email'])
    fc.input_text(cxe_terminate.get_mobile_number(driver), SAMO['individual_account_mobile'])

    fc.scroll_element(driver, cxe_terminate.get_next_button(driver))
    time.sleep(10)
    fc.click(cxe_terminate.get_next_button(driver))

    time.sleep(5)
    fc.click(cxe_terminate.get_terms_cond(driver))
    time.sleep(10)
    fc.click(cxe_terminate.get_submit(driver))


def TC032(driver, ts_id, firstname, lastname, emailaddress, mobilenumber, can):
    test_case = "TC032"
    function = Functions()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_home = CXEApplyHomePage()
    function.verify(cxe_apply_home.get_label_service_application(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1b")

    cxetermindividual = CXETerminateBusiness()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    function.click(cxetermindividual.get_business(driver))
    function.verify(cxetermindividual.get_start_service(driver))
    function.verify(cxetermindividual.get_modify_service(driver))
    function.verify(cxetermindividual.get_reactivate_service(driver))
    function.verify(cxetermindividual.get_stop_service(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    function.click(cxetermindividual.get_stop_service_clk(driver))
    function.verify(cxetermindividual.get_stop_lbl(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    function.verify(cxetermindividual.get_CAN(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    function.input_text(cxetermindividual.get_CAN(driver), can)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    function.input_text(cxetermindividual.get_firstname(driver), firstname)
    function.input_text(cxetermindividual.get_lastname(driver), lastname)
    function.input_text(cxetermindividual.get_emailaddress(driver), emailaddress)
    function.input_text(cxetermindividual.get_mobile_number(driver), mobilenumber)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")
    function.click(cxetermindividual.get_next1(driver))
    function.verify(cxetermindividual.get_terms_cond(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6b")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    function.click(cxetermindividual.get_yes(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7")
    #function.click(cxetermindividual.get_next3(driver))
    function.verify(cxetermindividual.get_terms_cond(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7b")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 10")
    function.click(cxetermindividual.get_terms_cond(driver))
    time.sleep(15)
    function.verify(cxetermindividual.get_submit(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 10")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 11")
    function.click(cxetermindividual.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 11")
    #function.verify(cxetermindividual.get_confirmation(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 11b")

    log.info(test_case + " Passed")

def TC033(driver, ts_id, firstname, lastname, emailaddress, mobilenumber, can, businessname):
    test_case = "TC033"
    function = Functions()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_home = CXEApplyHomePage()
    function.verify(cxe_apply_home.get_label_service_application(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1b")

    cxetermcontractor = CXETerminateContractor()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    function.click(cxetermcontractor.get_contractor(driver))
    function.verify(cxetermcontractor.get_start_service(driver))
    function.verify(cxetermcontractor.get_modify_service(driver))
    function.verify(cxetermcontractor.get_reactivate_service(driver))
    function.verify(cxetermcontractor.get_stop_service(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    function.click(cxetermcontractor.get_stop_service_clk(driver))
    function.verify(cxetermcontractor.get_stop_lbl(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    function.verify(cxetermcontractor.get_CAN(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    function.input_text(cxetermcontractor.get_CAN(driver), can)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    function.input_text(cxetermcontractor.get_firstname(driver), firstname)
    function.input_text(cxetermcontractor.get_lastname(driver), lastname)
    function.input_text(cxetermcontractor.get_emailaddress(driver), emailaddress)
    function.input_text(cxetermcontractor.get_mobile_number(driver), mobilenumber)
    function.input_text(cxetermcontractor.get_businessname(driver), businessname)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")
    function.click(cxetermcontractor.get_next1(driver))
    function.verify(cxetermcontractor.get_terms_cond(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6b")



    function.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    function.click(cxetermcontractor.get_terms_cond(driver))
    time.sleep(15)
    function.verify(cxetermcontractor.get_submit(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 10")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 8")
    function.click(cxetermcontractor.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8")
    #function.verify(cxetermindividual.get_confirmation(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8b")

    log.info(test_case + " Passed")

def TC034(driver, ts_id):
    test_case = "TC032"
    fc = Functions()
    cxe_apply_contractor = CXEApplyContractor()

    fc.new_tab(driver, cxe_apply)

    fc.click(cxe_apply_contractor.get_contractor(driver))
    fc.click(cxe_apply_contractor.get_contractor_reactivate(driver))

def TC035(driver, ts_id):
    test_case = "TC032"
    fc = Functions()
    cxe_apply_contractor = CXEApplyContractor()

    fc.new_tab(driver, cxe_apply)

    fc.click(cxe_apply_contractor.get_contractor(driver))
    fc.click(cxe_apply_contractor.get_contractor_reactivate(driver))


    fc.input_text(cxe_apply_contractor.get_first_name(driver), SAMO['individual_account_first'])
    fc.input_text(cxe_apply_contractor.get_last_name(driver), SAMO['individual_account_last'])
    fc.input_text(cxe_apply_contractor.get_business_name(driver), SAMO['business_company_name'])
    fc.input_text(cxe_apply_contractor.get_email_address(driver), SAMO['individual_account_email'])
    fc.input_text(cxe_apply_contractor.get_phone_number(driver), SAMO['individual_account_mobile'])

    fc.scroll_element(driver, cxe_apply_contractor.get_next_button(driver))
    fc.click(cxe_apply_contractor.get_next_button(driver))

    time.sleep(5)

    fc.input_text(cxe_apply_contractor.get_can_input(driver), SAMO['business_can'])
    fc.input_text(cxe_apply_contractor.get_first_name(driver), SAMO['individual_account_first'])
    fc.input_text(cxe_apply_contractor.get_last_name_recontract(driver), SAMO['individual_account_last'])
    fc.input_text(cxe_apply_contractor.get_email_address(driver), SAMO['individual_account_email'])
    fc.input_text(cxe_apply_contractor.get_phone_number(driver), SAMO['individual_account_mobile'])

def TC087(driver, ts_id):
    test_case = "TC087"
    home = HomePage()
    fc.modal_click(driver, home.get_overview(driver))
    time.sleep(5)
    fc.scroll_element(driver, home.get_activity_tracker(driver))
    fc.click(home.get_activity_tracker(driver))
    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")
    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

def TC115(driver, ts_id, can, sin , companyname, landline, firstname, lastname, emailaddress, designation, mobilenumber):
    test_case = "TC115"
    function = Functions()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_home = CXEApplyHomePage()
    function.verify(cxe_apply_home.get_label_service_application(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1b")

    cxemodifyindivid = CXEModificationIndividual()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    function.click(cxemodifyindivid.get_individual(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    function.click(cxemodifyindivid.get_modify_service_clk(driver))
    function.verify(cxemodifyindivid.get_request(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    function.verify(cxemodifyindivid.get_CAN(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    function.input_text(cxemodifyindivid.get_CAN(driver), can)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    function.input_text(cxemodifyindivid.get_SIN(driver), sin)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")


    function.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    function.click(cxemodifyindivid.get_change_contract_details(driver))
    function.click(cxemodifyindivid.get_change_contract_name(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 8")
    function.input_text(cxemodifyindivid.get_first_name(driver), firstname)
    function.input_text(cxemodifyindivid.get_last_name(driver), lastname)
    function.input_text(cxemodifyindivid.get_emailaddress(driver), emailaddress)
    function.input_text(cxemodifyindivid.get_mobile_number(driver), mobilenumber)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8")
    function.click(cxemodifyindivid.get_next1(driver))
    function.verify(cxemodifyindivid.get_contact_info(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7b")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 9")
    function.input_text(cxemodifyindivid.get_first_name_mod(driver), firstname)
    function.input_text(cxemodifyindivid.get_last_name_mod(driver), lastname)
    function.input_text(cxemodifyindivid.get_emailddress_mod(driver), emailaddress)
    function.input_text(cxemodifyindivid.get_mobile_number_mod(driver), mobilenumber)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 9")
    function.click(cxemodifyindivid.get_next2(driver))
    function.verify(cxemodifyindivid.get_value_added(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 9b")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 10")
    function.click(cxemodifyindivid.get_yes(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 10")
    function.click(cxemodifyindivid.get_next3(driver))
    function.verify(cxemodifyindivid.get_terms_condition(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 10b")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 11")
    function.click(cxemodifyindivid.get_click_term_condition(driver))
    time.sleep(20)
    function.verify(cxemodifyindivid.get_submit(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 11")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 12")
    function.click(cxemodifyindivid.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 12")
    function.verify(cxemodifyindivid.get_confirmation(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 12b")

    log.info(test_case + " Passed")


def TC116(driver, ts_id, can, sin , companyname, landline, firstname, lastname, emailaddress, designation, mobilenumber):
    test_case = "TC116"
    function = Functions()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_home = CXEApplyHomePage()
    function.verify(cxe_apply_home.get_label_service_application(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1b")

    cxemodifybusiness = CXEModificationBusiness()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    function.click(cxemodifybusiness.get_business(driver))
    function.verify(cxemodifybusiness.get_start_service(driver))
    function.verify(cxemodifybusiness.get_modify_service(driver))
    function.verify(cxemodifybusiness.get_reactivate_service(driver))
    function.verify(cxemodifybusiness.get_stop_service(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    function.click(cxemodifybusiness.get_modify_service_clk(driver))
    function.verify(cxemodifybusiness.get_request(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    function.verify(cxemodifybusiness.get_CAN(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    function.input_text(cxemodifybusiness.get_CAN(driver), can)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    function.input_text(cxemodifybusiness.get_SIN(driver), sin)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    function.click(cxemodifybusiness.get_change_contract_details(driver))
    function.click(cxemodifybusiness.get_change_contract_name(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 8")
    function.input_text(cxemodifybusiness.get_company_name(driver), companyname)
    function.input_text(cxemodifybusiness.get_landline(driver), landline)
    function.input_text(cxemodifybusiness.get_first_name(driver), firstname)
    function.input_text(cxemodifybusiness.get_last_name(driver), lastname)
    function.input_text(cxemodifybusiness.get_emailaddress(driver), emailaddress)
    function.input_text(cxemodifybusiness.get_mobile_number(driver), mobilenumber)
    function.input_text(cxemodifybusiness.get_designation(driver), designation)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8")
    function.click(cxemodifybusiness.get_next1(driver))
    function.verify(cxemodifybusiness.get_contact_info(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8b")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 9")
    function.input_text(cxemodifybusiness.get_first_name_mod(driver), firstname)
    function.input_text(cxemodifybusiness.get_last_name_mod(driver), lastname)
    function.input_text(cxemodifybusiness.get_emailddress_mod(driver), emailaddress)
    function.input_text(cxemodifybusiness.get_mobile_number_mod(driver), mobilenumber)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 9")
    function.click(cxemodifybusiness.get_next2(driver))
    function.verify(cxemodifybusiness.get_value_added(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 9b")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 10")
    function.click(cxemodifybusiness.get_yes(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 10")
    function.click(cxemodifybusiness.get_next3(driver))
    function.verify(cxemodifybusiness.get_terms_condition(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 10b")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 11")
    function.click(cxemodifybusiness.get_click_term_condition(driver))
    time.sleep(20)
    function.verify(cxemodifybusiness.get_submit(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 11")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 11")
    function.click(cxemodifybusiness.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 12")
    function.verify(cxemodifybusiness.get_confirmation(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 12")

    log.info(test_case + " Passed")


def TC117(driver, ts_id, can, sin , companyname, landline, firstname, lastname, emailaddress, designation, mobilenumber):
    test_case = "TC117"
    function = Functions()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_home = CXEApplyHomePage()
    function.verify(cxe_apply_home.get_label_service_application(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1b")

    cxemodifycontractor = CXEModificationContractor()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    function.click(cxemodifycontractor.get_contractor(driver))
    function.verify(cxemodifycontractor.get_start_service_cn(driver))
    function.verify(cxemodifycontractor.get_modify_service_cn(driver))
    function.verify(cxemodifycontractor.get_reactivate_service_cn(driver))
    function.verify(cxemodifycontractor.get_stop_service_cn(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    function.click(cxemodifycontractor.get_modify_service_clk(driver))
    function.verify(cxemodifycontractor.get_request(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    function.verify(cxemodifycontractor.get_CAN(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    function.input_text(cxemodifycontractor.get_CAN(driver), can)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    function.input_text(cxemodifycontractor.get_SIN(driver), sin)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    function.click(cxemodifycontractor.get_change_service_details(driver))
    function.click(cxemodifycontractor.get_change_downgrade_electrical(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7")
    function.click(cxemodifycontractor.get_click_nxtcont(driver))


    function.bookmark(serviceAppModule, ts_id, test_case, "Step 8")
    function.input_text(cxemodifycontractor.get_company_name(driver), companyname)
    function.input_text(cxemodifycontractor.get_first_name(driver), firstname)
    function.input_text(cxemodifycontractor.get_last_name(driver), lastname)
    function.input_text(cxemodifycontractor.get_emailaddress(driver), emailaddress)
    function.input_text(cxemodifycontractor.get_mobile_number(driver), mobilenumber)
    function.input_text(cxemodifycontractor.get_designation(driver), designation)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8")
    function.click(cxemodifycontractor.get_next1(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8b")


    function.bookmark(serviceAppModule, ts_id, test_case, "Step 9")
    function.click(cxemodifycontractor.get_click_term_condition(driver))
    time.sleep(10)
    function.verify(cxemodifycontractor.get_submit(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 9")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 10")
    function.click(cxemodifycontractor.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 10")
    function.verify(cxemodifycontractor.get_confirmation(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 10b")

    log.info(test_case + " Passed")


def TC118(driver, ts_id, firstname, lastname, emailaddress, mobilenumber, can, sin):
    test_case = "TC118"
    function = Functions()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_home = CXEApplyHomePage()
    function.verify(cxe_apply_home.get_label_service_application(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1b")

    cxetermindividual = CXETerminateIndividual()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    function.click(cxetermindividual.get_individual(driver))
    function.verify(cxetermindividual.get_start_service(driver))
    function.verify(cxetermindividual.get_modify_service(driver))
    function.verify(cxetermindividual.get_reactivate_service(driver))
    function.verify(cxetermindividual.get_stop_service(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    function.click(cxetermindividual.get_stop_service_clk(driver))
    function.verify(cxetermindividual.get_stop_lbl(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    function.verify(cxetermindividual.get_CAN(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    function.input_text(cxetermindividual.get_CAN(driver), can)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    function.input_text(cxetermindividual.get_SIN(driver), sin)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    function.input_text(cxetermindividual.get_firstname(driver), firstname)
    function.input_text(cxetermindividual.get_lastname(driver), lastname)
    function.input_text(cxetermindividual.get_emailaddress(driver), emailaddress)
    function.input_text(cxetermindividual.get_mobile_number(driver), mobilenumber)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7")
    function.click(cxetermindividual.get_next1(driver))
    function.verify(cxetermindividual.get_terms_cond(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7b")


    function.bookmark(serviceAppModule, ts_id, test_case, "Step 8")
    function.click(cxetermindividual.get_terms_cond(driver))
    time.sleep(15)
    function.verify(cxetermindividual.get_submit(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 9")
    function.click(cxetermindividual.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 9")
    #function.verify(cxetermindividual.get_confirmation(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 9b")

    log.info(test_case + " Passed")

def TC119(driver, ts_id, firstname, lastname, emailaddress, mobilenumber, can, sin):
    test_case = "TC119"
    function = Functions()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_home = CXEApplyHomePage()
    function.verify(cxe_apply_home.get_label_service_application(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1b")

    cxetermindividual = CXETerminateBusiness()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    function.click(cxetermindividual.get_business(driver))
    function.verify(cxetermindividual.get_start_service(driver))
    function.verify(cxetermindividual.get_modify_service(driver))
    function.verify(cxetermindividual.get_reactivate_service(driver))
    function.verify(cxetermindividual.get_stop_service(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    function.click(cxetermindividual.get_stop_service_clk(driver))
    function.verify(cxetermindividual.get_stop_lbl(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    function.verify(cxetermindividual.get_CAN(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    function.input_text(cxetermindividual.get_CAN(driver), can)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    function.input_text(cxetermindividual.get_SIN(driver), sin)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    function.input_text(cxetermindividual.get_firstname(driver), firstname)
    function.input_text(cxetermindividual.get_lastname(driver), lastname)
    function.input_text(cxetermindividual.get_emailaddress(driver), emailaddress)
    function.input_text(cxetermindividual.get_mobile_number(driver), mobilenumber)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7")
    function.click(cxetermindividual.get_next1(driver))
    function.verify(cxetermindividual.get_terms_cond(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7b")


    function.bookmark(serviceAppModule, ts_id, test_case, "Step 8")
    function.click(cxetermindividual.get_terms_cond(driver))
    time.sleep(15)
    function.verify(cxetermindividual.get_submit(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 9")
    function.click(cxetermindividual.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 9")
    #function.verify(cxetermindividual.get_confirmation(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 9b")

    log.info(test_case + " Passed")

def TC120(driver, ts_id, firstname, lastname, emailaddress, mobilenumber, can, businessname, sin):
    test_case = "TC120"
    function = Functions()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_home = CXEApplyHomePage()
    function.verify(cxe_apply_home.get_label_service_application(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1b")

    cxetermcontractor = CXETerminateContractor()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    function.click(cxetermcontractor.get_contractor(driver))
    function.verify(cxetermcontractor.get_start_service(driver))
    function.verify(cxetermcontractor.get_modify_service(driver))
    function.verify(cxetermcontractor.get_reactivate_service(driver))
    function.verify(cxetermcontractor.get_stop_service(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    function.click(cxetermcontractor.get_stop_service_clk(driver))
    function.verify(cxetermcontractor.get_stop_lbl(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    function.verify(cxetermcontractor.get_CAN(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    function.input_text(cxetermcontractor.get_CAN(driver), can)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    function.input_text(cxetermcontractor.get_SIN(driver), sin)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    function.input_text(cxetermcontractor.get_firstname(driver), firstname)
    function.input_text(cxetermcontractor.get_lastname(driver), lastname)
    function.input_text(cxetermcontractor.get_emailaddress(driver), emailaddress)
    function.input_text(cxetermcontractor.get_mobile_number(driver), mobilenumber)
    function.input_text(cxetermcontractor.get_businessname(driver), businessname)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7")
    function.click(cxetermcontractor.get_next1(driver))
    function.verify(cxetermcontractor.get_terms_cond(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7b")



    function.bookmark(serviceAppModule, ts_id, test_case, "Step 8")
    function.click(cxetermcontractor.get_terms_cond(driver))
    time.sleep(15)
    function.verify(cxetermcontractor.get_submit(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 9")
    function.click(cxetermcontractor.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 9")
    #function.verify(cxetermindividual.get_confirmation(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 9b")

    log.info(test_case + " Passed")


def TC121(driver, ts_id, firstname, lastname, emailaddress, mobilenumber, can, sin, designation, companyname, landline):
    test_case = "TC121"
    function = Functions()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_home = CXEApplyHomePage()
    function.verify(cxe_apply_home.get_label_service_application(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1b")

    cxereactivatebusiness = CXEReactivateBusiness()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    function.click(cxereactivatebusiness.get_business(driver))
    function.verify(cxereactivatebusiness.get_start_service(driver))
    function.verify(cxereactivatebusiness.get_modify_service(driver))
    function.verify(cxereactivatebusiness.get_reactivate_service(driver))
    function.verify(cxereactivatebusiness.get_stop_service(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    function.click(cxereactivatebusiness.get_reactivate_service(driver))
    function.verify(cxereactivatebusiness.get_stop_lbl(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    function.verify(cxereactivatebusiness.get_CAN(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    function.input_text(cxereactivatebusiness.get_CAN(driver), can)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    function.input_text(cxereactivatebusiness.get_SIN(driver), sin)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    function.input_text(cxereactivatebusiness.get_firstname(driver), firstname)
    function.input_text(cxereactivatebusiness.get_lastname(driver), lastname)
    function.input_text(cxereactivatebusiness.get_emailaddress(driver), emailaddress)
    function.input_text(cxereactivatebusiness.get_mobile_number(driver), mobilenumber)
    function.input_text(cxereactivatebusiness.get_designation(driver), designation)
    function.input_text(cxereactivatebusiness.get_companyname(driver), companyname)
    function.input_text(cxereactivatebusiness.get_landline(driver), landline)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7")
    function.click(cxereactivatebusiness.get_next1(driver))
    function.verify(cxereactivatebusiness.get_value_add(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7b")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 8")
    function.click(cxereactivatebusiness.get_yes(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8")
    #function.click(cxetermindividual.get_next3(driver))
    function.verify(cxereactivatebusiness.get_terms_cond(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8b")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 9")
    function.click(cxereactivatebusiness.get_terms_cond_clk(driver))
    time.sleep(15)
    function.verify(cxereactivatebusiness.get_submit(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 9")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 10")
    function.click(cxereactivatebusiness.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 10")
    #function.verify(cxetermindividual.get_confirmation(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 10b")

    log.info(test_case + " Passed")

def TC122(driver, ts_id, firstname, lastname, emailaddress, businessname, mobilenumber, can, sin, servadd):
    test_case = "TC122"
    function = Functions()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    function.new_tab(driver, cxe_apply)
    cxe_apply_home = CXEApplyHomePage()
    function.verify(cxe_apply_home.get_label_service_application(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1b")

    cxereactivatecontractor = CXEReactivateContractor()
    function.bookmark(serviceAppModule, ts_id, test_case, "Step 2")

    function.click(cxereactivatecontractor.get_contractor(driver))
    function.verify(cxereactivatecontractor.get_start_service(driver))
    function.verify(cxereactivatecontractor.get_modify_service(driver))
    function.verify(cxereactivatecontractor.get_reactivate_service(driver))
    function.verify(cxereactivatecontractor.get_stop_service(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    function.click(cxereactivatecontractor.get_reactivate_service(driver))
    function.verify(cxereactivatecontractor.get_reactivate_page(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    function.input_text(cxereactivatecontractor.get_firstname(driver), firstname)
    function.input_text(cxereactivatecontractor.get_lastname(driver), lastname)
    function.input_text(cxereactivatecontractor.get_emailaddress(driver), emailaddress)
    function.input_text(cxereactivatecontractor.get_businessname(driver), businessname)
    function.input_text(cxereactivatecontractor.get_mobile_number(driver), mobilenumber)
    #function.input_text(cxereactivatecontractor.get_companyname(driver), companyname)
    #function.input_text(cxereactivatecontractor.get_landline(driver), landline)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")
    function.click(cxereactivatecontractor.get_next1(driver))
    function.verify(cxereactivatecontractor.get_cust_info(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4b")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    function.verify(cxereactivatecontractor.get_CAN(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")


    function.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    function.input_text(cxereactivatecontractor.get_CAN(driver), can)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    function.input_text(cxereactivatecontractor.get_SIN(driver), sin)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 8")
    function.input_text(cxereactivatecontractor.get_firstname_cust(driver), firstname)
    function.input_text(cxereactivatecontractor.get_lastname_cust(driver), lastname)
    function.input_text(cxereactivatecontractor.get_emailaddress_cust(driver), emailaddress)
    function.input_text(cxereactivatecontractor.get_mobile_number_cust(driver), mobilenumber)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8")
    function.click(cxereactivatecontractor.get_next2(driver))
    function.verify(cxereactivatecontractor.get_new_address(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 8b")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 9")
    function.click(cxereactivatecontractor.get_no(driver))
    function.input_text(cxereactivatecontractor.get_serv_add(driver), servadd)
    function.click(cxereactivatecontractor.get_province(driver))
    function.click(cxereactivatecontractor.get_province_val(driver))
    function.click(cxereactivatecontractor.get_city(driver))
    function.click(cxereactivatecontractor.get_city_val(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 9")
    function.click(cxereactivatecontractor.get_next3(driver))

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 10")
    function.click(cxereactivatecontractor.get_terms_cond_clk(driver))
    time.sleep(15)
    function.verify(cxereactivatecontractor.get_submit(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 10")

    function.bookmark(serviceAppModule, ts_id, test_case, "Step 11")
    function.click(cxereactivatecontractor.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 11")
    #function.verify(cxetermindividual.get_confirmation(driver))
    function.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 11b")

    log.info(test_case + " Passed")



def TC108(driver, ts_id):
    test_case = "TC026"
    cxe_apply_home = CXEApplyHomePage()
    cxe_apply_contractor = CXEApplyContractor()
    cxeHome = CXEHomePage()
    cxe_apply_reg = CXEApplyContractorRegPage()
    home = HomePage()
    yopmail_inbox = YopmailInboxPage()
    resetPass = ResetPasswordPage()

    fc.new_tab(driver, cxe_apply)

    time.sleep(5)
    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 1")
    fc.verify(cxe_apply_home.get_label_service_application(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 1")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 2")
    fc.click(cxe_apply_contractor.get_contractor(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 2")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 3")
    fc.click(cxe_apply_contractor.get_contractor_start(driver))
    fc.modal_click(driver, cxe_apply_contractor.get_submit_btn(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 3")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 4")
    fc.scroll_element(driver, cxe_apply_contractor.get_next_button(driver))
    fc.input_text(cxe_apply_contractor.get_first_name(driver), SAMO['contractor_firstName'])
    fc.input_text(cxe_apply_contractor.get_last_name(driver), SAMO['contractor_lastName'])
    fc.input_text(cxe_apply_contractor.get_business_name_cxe_apply(driver), SAMO['contractor_businessName'])
    fc.input_text(cxe_apply_contractor.get_email_address(driver), SAMO['contractor_emailAddress'])
    fc.input_text(cxe_apply_contractor.get_phone_number(driver), SAMO['contractor_mobileNumber'])
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4")
    fc.click(cxe_apply_contractor.get_next_button(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 4b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 5")
    fc.input_text(cxe_apply_contractor.get_firstname_cxe_apply(driver), SAMO['individual_account_first'])
    fc.input_text(cxe_apply_contractor.get_lastname_cxe_apply(driver), SAMO['individual_account_last'])
    fc.input_text(cxe_apply_contractor.get_email_cxe_apply(driver), SAMO['individual_account_email'])
    fc.input_text(cxe_apply_contractor.get_birthday_cxe_apply(driver), SAMO['contractor_birthday'])
    fc.input_text(cxe_apply_contractor.get_mobile_num_cxe_apply(driver), SAMO['individual_account_mobile'])
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5")
    fc.click(cxe_apply_contractor.get_next_btn(driver))
    time.sleep(5)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 5b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 6")
    fc.input_text(cxe_apply_contractor.get_service_add(driver), SAMO['contractor_service_add'])
    fc.select_dropdown_element(cxe_apply_contractor.get_province(driver), SAMO['contractor_province'])
    fc.select_dropdown_element(cxe_apply_contractor.get_city(driver), SAMO['contractor_city'])
    fc.select_dropdown_element(cxe_apply_contractor.get_ownership(driver), SAMO['contractor_ownership'])
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6")
    fc.click(cxe_apply_contractor.get_new_add_next_btn(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 6b")

    fc.bookmark(serviceAppModule, ts_id, test_case, "Step 7")
    fc.click(cxe_apply_contractor.get_terms_conditions(driver))
    time.sleep(15)
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7")
    fc.click(cxe_apply_contractor.get_terms_next_btn(driver))
    fc.screen_capture(driver, serviceAppModule, ts_id, test_case, "Step 7b")
