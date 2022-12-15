import time
from Pages.Page_CXE_Case import CXECasePage
from Pages.Page_CXE_Apply_Home import CXEApplyHomePage
from Pages.Page_CXE_Terminate_Individual import CXETerminateIndividual
from Pages.Page_CXE_Customer_Document import CXECustomerDocumentPage
from Pages.Page_CXE_Document import CXEDocumentPage
from Pages.Page_CXE_Home import CXEHomePage
from Pages.Page_CXE_Page_Search import CXESearchPage
from Pages.Page_CXE_Question_Response import CXEQuestionResponsePage
from Pages.Page_CXE_Question_Responses import CXEQuestionResponsesPage
from Pages.Page_CXE_Account import CXEAccountPage
from Pages.Page_Service import PageService
from Pages.Page_Manage_Accounts import ManageAccountsPage
from Pages.Page_Yopmail_Home import YopmailHomePage
from Pages.Page_ConcernStatus import ConcernStatusPage
from Pages.Page_Home import HomePage
from Pages.Page_ContactUs import ContactUsPage
from Test.Module_Functions.MO_Functions import *
from Utilities.Functions import *
from Utilities.Utils import Utilities
from Pages.Page_Yopmail_Home import YopmailHomePage
from Utilities.Config import *
from selenium.common import exceptions


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
yopmail_home = YopmailHomePage()
document = CXEDocumentPage()
module = "Release5"
inquiry_reference_no = ''

