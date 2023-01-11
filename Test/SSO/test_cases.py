import time

from Pages.Page_AppleID_Login import AppleLoginPage
from Pages.Page_Enroll_Service import EnrollServicePage
from Pages.Page_Forgot_Password import ForgotPasswordPage
from Pages.Page_Google_Login import GoogleLoginPage
from Pages.Page_Home import HomePage
from Pages.Page_Login import LoginPage
from Pages.Page_My_Profile import MyProfilePage
from Pages.Page_Reset_Password import ResetPasswordPage
from Pages.Page_Yopmail_Home import YopmailHomePage
from Pages.Page_Yopmail_Inbox import YopmailInboxPage
from Utilities.Config import *
from Utilities.Data import SSO
from Utilities.Functions import Functions
from Utilities.Utils import Utilities
from Test.Module_Functions.MO_Functions import *


log = Utilities().getlogger()
module = "SSO"
fc = Functions()


def TC001(driver, ts_id, email):
    test_case = "TC001"

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
    error_prompt = "Please use your Facebook, Google, or Apple account to login. Your Meralco Online account is registered and/or previously accessed in using these options."
    function.verify_text(forgot_password.get_sso_forgot(driver), error_prompt)
    function.screen_capture(driver, module, ts_id, test_case, "Step 2b")

