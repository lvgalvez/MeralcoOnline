import time

from Pages.Page_CXE_Apply_Home import CXEApplyHomePage
from Pages.Page_CXE_Apply_Reg import CXEApplyRegPage
from Pages.Page_Forgot_Password import ForgotPasswordPage
from Pages.Page_Home import HomePage
from Pages.Page_Login import LoginPage
from Pages.Page_Reset_Password import ResetPasswordPage
from Pages.Page_Yopmail_Home import YopmailHomePage
from Pages.Page_Yopmail_Inbox import YopmailInboxPage
from Utilities.Config import *
from Utilities.Data import SSO
from Utilities.Functions import Functions
from Utilities.Utils import Utilities


log = Utilities().getlogger()
module = "SAMO"


def TC002(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, password):
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
