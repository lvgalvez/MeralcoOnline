import time
from Pages.Page_CXE_Case import CXECasePage
from Pages.Page_CXE_Apply_Home import CXEApplyHomePage
from Pages.Page_CXE_New_Case import CXENewCasePage
from Pages.Page_CXE_New_Case_Recontract import CXENewCaseRecontractPage
from Pages.Page_CXE_New_Case_Termination import CXENewCaseTerminationPage
from Pages.Page_CXE_Terminate_Individual import CXETerminateIndividual
from Pages.Page_CXE_Customer_Document import CXECustomerDocumentPage
from Pages.Page_CXE_Document import CXEDocumentPage
from Pages.Page_CXE_Home import CXEHomePage
from Pages.Page_CXE_Page_Search import CXESearchPage
from Pages.Page_CXE_Question_Response import CXEQuestionResponsePage
from Pages.Page_CXE_Question_Responses import CXEQuestionResponsesPage
from Pages.Page_CXE_Account import CXEAccountPage
from Pages.Page_Paperless_Billing import PaperlessBillingPage
from Pages.Page_Service import PageService
from Pages.Page_ConcernStatus import ConcernStatusPage
from Pages.Page_Home import HomePage
from Pages.Page_ContactUs import ContactUsPage
from Test.Module_Functions.CXE_Functions import *
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
cxe_home = CXEHomePage()
new_case = CXENewCasePage()
new_case_termination = CXENewCaseTerminationPage()
new_case_recontract = CXENewCaseRecontractPage()
paperless_billing = PaperlessBillingPage()


def Precondition_Login_CXE(driver, ts_id, cxe_email, cxe_password):
    Log_in_CXE(driver, cxe_email, cxe_password)


def TC001(driver, ts_id, page):
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


