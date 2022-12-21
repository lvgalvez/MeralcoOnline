
from Utilities.WebMisc import WebMisc

class PayBillPage:

    pay_now = "//a[contains(text(), 'Pay Now')]"
    subTotal = "//input[contains(@class, 'uiInputSmartNumber')]"
    proceedBtn = "//a[contains(text(), 'Proceed')]"


    def get_pay_now(self, driver):
        return WebMisc().clickable_element(driver, self.pay_now, "pay_now")

    def get_subtotal(self, driver):
        return WebMisc().clickable_element(driver, self.subTotal, "subTotal")

    def get_proceed(self, driver):
        return WebMisc().clickable_element(driver, self.proceedBtn, "proceedBtn")
