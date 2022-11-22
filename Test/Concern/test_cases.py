import time
from Pages.Page_CXE_Case import CXECasePage
from Pages.Page_CXE_Customer_Document import CXECustomerDocumentPage
from Pages.Page_CXE_Document import CXEDocumentPage
from Pages.Page_CXE_Home import CXEHomePage
from Pages.Page_CXE_Page_Search import CXESearchPage
from Pages.Page_CXE_Question_Response import CXEQuestionResponsePage
from Pages.Page_CXE_Question_Responses import CXEQuestionResponsesPage
from Pages.Page_Yopmail_Home import YopmailHomePage
from Pages.Page_ConcernStatus import ConcernStatusPage
from Pages.Page_Home import HomePage
from Pages.Page_ContactUs import ContactUsPage
from Test.Module_Functions.MO_Functions import *
from Utilities.Functions import *
from Utilities.Utils import Utilities
from Pages.Page_Yopmail_Home import YopmailHomePage
from Utilities.Config import *

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
module = "Concern"
inquiry_reference_no = ''




def TC001(driver,ts_id):
    test_case = "TC001"
    homePage = HomePage()
    contactUsPage = ContactUsPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.click(homePage.get_contact_us(driver))
    fc.click(contactUsPage.get_log_inquiry(driver))
    fc.scroll_element(driver, contactUsPage.get_log_remarks(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

def TC003(driver, ts_id):
    test_case = "TC003"
    contactUsPage = ContactUsPage()
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, "https://fuat-meralco.cs73.force.com/customers/s/contact")
    fc.click(contactUsPage.get_log_inquiry(driver))
    fc.verify(contactUsPage.get_CAN(driver))
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

def TC007(driver, ts_id):
    test_case = "TC007"
    contactUsPage = ContactUsPage()
    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.new_tab(driver, "https://fuat-meralco.cs73.force.com/customers/s/contact")
    fc.click(contactUsPage.get_log_inquiry(driver))
    #fc.click(contactUsPage.get_feedback(driver))
    #fc.click(contactUsPage.get_make_request(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

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

    fc.bookmark(module, ts_id, test_case, "Step 16")
    fc.new_tab(driver, yopmail)
    fc.input_text(yopmail_home.get_email(driver), email)
    fc.click(yopmail_home.get_check_inbox(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 16")