def TC079(driver, ts_id, username, password):
    test_case = "TC079"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, username, password)
    fc.scroll_element(driver, home.get_bayadexpress_here(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.page_down(driver, 1)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")


def TC080(driver, ts_id, username, password):
    test_case = "TC079"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, username, password)
    fc.scroll_element(driver, home.get_paperless_billing(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(home.get_paperless_billing(driver))
    fc.verify(paperless_billing.get_paperless_billing(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")



def TC087(driver, ts_id):
    test_case = "TC087"
    home = HomePage()
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.scroll_element(driver, home.get_activity_tracker(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(home.get_activity_tracker(driver))

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")


def TC088a(driver, ts_id, can, sin):
    test_case = "TC088"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_navigation_menu(driver))
    fc.click(cxe_home.get_navigation_cases(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_modification_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(new_case.get_can(driver), can)
    fc.input_text(new_case.get_sin(driver), sin)
    fc.click(new_case.get_sin(driver))
    fc.arrow_down(new_case.get_sin(driver))
    fc.arrow_down(new_case.get_sin(driver))
    fc.enter(new_case.get_sin(driver))
    fc.modal_click(driver, new_case.get_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(new_case.get_change_name(driver))
    fc.click(new_case.get_move_chosen(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(new_case.get_case_origin(driver))
    fc.click(new_case.get_origin_kiosk(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3b")
    fc.click(new_case.get_energization_date(driver))
    fc.click(new_case.get_energization_today(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3c")
    fc.click(new_case.get_case_save(driver))
    fc.scroll_element(driver, new_case.get_can_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3d")
    fc.click(new_case.get_close_modification(driver))


def TC088b(driver, ts_id, can):
    test_case = "TC088"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_termination_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(new_case_termination.get_can(driver), can)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(new_case_termination.get_case_origin(driver))
    fc.click(new_case_termination.get_origin_kiosk(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(new_case_termination.get_case_save(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3b")
    fc.click(new_case_termination.get_close_termination(driver))


def TC088c(driver, ts_id, can):
    test_case = "TC088"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_recontract_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(new_case_recontract.get_sin(driver), can)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(new_case_recontract.get_case_origin(driver))
    fc.click(new_case_recontract.get_origin_kiosk(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(new_case.get_energization_date(driver))
    fc.click(new_case.get_energization_today(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3b")
    fc.click(new_case_recontract.get_case_save(driver))
    fc.scroll_element(driver, new_case_recontract.get_can(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3c")
    fc.click(new_case_recontract.get_close_recontract(driver))



def TC089a(driver, ts_id, can, sin):
    test_case = "TC089"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_modification_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(new_case.get_can(driver), can)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.input_text(new_case.get_sin(driver), sin)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.bookmark(module, ts_id, test_case, "Step 4")
    fc.click(new_case.get_change_name(driver))
    fc.click(new_case.get_move_chosen(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")
    fc.click(new_case.get_case_origin(driver))
    fc.click(new_case.get_origin_kiosk(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4b")
    fc.click(new_case.get_energization_date(driver))
    fc.click(new_case.get_energization_today(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4c")
    fc.click(new_case.get_case_save(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4d")
    fc.click(new_case.get_close_modification(driver))


def TC089b(driver, ts_id, can, sin):
    test_case = "TC089"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_termination_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(new_case_termination.get_can(driver), can)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.input_text(new_case_termination.get_sin(driver), sin)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.bookmark(module, ts_id, test_case, "Step 4")
    fc.click(new_case_termination.get_case_origin(driver))
    fc.click(new_case_termination.get_origin_kiosk(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")
    fc.click(new_case_termination.get_case_save(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4b")
    fc.click(new_case_termination.get_close_termination(driver))


def TC089c(driver, ts_id, can, sin):
    test_case = "TC089"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_recontract_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(new_case_recontract.get_can(driver), can)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.input_text(new_case_recontract.get_sin(driver), sin)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.bookmark(module, ts_id, test_case, "Step 4")
    fc.click(new_case_recontract.get_case_origin(driver))
    fc.click(new_case_recontract.get_origin_kiosk(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")
    fc.click(new_case.get_energization_date(driver))
    fc.click(new_case.get_energization_today(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4b")
    fc.click(new_case_recontract.get_case_save(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4c")
    fc.click(new_case_recontract.get_close_recontract(driver))


def TC090(driver, ts_id):
    test_case = "TC090"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_navigation_menu(driver))
    fc.click(cxe_home.get_navigation_cases(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_modification_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(new_case.get_change_name(driver))
    fc.click(new_case.get_move_chosen(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(new_case.get_case_origin(driver))
    fc.click(new_case.get_origin_kiosk(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3b")
    fc.click(new_case.get_energization_date(driver))
    fc.click(new_case.get_energization_today(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3c")
    fc.click(new_case.get_case_save(driver))
    fc.scroll_element(driver, new_case.get_can_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3d")
    fc.click(new_case.get_close_modification(driver))


def TC090b(driver, ts_id):
    test_case = "TC090"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_navigation_menu(driver))
    fc.click(cxe_home.get_navigation_cases(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_termination_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(new_case_termination.get_case_origin(driver))
    fc.click(new_case_termination.get_origin_kiosk(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(new_case_termination.get_case_save(driver))
    fc.scroll_element(driver, new_case_termination.get_can_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3b")
    fc.click(new_case_termination.get_close_termination(driver))


def TC090c(driver, ts_id):
    test_case = "TC090"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_navigation_menu(driver))
    fc.click(cxe_home.get_navigation_cases(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_recontract_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(new_case_recontract.get_case_origin(driver))
    fc.click(new_case_recontract.get_origin_kiosk(driver))
    fc.click(new_case.get_energization_date(driver))
    fc.click(new_case.get_energization_today(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(new_case_recontract.get_case_save(driver))
    fc.scroll_element(driver, new_case_recontract.get_sin(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3b")
    fc.scroll_element(driver, new_case_recontract.get_text_reconnect(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3c")
    fc.click(new_case_recontract.get_close_recontract(driver))


def TC091(driver, ts_id, can):
    test_case = "TC091"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_modification_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(new_case.get_can(driver), can)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(new_case.get_change_name(driver))
    fc.click(new_case.get_move_chosen(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(new_case.get_case_origin(driver))
    fc.click(new_case.get_origin_kiosk(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3b")
    fc.click(new_case.get_energization_date(driver))
    fc.click(new_case.get_energization_today(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3c")
    fc.click(new_case.get_case_save(driver))
    fc.scroll_element(driver, new_case.get_can_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3d")
    fc.click(new_case.get_close_modification(driver))


def TC091b(driver, ts_id, can):
    test_case = "TC091"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_termination_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(new_case_termination.get_can(driver), can)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(new_case_termination.get_case_origin(driver))
    fc.click(new_case_termination.get_origin_kiosk(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(new_case_termination.get_case_save(driver))
    fc.scroll_element(driver, new_case_termination.get_can_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3b")
    fc.click(new_case_termination.get_close_termination(driver))


def TC091c(driver, ts_id, can):
    test_case = "TC091"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_recontract_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(new_case_recontract.get_sin(driver), can)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(new_case_recontract.get_case_origin(driver))
    fc.click(new_case_recontract.get_origin_kiosk(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(new_case.get_energization_date(driver))
    fc.click(new_case.get_energization_today(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3b")
    fc.click(new_case_recontract.get_case_save(driver))
    fc.scroll_element(driver, new_case_recontract.get_sin(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3c")
    fc.scroll_element(driver, new_case_recontract.get_text_reconnect(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3d")
    fc.click(new_case_recontract.get_close_recontract(driver))


def TC092(driver, ts_id, can):
    test_case = "TC092"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_modification_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(new_case.get_can(driver), can)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(new_case.get_change_name(driver))
    fc.click(new_case.get_move_chosen(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(new_case.get_case_origin(driver))
    fc.click(new_case.get_origin_kiosk(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3b")
    fc.click(new_case.get_energization_date(driver))
    fc.click(new_case.get_energization_today(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3c")
    fc.click(new_case.get_case_save(driver))
    fc.scroll_element(driver, new_case.get_can_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3d")
    fc.click(new_case.get_close_modification(driver))


def TC092b(driver, ts_id, can):
    test_case = "TC092"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_termination_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(new_case_termination.get_can(driver), can)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(new_case_termination.get_case_origin(driver))
    fc.click(new_case_termination.get_origin_kiosk(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(new_case_termination.get_case_save(driver))
    fc.scroll_element(driver, new_case_termination.get_can_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3b")
    fc.click(new_case_termination.get_close_termination(driver))


def TC092c(driver, ts_id, can):
    test_case = "TC092"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_recontract_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(new_case_recontract.get_sin(driver), can)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(new_case_recontract.get_case_origin(driver))
    fc.click(new_case_recontract.get_origin_kiosk(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(new_case.get_energization_date(driver))
    fc.click(new_case.get_energization_today(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3b")
    fc.click(new_case_recontract.get_case_save(driver))
    fc.scroll_element(driver, new_case_recontract.get_sin(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3c")
    fc.scroll_element(driver, new_case_recontract.get_text_reconnect(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3d")
    fc.scroll_element(driver, new_case_recontract.get_text_reconnect(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3e")
    fc.click(new_case_recontract.get_close_recontract(driver))


def TC093(driver, ts_id, can):
    test_case = "TC093"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_modification_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(new_case.get_can(driver), can)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(new_case.get_change_name(driver))
    fc.click(new_case.get_move_chosen(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(new_case.get_case_origin(driver))
    fc.click(new_case.get_origin_kiosk(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3b")
    fc.click(new_case.get_energization_date(driver))
    fc.click(new_case.get_energization_today(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3c")
    fc.click(new_case.get_case_save(driver))
    fc.scroll_element(driver, new_case.get_can_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3d")
    fc.click(new_case.get_close_modification(driver))


def TC093b(driver, ts_id, can):
    test_case = "TC093"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_termination_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(new_case_termination.get_can(driver), can)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(new_case_termination.get_case_origin(driver))
    fc.click(new_case_termination.get_origin_kiosk(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(new_case_termination.get_case_save(driver))
    fc.scroll_element(driver, new_case_termination.get_can_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3b")
    fc.click(new_case_termination.get_close_termination(driver))


def TC093c(driver, ts_id, can):
    test_case = "TC093"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_recontract_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(new_case_recontract.get_sin(driver), can)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(new_case_recontract.get_case_origin(driver))
    fc.click(new_case_recontract.get_origin_kiosk(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(new_case.get_energization_date(driver))
    fc.click(new_case.get_energization_today(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3b")
    fc.click(new_case_recontract.get_case_save(driver))
    fc.scroll_element(driver, new_case_recontract.get_sin(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3c")
    fc.scroll_element(driver, new_case_recontract.get_text_reconnect(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3d")
    fc.click(new_case_recontract.get_close_recontract(driver))


def TC094(driver, ts_id, can):
    test_case = "TC094"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_modification_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(new_case.get_can(driver), can)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(new_case.get_change_name(driver))
    fc.click(new_case.get_move_chosen(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(new_case.get_case_origin(driver))
    fc.click(new_case.get_origin_kiosk(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3b")
    fc.click(new_case.get_energization_date(driver))
    fc.click(new_case.get_energization_today(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3c")
    fc.click(new_case.get_case_save(driver))
    fc.scroll_element(driver, new_case.get_can_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3d")
    fc.click(new_case.get_close_modification(driver))


def TC094b(driver, ts_id, can):
    test_case = "TC094"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_termination_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(new_case_termination.get_can(driver), can)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(new_case_termination.get_case_origin(driver))
    fc.click(new_case_termination.get_origin_kiosk(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(new_case_termination.get_case_save(driver))
    fc.scroll_element(driver, new_case_termination.get_can_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3b")
    fc.click(new_case_termination.get_close_termination(driver))


def TC094c(driver, ts_id, can):
    test_case = "TC094"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_recontract_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(new_case_recontract.get_sin(driver), can)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(new_case_recontract.get_case_origin(driver))
    fc.click(new_case_recontract.get_origin_kiosk(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(new_case.get_energization_date(driver))
    fc.click(new_case.get_energization_today(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3b")
    fc.click(new_case_recontract.get_case_save(driver))
    fc.scroll_element(driver, new_case_recontract.get_sin(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3c")
    fc.scroll_element(driver, new_case_recontract.get_text_reconnect(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3d")
    fc.click(new_case_recontract.get_close_recontract(driver))


def TC095(driver, ts_id, can, sin):
    test_case = "TC095"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_modification_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(new_case.get_can(driver), can)
    fc.input_text(new_case.get_sin(driver), sin)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(new_case.get_change_name(driver))
    fc.click(new_case.get_move_chosen(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(new_case.get_case_origin(driver))
    fc.click(new_case.get_origin_kiosk(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3b")
    fc.click(new_case.get_energization_date(driver))
    fc.click(new_case.get_energization_today(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3c")
    fc.click(new_case.get_case_save(driver))
    fc.scroll_element(driver, new_case.get_can_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3d")
    fc.click(new_case.get_close_modification(driver))
    time.sleep(10)
    fc.click(cxe_home.get_navigation_menu(driver))
    fc.click(cxe_home.get_navigation_home(driver))
    fc.click(cxe_home.get_search_button(driver))
    fc.input_text(cxe_home.get_search_input(driver), can)
    time.sleep(5)
    fc.click(cxe_home.get_suggestion_case(driver))
    fc.verify(cxe_cases.get_cases_text(driver))


def TC095b(driver, ts_id, can, sin):
    test_case = "TC095"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_termination_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(new_case_termination.get_can(driver), can)
    fc.input_text(new_case_termination.get_sin(driver), sin)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(new_case_termination.get_case_origin(driver))
    fc.click(new_case_termination.get_origin_kiosk(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(new_case_termination.get_case_save(driver))
    fc.scroll_element(driver, new_case_termination.get_can_text(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3b")
    fc.click(new_case_termination.get_close_termination(driver))


def TC095c(driver, ts_id, can, sin):
    test_case = "TC095"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(cxe_home.get_case_new(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    fc.click(new_case.get_recontract_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    fc.click(new_case.get_next(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(new_case_recontract.get_can(driver), can)
    fc.input_text(new_case_recontract.get_sin(driver), sin)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.click(new_case_recontract.get_case_origin(driver))
    fc.click(new_case_recontract.get_origin_kiosk(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(new_case.get_energization_date(driver))
    fc.click(new_case.get_energization_today(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3b")
    fc.click(new_case_recontract.get_case_save(driver))
    fc.scroll_element(driver, new_case_recontract.get_sin(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3c")
    fc.scroll_element(driver, new_case_recontract.get_text_reconnect(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3d")
    fc.click(new_case_recontract.get_close_recontract(driver))

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
