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

def TC007(driver, ts_id):
    test_case = "TC063"
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, internal_outage)
    Login_CXE(driver)


    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    print("Done")

def TC001(driver,ts_id):
    test_case = "TC001"
    homePage = HomePage()
    contactUsPage = ContactUsPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.click(homePage.get_contact_us(driver))
    fc.click(contactUsPage.get_log_inquiry(driver))
    fc.scroll_element(driver, contactUsPage.get_log_remarks(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

def TC005(driver, ts_id):
    test_case = "TC005"
    contactUsPage = ContactUsPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.select_dropdown_element(driver,contactUsPage.get_log_inquiry_concern_type(driver), Outage['inquiry_concern_type'])
    contactUsPage.enter_remarks(driver,Concern['inquiry_remarks'])
    fc.scroll_element(driver, contactUsPage.get_log_inquiry_submit(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(contactUsPage.get_log_inquiry_submit(driver))
    fc.scroll_element(driver, contactUsPage.get_log_inquiry(driver))
    inquiry_reference_no = contactUsPage.get_log_inquiry_reference_number(driver)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC006(driver, ts_id):
    test_case = "TC005"
    contactUsPage = ContactUsPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")


