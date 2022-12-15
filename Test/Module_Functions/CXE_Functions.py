from Pages.Page_CXE_Login import CXELoginPage
from Pages.Page_ContactUs import ContactUsPage
from Pages.Page_External_Outage import ExternalOutagePage
from Pages.Page_Home import HomePage
from Pages.Page_Internal_Outage import InternalOutagePage
from Pages.Page_Login import LoginPage
from Pages.Page_Report_Outage import ReportOutagePage
from Utilities.Config import *
from Utilities.Functions import Functions
from Utilities.Utils import Utilities
from Utilities.Data import *
import time

fc = Functions()
log = Utilities().getlogger()
home = HomePage()
contact = ContactUsPage()
login = LoginPage()
external_outage = ExternalOutagePage()
report_outage = ReportOutagePage()
internal_outage = InternalOutagePage()
cxe_login = CXELoginPage()


def Log_in_CXE(driver, cxe_email, cxe_password):
    fc.new_tab(driver, cxe)
    fc.click(cxe_login.get_meralco_user_id(driver))
    # function.click(cxe_login.get_use_another_account(driver))
    fc.input_text(cxe_login.get_email(driver), cxe_email)
    fc.click(cxe_login.get_next(driver))
    fc.input_text(cxe_login.get_password(driver), cxe_password)
    fc.click(cxe_login.get_sign_in(driver))
    time.sleep(25)
    fc.click(cxe_login.get_stay_sign_no(driver))
