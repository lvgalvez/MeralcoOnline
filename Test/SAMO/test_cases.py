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
from Pages.Page_CXE_Modification_Contractor import CXEModificationContractor
from Pages.Page_CXE_Account import CXEAccountPage
from Pages.Page_ES_Business import CXEEsBusiness
from Pages.Page_CXE_Terminate_Individual import CXETerminateIndividual
from Pages.Page_CXE_Terminate_Business import CXETerminateBusiness
from Pages.Page_CXE_Terminate_Contractor import CXETerminateContractor
from Pages.Page_CXE_Reactivate_Business import CXEReactivateBusiness
from Utilities.Config import *
from Utilities.Data import SSO
from Utilities.Functions import Functions
from Utilities.Utils import Utilities


log = Utilities().getlogger()
module = "SAMO"


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
    function.screen_capture(driver, module, ts_id, test_case, "Step ")

    pageservice = PageService()

    function.bookmark(module, ts_id, test_case, "Step 3")
    function.input_text(pageservice.get_birthday(driver), birthday)
    function.click(pageservice.get_click_next(driver))
    function.verify(pageservice.get_label_serv_add(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3")

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
    function.click(pageservice.get_next(driver))
    function.verify(pageservice.get_value_added(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 4")

    function.bookmark(module, ts_id, test_case, "Step 5")
    function.click(pageservice.get_automatic_payment(driver))
    #function.click(pageservice.get_attach_docu(driver)) #upload file to be follow
    function.click(pageservice.get_clk_next_2(driver))
    function.verify(pageservice.get_term_condition(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 5")

    function.bookmark(module, ts_id, test_case, "Step 6")
    function.click(pageservice.get_click_term_condition(driver))
    #function.click(pageservice.get_iam_not_robot(driver)) #for manual only
    time.sleep(20)
    function.click(pageservice.get_submit(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 6")
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

def TC007(driver, ts_id, email, password, serviceaddress):
    test_case = "TC007"
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
    function.click(cxe_account.get_change_contract_details(driver))
    time.sleep(3)
    function.verify(cxe_account.get_request(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3")

    esbusiness = CXEEsBusiness()
    function.bookmark(module, ts_id, test_case, "Step 4")
    function.click(esbusiness.get_change_contract_name(driver))
    function.click(esbusiness.get_next2(driver))
    function.verify(esbusiness.get_value_added(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 4")

    function.bookmark(module, ts_id, test_case, "Step 5")
    function.click(esbusiness.get_radio_yes(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 5")
    function.click(esbusiness.get_next(driver))

    function.bookmark(module, ts_id, test_case, "Step 6")
    function.click(esbusiness.get_click_term_condition(driver))
    time.sleep(20)
    function.verify(esbusiness.get_submit(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 6")

    function.bookmark(module, ts_id, test_case, "Step 7")
    function.click(esbusiness.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, module, ts_id, test_case, "Step 7")

    log.info(test_case + " Passed")

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
    function.input_text(cxemodifycontractor.get_company_name(driver), companyname)
    function.input_text(cxemodifycontractor.get_landline(driver), landline)
    function.input_text(cxemodifycontractor.get_first_name(driver), firstname)
    function.input_text(cxemodifycontractor.get_last_name(driver), lastname)
    function.input_text(cxemodifycontractor.get_emailaddress(driver), emailaddress)
    function.input_text(cxemodifycontractor.get_mobile_number(driver), mobilenumber)
    function.input_text(cxemodifycontractor.get_designation(driver), designation)
    function.screen_capture(driver, module, ts_id, test_case, "Step 7")
    function.click(cxemodifycontractor.get_next1(driver))
    function.verify(cxemodifycontractor.get_contact_info(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 7b")

    function.bookmark(module, ts_id, test_case, "Step 8")
    function.click(cxemodifycontractor.get_yes(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 8")
    function.click(cxemodifycontractor.get_next3(driver))
    function.verify(cxemodifycontractor.get_terms_condition(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 8b")

    function.bookmark(module, ts_id, test_case, "Step 10")
    function.click(cxemodifycontractor.get_click_term_condition(driver))
    time.sleep(10)
    function.verify(cxemodifycontractor.get_submit(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 10")

    function.bookmark(module, ts_id, test_case, "Step 11")
    function.click(cxemodifycontractor.get_submit(driver))
    time.sleep(8)
    function.screen_capture(driver, module, ts_id, test_case, "Step 11")
    function.verify(cxemodifycontractor.get_confirmation(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 11b")

    log.info(test_case + " Passed")


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










