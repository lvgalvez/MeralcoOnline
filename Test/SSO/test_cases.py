from Pages.Page_Home import HomePage
from Pages.Page_Login import LoginPage
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
