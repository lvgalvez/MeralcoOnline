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
    login.get_email(driver).send_keys(email)
    login.get_password(driver).send_keys(password)
    function.screen_capture(driver, module, ts_id, test_case, "Step 1")
    login.get_log_in(driver).click()
    home = HomePage()
    home.get_hello_message(driver)
    function.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    function.new_tab(driver, yopmail)
    log.info(test_case + " Passed")

def TC003(driver, ts_id, email, password):
    test_case = "TC003"
    log.info("==========Forgot Password==========")

    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    login = LoginPage()
    login.get_forgot_password(driver).click()
    function.screen_capture(driver, module, ts_id, test_case, "Step 1")
    function.bookmark(module, ts_id, test_case, "Step 2")
    forgot_password = ForgotPasswordPage()
    forgot_password.get_email(driver).send_keys(email)
    function.screen_capture(driver, module, ts_id, test_case, "Step 2")
    forgot_password.get_send_confirmation_email(driver).click()
    forgot_password.get_email_sent(driver).is_displayed()
    function.screen_capture(driver, module, ts_id, test_case, "Step 2b")
    function.bookmark(module, ts_id, test_case, "Step 3")
    function.new_tab(driver, yopmail)
    yopmail_home = YopmailHomePage()
    yopmail_home.get_email(driver).send_keys(email)
    yopmail_home.get_check_inbox(driver).click()
    function.screen_capture(driver, module, ts_id, test_case, "Step 3")
    yopmail_inbox = YopmailInboxPage()
    yopmail_inbox.get_here_link(driver)
    reset_password = ResetPasswordPage()
    reset_password.get_new_password(driver).send_keys(password)
    reset_password.get_confirm_password(driver).send_keys(password)
    function.screen_capture(driver, module, ts_id, test_case, "Step 3b")
    reset_password.get_set_password(driver).click()
    login.get_new_password_confirmation(driver).is_displayed()
    function.screen_capture(driver, module, ts_id, test_case, "Step 3c")
    function.bookmark(module, ts_id, test_case, "Step 4")
    login.get_email(driver).send_keys(email)
    login.get_password(driver).send_keys(password)
    function.screen_capture(driver, module, ts_id, test_case, "Step 4")
    login.get_log_in(driver).click()
    home = HomePage()
    home.get_hello_message(driver)
    function.screen_capture(driver, module, ts_id, test_case, "Step 4b")
    log.info(test_case + " Passed")






