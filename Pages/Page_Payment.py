from Utilities.WebMisc import WebMisc

class PaymentPage:
    cardPayment = "//img[@src='/static/media/cardLogo.c6a02c1e.svg']"
    payBtn = "//button[contains(@class, 'MuiButton-fullWidth')]"
    cardNumber = "//input[@name='cardNumber']"
    expiryDate = "//input[@name='expiryDate']"
    cvc = "//input[@name='cvc']"
    firstName = "//input[@name='firstName']"
    lastName = "//input[@name='lastName']"
    back_to_merchant = "//button[@id='button-back']"


    def get_card_payment(self, driver):
        return WebMisc().clickable_element(driver, self.cardPayment, "cardPayment")

    def get_pay_btn(self, driver):
        return WebMisc().clickable_element(driver, self.payBtn, "payBtn")

    def get_card_number(self, driver):
        return WebMisc().clickable_element(driver, self.cardNumber, "cardNumber")

    def get_expiry_date(self, driver):
        return WebMisc().clickable_element(driver, self.expiryDate, "expiryDate")

    def get_cvc(self, driver):
        return WebMisc().clickable_element(driver, self.cvc, "cvc")

    def get_firstName(self, driver):
        return WebMisc().clickable_element(driver, self.firstName, "firstName")

    def get_lastName(self, driver):
        return WebMisc().clickable_element(driver, self.lastName, "lastName")

    def get_back_to_merchant(self, driver):
        return WebMisc().clickable_element(driver, self.back_to_merchant, "back_to_merchant")
