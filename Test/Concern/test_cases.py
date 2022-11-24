import time
from Pages.Page_CXE_Case import CXECasePage
from Pages.Page_CXE_Customer_Document import CXECustomerDocumentPage
from Pages.Page_CXE_Document import CXEDocumentPage
from Pages.Page_CXE_Home import CXEHomePage
from Pages.Page_CXE_Page_Search import CXESearchPage
from Pages.Page_CXE_Question_Response import CXEQuestionResponsePage
from Pages.Page_CXE_Question_Responses import CXEQuestionResponsesPage
from Pages.Page_Yopmail_Home import YopmailHomePage
from Pages.Page_Home import HomePage
from Pages.Page_ContactUs import ContactUsPage
from Test.Module_Functions.MO_Functions import *
from Utilities.Functions import *
from Utilities.Utils import Utilities
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
document = CXEDocumentPage()
module = "Concern"
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

    fc.select_dropdown_element(contactUsPage.get_can(driver), Concern['change_selected_can'])
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")


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

def TC006(driver, ts_id):
    test_case = "TC006"
    contactUsPage = ContactUsPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.scroll_element(driver, contactUsPage.get_ok_btn(driver))
    fc.click(contactUsPage.get_ok_btn(driver))
    time.sleep(5)
    #insert Assert for validation
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

