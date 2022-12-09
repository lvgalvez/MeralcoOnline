import time

from Utilities.Functions import *
from Utilities.Utils import Utilities
from Pages.Page_Login import LoginPage
from Pages.Page_PayBills import PayBillPage
from Pages.Page_Payment import PaymentPage
from Test.Module_Functions.MO_Functions import *
from Utilities.Data import *

fc = Functions()
log = Utilities().getlogger()

module = "RFC"

def TC001(driver, ts_id):
    test_case = "TC001"
    login= LoginPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    element = login.get_red_banner(driver)
    assertRedBanner(element)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")

def TC002(driver, ts_id):
    test_case = "TC002"
    login = LoginPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.click(login.get_forgot_password(driver))
    time.sleep(2)

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")
    element = login.get_red_banner(driver)
    assertRedBanner(element)

def TC049(driver, ts_id):
    test_case = "TC049"

    homePage = HomePage()
    payBillsPage = PayBillPage()
    paymentPage = PaymentPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, RFC['username_multiple_service'], RFC['password'])
    time.sleep(5)

    fc.click(homePage.get_bills_and_payments(driver))
    time.sleep(10)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    fc.modal_click(driver, homePage.get_pay_bills(driver))


    fc.bookmark(module, ts_id, test_case, "Step 2")
    time.sleep(20)
    #fc.scroll_element(driver, payBillsPage.get_pay_now(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.scroll_element(driver, payBillsPage.get_pay_now(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")
    fc.click(payBillsPage.get_pay_now(driver))
    time.sleep(5)


    fc.bookmark(module, ts_id, test_case, "Step 4")
    fc.scroll_element(driver, payBillsPage.get_proceed(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")
    fc.click(payBillsPage.get_proceed(driver))

    fc.bookmark(module, ts_id, test_case, "Step 5")
    time.sleep(5)
    fc.click(paymentPage.get_card_payment(driver))
    fc.input_text(paymentPage.get_card_number(driver), RFC['card_number'])
    fc.input_text(paymentPage.get_expiry_date(driver), RFC['expiry_date'])
    fc.input_text(paymentPage.get_cvc(driver), RFC['cvv'])
    fc.input_text(paymentPage.get_firstName(driver), RFC['first_name'])
    fc.input_text(paymentPage.get_lastName(driver), RFC['last_name'])
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")

    fc.bookmark(module, ts_id, test_case, "Step 6")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 6")
    fc.click(paymentPage.get_pay_btn(driver))


    time.sleep(15)

    fc.bookmark(module, ts_id, test_case, "Step 7")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 7")
    fc.click(paymentPage.get_back_to_merchant(driver))
    time.sleep(10)


    fc.bookmark(module, ts_id, test_case, "Step 8")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 8")

def TC050(driver, ts_id):
    test_case = "TC050"

    homePage = HomePage()
    payBillsPage = PayBillPage()
    paymentPage = PaymentPage()

    fc.bookmark(module, ts_id, test_case, "Step 1")
    Log_In_Meralco_Online(driver, Concern['username_single_service'], Concern['password'])
    time.sleep(5)

    fc.click(homePage.get_bills_and_payments(driver))
    time.sleep(10)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")
    # fc.modal_click(driver, homePage.get_pay_bills(driver))

    fc.bookmark(module, ts_id, test_case, "Step 2")
    fc.scroll_element(driver, payBillsPage.get_pay_now(driver))
    # fc.click(payBillsPage.get_pay_now(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 2")

    fc.bookmark(module, ts_id, test_case, "Step 3")
    fc.scroll_element(driver, payBillsPage.get_pay_now(driver))
    fc.click(payBillsPage.get_pay_now(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 3")

    fc.bookmark(module, ts_id, test_case, "Step 4")
    fc.scroll_element(driver, payBillsPage.get_proceed(driver))
    fc.click(payBillsPage.get_proceed(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 4")

    fc.bookmark(module, ts_id, test_case, "Step 5")
    time.sleep(5)
    fc.click(paymentPage.get_card_payment(driver))
    fc.input_text(paymentPage.get_card_number(driver), RFC['card_number'])
    fc.input_text(paymentPage.get_expiry_date(driver), RFC['expiry_date'])
    fc.input_text(paymentPage.get_cvc(driver), RFC['cvv'])
    fc.input_text(paymentPage.get_firstName(driver), RFC['first_name'])
    fc.input_text(paymentPage.get_lastName(driver), RFC['last_name'])
    fc.screen_capture(driver, module, ts_id, test_case, "Step 5")

    fc.bookmark(module, ts_id, test_case, "Step 6")
    fc.click(paymentPage.get_pay_btn(driver))
    fc.screen_capture(driver, module, ts_id, test_case, "Step 6")

    time.sleep(15)

    fc.bookmark(module, ts_id, test_case, "Step 7")
    fc.click(paymentPage.back_to_merchant)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 7")

    fc.bookmark(module, ts_id, test_case, "Step 8")
    fc.screen_capture(driver, module, ts_id, test_case, "Step 8")

    fc.bookmark(module, ts_id, test_case, "Step 9")
    tab = driver.window_handles[1]
    fc.switch_window_tab(tab)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 9")

def TC051(driver, ts_id):
    test_case = "TC049"

    homePage = HomePage()
    Log_In_Meralco_Online(driver, Concern['username_single_service'], Concern['password'])
    time.sleep(5)

    fc.bookmark(module, ts_id, test_case, "Step 1")
    fc.scroll_element(driver,homePage.get_bayad_express_ad(driver))
    element = homePage.get_bayad_express_ad(driver)
    assertBayadExpressAd(element)
    fc.screen_capture(driver, module, ts_id, test_case, "Step 1")