def TC002a(driver, ts_id):
    test_case = "TC001a"
    login = LoginPage()
    google = GoogleLoginPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")

    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(login.get_google_login(driver))
    fc.input_text(google.get_email(driver), SSO['google_email'])
    fc.click(google.get_next(driver))
    fc.input_text(google.get_password(driver), SSO['google_password'])
    fc.click(google.get_send(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC003a(driver, ts_id):
    test_case = "TC003a"
    login = LoginPage()
    apple = AppleLoginPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")

    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(login.get_apple_login(driver))
    fc.input_text(apple.get_email(driver), SSO['google_email'])
    fc.click(apple.get_next_btn(driver))
    fc.input_text(apple.get_password(driver), SSO['google_password'])
    fc.click(apple.get_sign_in(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC005a(driver, ts_id):
    test_case = "TC005a"
    login = LoginPage()
    google = GoogleLoginPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")

    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(login.get_google_login(driver))
    fc.input_text(google.get_email(driver), SSO['google_email'])
    fc.click(google.get_next(driver))
    fc.input_text(google.get_password(driver), SSO['google_password'])
    fc.click(google.get_send(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC006a(driver, ts_id):
    test_case = "TC006a"
    login = LoginPage()
    apple = AppleLoginPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")

    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(login.get_apple_login(driver))
    fc.input_text(apple.get_email(driver), SSO['google_email'])
    fc.click(apple.get_next_btn(driver))
    fc.input_text(apple.get_password(driver), SSO['google_password'])
    fc.click(apple.get_sign_in(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC008a(driver, ts_id):
    test_case = "TC008a"
    login = LoginPage()
    google = GoogleLoginPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")

    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(login.get_google_login(driver))
    fc.input_text(google.get_email(driver), SSO['google_email'])
    fc.click(google.get_next(driver))
    fc.input_text(google.get_password(driver), SSO['google_password'])
    fc.click(google.get_send(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC009a(driver, ts_id):
    test_case = "TC006a"
    login = LoginPage()
    apple = AppleLoginPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")

    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(login.get_apple_login(driver))
    fc.input_text(apple.get_email(driver), SSO['google_email'])
    fc.click(apple.get_next_btn(driver))
    fc.input_text(apple.get_password(driver), SSO['google_password'])
    fc.click(apple.get_sign_in(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC011a(driver, ts_id):
    test_case = "TC008a"
    login = LoginPage()
    google = GoogleLoginPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")

    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(login.get_google_login(driver))
    fc.input_text(google.get_email(driver), SSO['google_email'])
    fc.click(google.get_next(driver))
    fc.input_text(google.get_password(driver), SSO['google_password'])
    fc.click(google.get_send(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC012a(driver, ts_id):
    test_case = "TC006a"
    login = LoginPage()
    apple = AppleLoginPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")

    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.click(login.get_apple_login(driver))
    fc.input_text(apple.get_email(driver), SSO['google_email'])
    fc.click(apple.get_next_btn(driver))
    fc.input_text(apple.get_password(driver), SSO['google_password'])
    fc.click(apple.get_sign_in(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC039a(driver, ts_id):
    test_case = "TC039a"
    home = HomePage()
    enroll = EnrollServicePage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, Concern['username_single_service'], Concern['password'])
    fc.modal_click(driver, home.get_accounts(driver))
    fc.modal_click(driver, home.get_enroll_service(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    time.sleep(5)

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(enroll.get_can(driver), Concern['sacxe_single_can'])
    fc.input_text(enroll.get_sin(driver), Concern['sacxe_single_sin'])
    fc.input_text(enroll.get_total_kwh(driver), RFC['total_kwh'])
    fc.input_text(enroll.get_bill_date(driver), RFC['bill_date'])
    #fc.click(enroll.get_submit(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC042a(driver, ts_id):
    test_case = "TC039a"
    home = HomePage()
    profile = MyProfilePage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, Concern['username_single_service'], Concern['password'])
    fc.modal_click(driver, home.get_profile_name(driver))
    fc.modal_click(driver, home.get_my_profile(driver))
    time.sleep(5)
    fc.click(profile.get_landline_edit(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(profile.get_landline(driver), Outage['landline'])
    #fc.scroll_element(driver, profile.get_save_btn(driver))
    fc.click(profile.get_save_btn(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC045a(driver, ts_id):
    test_case = "TC039a"
    home = HomePage()
    profile = MyProfilePage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, Concern['username_single_service'], Concern['password'])
    fc.modal_click(driver, home.get_profile_name(driver))
    fc.modal_click(driver, home.get_my_profile(driver))
    time.sleep(5)
    fc.click(profile.get_landline_edit(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.input_text(profile.get_landline(driver), Outage['wrongLandline'])
    fc.click(profile.get_save_btn(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

def TC002(driver, ts_id, email, password):
    test_case = "TC002"

    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    login = LoginPage()
    function.click(login.get_google_login(driver))
    google_login = GoogleLoginPage()
    function.option_click(google_login.get_use_another_account(driver))
    function.input_text(google_login.get_email(driver), email)
    function.screen_capture(driver, module, ts_id, test_case, "Step 1")
    function.click(google_login.get_next(driver))
    function.input_text(google_login.get_password(driver), password)
    function.click(google_login.get_next(driver))
    time.sleep(40)
    home = HomePage()
    function.verify(home.get_hello_message(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    function.bookmark(module, ts_id, test_case, "Step 2")
    function.click(home.get_profile_name(driver))
    function.click(home.get_my_profile(driver))
    my_profile = MyProfilePage()
    function.click(my_profile.get_change_password(driver))
    sso_prompt = "For added security, this function is unavailable as your Meralco Online account is linked to your Facebook, Google, or Apple Account."
    function.verify_text(my_profile.get_sso_prompt(driver), sso_prompt)
    function.screen_capture(driver, module, ts_id, test_case, "Step 2")


def TC003(driver, ts_id, email, password):
    test_case = "TC003"

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


def TC004(driver, ts_id, email, password, new_password):
    test_case = "TC004"

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
    function.bookmark(module, ts_id, test_case, "Step 2")
    function.click(home.get_profile_name(driver))
    function.click(home.get_my_profile(driver))
    my_profile = MyProfilePage()
    function.click(my_profile.get_change_password(driver))
    function.input_text(my_profile.get_current_password(driver), password)
    function.input_text(my_profile.get_new_password(driver), new_password)
    function.input_text(my_profile.get_confirm_new_password(driver), new_password)
    function.screen_capture(driver, module, ts_id, test_case, "Step 2")
    function.click(my_profile.get_set_password(driver))
    time.sleep(2)
    function.screen_capture(driver, module, ts_id, test_case, "Step 2b")
    function.click(my_profile.get_password_confirmation(driver))
    function.bookmark(module, ts_id, test_case, "Step 3")
    function.input_text(login.get_email(driver), email)
    function.input_text(login.get_password(driver), new_password)
    function.screen_capture(driver, module, ts_id, test_case, "Step 3")
    function.click(login.get_log_in(driver))
    function.verify(home.get_hello_message(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 3b")


def TC005(driver, ts_id, email, password):
    test_case = "TC005"

    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    login = LoginPage()
    function.input_text(login.get_email(driver), email)
    function.input_text(login.get_password(driver), password)
    function.screen_capture(driver, module, ts_id, test_case, "Step 1")
    function.click(login.get_log_in(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1b")


def TC006(driver, ts_id, email, password):
    test_case = "TC006"

    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    login = LoginPage()
    function.input_text(login.get_email(driver), email)
    function.input_text(login.get_password(driver), password)
    function.screen_capture(driver, module, ts_id, test_case, "Step 1")
    function.click(login.get_log_in(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    function.click(login.get_google_login(driver))
    google_login = GoogleLoginPage()
    function.bookmark(module, ts_id, test_case, "Step 2")
    function.option_click(google_login.get_use_another_account(driver))
    function.input_text(google_login.get_email(driver), email)
    function.screen_capture(driver, module, ts_id, test_case, "Step 2")
    function.click(google_login.get_next(driver))
    function.input_text(google_login.get_password(driver), password)
    function.click(google_login.get_next(driver))
    time.sleep(20)
    home = HomePage()
    function.verify(home.get_hello_message(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 2b")


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


def TC008(driver, ts_id, email, password):
    test_case = "TC008"

    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    login = LoginPage()
    function.click(login.get_google_login(driver))
    google_login = GoogleLoginPage()
    function.option_click(google_login.get_use_another_account(driver))
    function.input_text(google_login.get_email(driver), email)
    function.screen_capture(driver, module, ts_id, test_case, "Step 1")
    function.click(google_login.get_next(driver))
    function.input_text(google_login.get_password(driver), password)
    function.click(google_login.get_next(driver))
    time.sleep(40)
    home = HomePage()
    function.verify(home.get_hello_message(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1b")


def TC009(driver, ts_id, email, password):
    test_case = "TC009"

    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    login = LoginPage()
    function.input_text(login.get_email(driver), email)
    function.input_text(login.get_password(driver), password)
    function.screen_capture(driver, module, ts_id, test_case, "Step 1")
    function.click(login.get_log_in(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1b")


def TC010(driver, ts_id, email, password):
    test_case = "TC010"
    log.info("==========Log in==========")

    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    login = LoginPage()
    function.input_text(login.get_email(driver), email)
    function.input_text(login.get_password(driver), password)
    function.screen_capture(driver, module, ts_id, test_case, "Step 1")
    function.click(login.get_log_in(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1b")
    login.get_email(driver).clear()
    login.get_password(driver).clear()
    function.input_text(login.get_email(driver), email)
    function.input_text(login.get_password(driver), password)
    function.screen_capture(driver, module, ts_id, test_case, "Step 1c")
    function.click(login.get_log_in(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1d")
    login.get_email(driver).clear()
    login.get_password(driver).clear()
    function.input_text(login.get_email(driver), email)
    function.input_text(login.get_password(driver), password)
    function.screen_capture(driver, module, ts_id, test_case, "Step 1e")
    function.click(login.get_log_in(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1f")
    login.get_email(driver).clear()
    login.get_password(driver).clear()
    function.input_text(login.get_email(driver), email)
    function.input_text(login.get_password(driver), password)
    function.screen_capture(driver, module, ts_id, test_case, "Step 1g")
    function.click(login.get_log_in(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1h")
    login.get_email(driver).clear()
    login.get_password(driver).clear()
    function.input_text(login.get_email(driver), email)
    function.input_text(login.get_password(driver), password)
    function.screen_capture(driver, module, ts_id, test_case, "Step 1i")
    function.click(login.get_log_in(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1j")


def TC013(driver, ts_id, email):
    test_case = "TC013"

    function = Functions()
    function.bookmark(module, ts_id, test_case, "Step 1")
    login = LoginPage()
    function.click(login.get_google_login(driver))
    google_login = GoogleLoginPage()
    function.option_click(google_login.get_use_another_account(driver))
    function.input_text(google_login.get_email(driver), email)
    function.screen_capture(driver, module, ts_id, test_case, "Step 1")
    function.click(google_login.get_next(driver))
    function.screen_capture(driver, module, ts_id, test_case, "Step 1b")