def TC001(driver,ts_id, page):
    test_case = "TC001"
    homePage = HomePage()
    contactUsPage = ContactUsPage()

    Log_In_Meralco_Online(driver, Concern['username_single_service'], Concern['password'])

    time.sleep(10)
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.modal_click(driver, homePage.get_contact_us(driver))
    # homePage.get_contact_us(driver).click()

    if page == 'Inquiry':
        fc.click(contactUsPage.get_log_inquiry(driver))
    elif page == 'Feedback':
        fc.click((contactUsPage.get_give_feedback(driver)))
    elif page == 'Request':
        fc.click((contactUsPage.get_request(driver)))

    fc.scroll_element(driver, contactUsPage.get_log_remarks(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

def TC001a(driver,ts_id):
    test_case = "TC001"
    contactUsPage = ContactUsPage()
    time.sleep(10)
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.verify(contactUsPage.get_CAN(driver))
    #fc.scroll_element(driver, contactUsPage.get_log_remarks(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")



def TC002(driver, ts_id, page):
    test_case = "TC002"
    contactUsPage = ContactUsPage()
    homePage = HomePage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, Concern['username_multiple_can'], Concern['password'])
    time.sleep(10)
    fc.modal_click(driver, homePage.get_contact_us(driver))

    if page == 'Inquiry':
        fc.click(contactUsPage.get_log_inquiry(driver))
    elif page == 'Feedback':
        fc.click(contactUsPage.get_give_feedback(driver))
    elif page == "Request":
        fc.click(contactUsPage.get_request(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.select_dropdown_element(contactUsPage.get_can(driver), Concern['change_selected_can'])
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")


def TC003(driver, ts_id, page):
    test_case = "TC003"
    contactUsPage = ContactUsPage()
    homePage = HomePage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, Concern['username_multiple_service'], Concern['password'])
    time.sleep(10)
    fc.modal_click(driver, homePage.get_contact_us(driver))

    if page == 'Inquiry':
        fc.click(contactUsPage.get_log_inquiry(driver))
    elif page == 'Feedback':
        fc.click(contactUsPage.get_give_feedback(driver))
    elif page == "Request":
        fc.click(contactUsPage.get_request(driver))

    fc.select_dropdown_element(contactUsPage.get_sin(driver), Concern['change_selected_sin'])
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

def TC003a(driver, ts_id, can):
    test_case = "TC003"
    contactUsPage = ContactUsPage()
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.input_text(contactUsPage.get_CAN(driver), can)
    fc.verify(contactUsPage.get_CAN(driver))
    fc.verify(contactUsPage.get_concern_sn(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

def TC004(driver, ts_id, page):
    test_case = "TC004"
    contactUsPage = ContactUsPage()
    homePage = HomePage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, Concern['username_multiple_can_multiple_sin'], Concern['password'])
    time.sleep(10)
    fc.modal_click(driver, homePage.get_contact_us(driver))

    if page == 'Inquiry':
        fc.click(contactUsPage.get_log_inquiry(driver))
    elif page == 'Feedback':
        fc.click(contactUsPage.get_give_feedback(driver))
    elif page == "Request":
        fc.click(contactUsPage.get_request(driver))

    time.sleep(10)
    fc.select_dropdown_element(contactUsPage.get_can(driver), Concern['selected_multiple_can'])
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.select_dropdown_element(contactUsPage.get_sin(driver), Concern['selected_multiple_sin'])
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")



def TC005(driver, ts_id, page):
    test_case = "TC005"
    contactUsPage = ContactUsPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")

    if page == 'Inquiry':
        fc.select_dropdown_element(contactUsPage.get_log_inquiry_concern_type(driver),
                                   Concern['inquiry_concern_type'])
    elif page == 'Feedback':
        fc.select_dropdown_element(contactUsPage.get_log_inquiry_concern_type(driver),
                                   Concern['feedback_concern_type'])
    elif page == "Request":
        fc.select_dropdown_element(contactUsPage.get_log_inquiry_concern_type(driver),
                                   Concern['request_concern_type'])

    contactUsPage.enter_remarks(driver,Concern['remarks'])
    fc.scroll_element(driver, contactUsPage.get_submit(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(contactUsPage.get_submit(driver))

    if page == 'Inquiry':
        fc.scroll_element(driver, contactUsPage.get_top_page(driver, 'Log an Inquiry'))
    elif page == 'Feedback':
        fc.scroll_element(driver, contactUsPage.get_top_page(driver, 'Give Feedback'))
    elif page == "Request":
        fc.scroll_element(driver, contactUsPage.get_top_page(driver, 'Make a Request'))


    inquiry_reference_no = contactUsPage.get_log_inquiry_reference_number(driver)
    time.sleep(5)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC005a(driver, ts_id, can, firstname, lastname, emailaddress, mobilenumber, remarks):
    test_case = "TC005"
    contactUsPage = ContactUsPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.select_dropdown_element(contactUsPage.get_log_inquiry_concern_type(driver),
                               Concern['inquiry_concern_type'])
    fc.input_text(contactUsPage.get_CAN(driver), can)
    fc.input_text(contactUsPage.get_firstname(driver), firstname)
    fc.input_text(contactUsPage.get_lastname(driver), lastname)
    fc.input_text(contactUsPage.get_email(driver), emailaddress)
    fc.input_text(contactUsPage.get_mobile(driver), mobilenumber)
    fc.input_text(contactUsPage.get_remarks(driver), remarks)
    fc.input_text(contactUsPage.get_remarks(driver), remarks)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(contactUsPage.get_submit(driver))


    inquiry_reference_no = contactUsPage.get_log_inquiry_reference_number(driver)
    time.sleep(5)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC005b(driver, ts_id, can, sin, firstname, lastname, emailaddress, mobilenumber, remarks):
    test_case = "TC005"
    contactUsPage = ContactUsPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.select_dropdown_element(contactUsPage.get_log_inquiry_concern_type(driver),
                               Concern['inquiry_concern_type'])
    fc.input_text(contactUsPage.get_CAN(driver), can)
    fc.input_text(contactUsPage.get_concern_sn(driver), sin)
    fc.input_text(contactUsPage.get_firstname(driver), firstname)
    fc.input_text(contactUsPage.get_lastname(driver), lastname)
    fc.input_text(contactUsPage.get_email(driver), emailaddress)
    fc.input_text(contactUsPage.get_mobile(driver), mobilenumber)
    fc.input_text(contactUsPage.get_remarks(driver), remarks)
    fc.input_text(contactUsPage.get_remarks(driver), remarks)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(contactUsPage.get_submit(driver))


    inquiry_reference_no = contactUsPage.get_log_inquiry_reference_number(driver)
    time.sleep(5)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC006(driver, ts_id):
    test_case = "TC006"
    contactUsPage = ContactUsPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.scroll_element(driver, contactUsPage.get_ok_btn(driver))
    fc.click(contactUsPage.get_ok_btn(driver))
    time.sleep(5)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    # insert Assert for validation
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC007(driver, ts_id, page):
    test_case = "TC007"
    contactUsPage = ContactUsPage()
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, "https://fuat-meralco.cs73.force.com/customers/s/contact")
    if page == 'Inquiry':
        fc.click(contactUsPage.get_log_inquiry(driver))
    elif page == 'Feedback':
        fc.click(contactUsPage.get_give_feedback(driver))
    elif page == "Request":
        fc.click(contactUsPage.get_make_request(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

def TC012(driver, ts_id):
    test_case = "TC012"
    home = HomePage()
    cxeHome = CXEHomePage()
    service = PageService()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, Concern['username_multiple_can_multiple_sin'], Concern['password'])
    time.sleep(10)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.scroll_element(driver, home.get_request_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.click(home.get_request_service(driver))
    time.sleep(10)

    #fc.modal_click(driver, cxeHome.get_peccbm_no(driver))

    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.input_text(service.get_birthday(driver), Concern['birthday'])
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(service.get_click_next(driver))

    time.sleep(5)
    fc.bookmark(module, ts_id, test_case, "Step 4")
    fc.input_text(service.get_inp_serv_add(driver), Concern['service_address'])
    fc.select_dropdown_element(service.get_province(driver), Concern['province'])
    fc.select_dropdown_element(service.get_city(driver), Concern['city'])
    fc.select_dropdown_element(service.get_ownership(driver), Concern['home_ownership'])
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")
    fc.click(service.get_clk_next_btn(driver))
    time.sleep(5)

    fc.bookmark(module, ts_id, test_case, "Step 5")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")
    fc.click(service.get_clk_next_btn(driver))
    time.sleep(5)

    fc.bookmark(module, ts_id, test_case, "Step 6")
    element = service.get_terms_and_conditions(driver)
    fc.scroll_element(driver, service.get_submit_btn(driver))
    driver.execute_script("arguments[0].click();", element)
    #iamnotRobot
    time.sleep(10)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 6")

    fc.click(service.get_submit_btn(driver))

    fc.bookmark(module, ts_id, test_case, "Step 7")
    fc.click(service.get_ok_btn(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 7")

def TC013(driver, ts_id):
    test_case = "TC013"
    home = HomePage()
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.scroll_element(driver, home.get_activity_tracker(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(home.get_activity_tracker(driver))

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC014(driver, ts_id, email):
    test_case = "TC014"
    contactUsPage = ContactUsPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, yopmail)
    fc.input_text(yopmail_home.get_email(driver), email)
    fc.click(yopmail_home.get_check_inbox(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    #insert Assert for validation

def TC020(driver, ts_id):
    test_case = "TC020"
    home = HomePage()
    account = ManageAccountsPage()
    service = PageService()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, Concern['username_single_service'], Concern['password'])
    time.sleep(10)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.modal_click(driver, home.get_accounts(driver))
    fc.modal_click(driver, home.get_manage_accounts(driver))
    time.sleep(5)

    fc.scroll_element(driver, account.get_change_service(driver))
    fc.click(account.get_change_service(driver))
    time.sleep(5)

    fc.click(service.get_clk_next_btn(driver))
    time.sleep(5)

    #fc.click(service.get_no_radio_btn_peccbm(driver))
    #fc.click(service.get_clk_next_btn(driver))

    time.sleep(5)
    #fc.click(service.get_terms_and_conditions(driver))
    element = service.get_terms_and_conditions_service_details(driver)
    fc.scroll_element(driver, element)
    driver.execute_script("arguments[0].click();", element)
    #iamrobot
    fc.scroll_element(driver, service.get_submit_btn(driver))
    time.sleep(10)
    fc.click(service.get_submit_btn(driver))

def TC021(driver, ts_id):
    test_case = "TC021"
    home = HomePage()
    account = ManageAccountsPage()
    service = PageService()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, Concern['username_single_service'], Concern['password'])
    time.sleep(10)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.modal_click(driver, home.get_accounts(driver))
    fc.modal_click(driver, home.get_manage_accounts(driver))
    time.sleep(5)

    fc.scroll_element(driver, account.get_change_contract(driver))
    fc.click(account.get_change_contract(driver))
    time.sleep(5)

    fc.click(service.get_change_contract_radio_btn(driver))
    fc.scroll_element(driver, service.get_clk_next_btn(driver))
    fc.click(service.get_clk_next_btn(driver))
    time.sleep(5)

    #fc.click(service.get_clk_next_btn(driver))

    #time.sleep(5)

    element = service.get_terms_and_conditions_contract_details(driver)
    fc.scroll_element(driver, element)
    driver.execute_script("arguments[0].click();", element)
    # iamrobot
    fc.scroll_element(driver, service.get_submit_btn(driver))
    time.sleep(10)
    fc.click(service.get_submit_btn(driver))

def TC022(driver, ts_id):
    test_case = "TC022"
    home = HomePage()
    account = ManageAccountsPage()
    service = PageService()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, Concern['username_single_service'], Concern['password'])
    time.sleep(10)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.modal_click(driver, home.get_accounts(driver))
    fc.modal_click(driver, home.get_manage_accounts(driver))
    time.sleep(10)

    fc.scroll_element(driver, account.get_change_contract(driver))
    fc.click(account.get_change_contract(driver))

    fc.click(service.get_transfer_service(driver))
    fc.scroll_element(driver, service.get_clk_next_btn(driver))
    fc.click(service.get_clk_next_btn(driver))
    time.sleep(2)
    fc.scroll_element(driver, home.get_search(driver))
    time.sleep(2)
    fc.scroll_element(driver, service.get_clk_next_btn(driver))
    fc.click(service.get_clk_next_btn(driver))

def TC023(driver, ts_id):
    test_case = "TC023"
    home = HomePage()
    account = ManageAccountsPage()
    service = PageService()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, Concern['username_single_service'], Concern['password'])
    time.sleep(10)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.modal_click(driver, home.get_accounts(driver))
    fc.modal_click(driver, home.get_manage_accounts(driver))
    time.sleep(10)

    fc.scroll_element(driver, account.get_stop_service(driver))
    fc.click(account.get_stop_service(driver))
    time.sleep(20)

    fc.click(service.get_next_button(driver))

def TC024(driver, ts_id):
    test_case = "TC024"
    home = HomePage()
    account = ManageAccountsPage()
    service = PageService()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, Concern['username_single_service'], Concern['password'])
    time.sleep(10)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.modal_click(driver, home.get_accounts(driver))
    fc.modal_click(driver, home.get_manage_accounts(driver))
    time.sleep(10)

    fc.scroll_element(driver, account.get_reactivate_service(driver))
    fc.click(account.get_reactivate_service(driver))

    time.sleep(5)
    fc.click(service.get_next_button(driver))


def TC036(driver, ts_id):
    test_case = "TC036"
    homePage = HomePage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, Concern['username_multiple_service'], Concern['password'])
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC037(driver, ts_id):
    test_case = "TC037"
    homePage = HomePage()
    cxehome = CXEHomePage()
    account = CXEAccountPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, Concern['username_multiple_service'], Concern['password'])
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(cxehome.get_account_details(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(account.get_submit_account(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

def TC038(driver, ts_id):
    test_case = "TC038"
    homePage = HomePage()
    cxehome = CXEHomePage()
    account = CXEAccountPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, Concern['username_multiple_service'], Concern['password'])
    fc.click(cxehome.get_payment_history(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC087(driver, ts_id):
    test_case = "TC087"
    home = HomePage()
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.scroll_element(driver, home.get_activity_tracker(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(home.get_activity_tracker(driver))

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")


def TC110(driver, ts_id, referencenumber, lastname):
    test_case = "TC110"
    concernstatus = ConcernStatusPage()
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, "https://fuat-meralco.cs73.force.com/customers/s/concernstatus")
    fc.input_text(concernstatus.get_log_inquiry_reference_number(driver), referencenumber)
    fc.input_text(concernstatus.get_lastname(driver), lastname)
    fc.click(concernstatus.get_log_inquiry_submit(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

def TC111(driver, ts_id, email):
    test_case = "TC111"
    contactUsPage = ContactUsPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, yopmail)
    fc.input_text(yopmail_home.get_email(driver), email)
    fc.click(yopmail_home.get_check_inbox(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.scroll_element(driver, contactUsPage.get_ok_btn(driver))
    fc.click(contactUsPage.get_ok_btn(driver))
    time.sleep(5)
    #insert Assert for validation
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

def TC111a(driver, ts_id, email):
    test_case = "TC111"
    contactUsPage = ContactUsPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, yopmail)
    fc.input_text(yopmail_home.get_email(driver), email)
    fc.click(yopmail_home.get_check_inbox(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    #insert Assert for validation

def TC118(driver, ts_id, firstname, lastname, emailaddress, mobilenumber, can, sin):
    test_case = "TC118"
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
    function.input_text(cxetermindividual.get_SIN(driver), sin)
    function.screen_capture(driver, module, ts_id, test_case, "Step 6")


    function.bookmark(module, ts_id, test_case, "Step 7")
    function.input_text(cxetermindividual.get_firstname(driver), firstname)
    function.input_text(cxetermindividual.get_lastname(driver), lastname)
    function.input_text(cxetermindividual.get_emailaddress(driver), emailaddress)
    function.input_text(cxetermindividual.get_mobile_number(driver), mobilenumber)
    function.screen_capture(driver, module, ts_id, test_case, "Step 7")
    function.click(cxetermindividual.get_next1(driver))
    function.verify(cxetermindividual.get_terms_cond(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 7")

    function.bookmark(module, ts_id, test_case, "Step 8")
    function.click(cxetermindividual.get_yes(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 8")
    #function.click(cxetermindividual.get_next3(driver))
    function.verify(cxetermindividual.get_terms_cond(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 8")

    function.bookmark(module, ts_id, test_case, "Step 9")
    function.click(cxetermindividual.get_terms_cond(driver))
    time.sleep(15)
    #function.verify(cxetermindividual.get_submit(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 9")

    log.info(test_case + " Passed")
