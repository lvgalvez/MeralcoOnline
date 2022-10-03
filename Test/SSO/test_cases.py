import time

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
module = "SSO"

def TC007(driver, ts_id, email, password):
    test_case = "TC007"
    log.info("==========Log in==========")

    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    login = LoginPage()
    function.input_text(login.get_email(driver), email)
    function.input_text(login.get_password(driver), password)
    function.screen_capture(driver, module, ts_id, test_case, "Step 1")
    function.click(login.get_log_in(driver))
    home = HomePage()
    function.verify(home.get_hello_message(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    log.info(test_case + " Passed")

def TC003(driver, ts_id, email, password):
    test_case = "TC003"
    log.info("==========Forgot Password==========")

    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    login = LoginPage()
    function.click(login.get_forgot_password(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1")
    function.bookmark(module, ts_id, test_case, "Step 2")
    forgot_password = ForgotPasswordPage()
    function.input_text(forgot_password.get_email(driver), email)
    function.screen_capture(driver, module, ts_id, test_case, "Step 2")
    function.click(forgot_password.get_send_confirmation_email(driver))
    function.verify(forgot_password.get_email_sent(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 2b")
    function.bookmark(module, ts_id, test_case, "Step 3")
    function.new_tab(driver, yopmail)
    yopmail_home = YopmailHomePage()
    function.input_text(yopmail_home.get_email(driver), email)
    function.click(yopmail_home.get_check_inbox(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3")
    yopmail_inbox = YopmailInboxPage()
    yopmail_inbox.get_here_link(driver)
    reset_password = ResetPasswordPage()
    function.input_text(reset_password.get_new_password(driver), password)
    function.input_text(reset_password.get_confirm_password(driver), password)
    function.screen_capture(driver, module, ts_id, test_case, "Step 3b")
    function.click(reset_password.get_set_password(driver))
    function.verify(login.get_new_password_confirmation(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3c")
    function.bookmark(module, ts_id, test_case, "Step 4")
    function.input_text(login.get_email(driver), email)
    function.input_text(login.get_password(driver), password)
    function.screen_capture(driver, module, ts_id, test_case, "Step 4")
    function.click(login.get_log_in(driver))
    home = HomePage()
    function.verify(home.get_hello_message(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 4b")
    log.info(test_case + " Passed")






