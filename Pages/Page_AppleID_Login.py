from Utilities.WebMisc import WebMisc


class AppleLoginPage:
    appleID = "//apple-auth/div/div[1]/div/sign-in/div/div[1]/div[1]/div/div/div[1]/div/div/input"
    next_btn = "//div[1]/oauth-init/div[1]/div/oauth-signin/div/apple-auth/div/div[1]/div/sign-in/div/div[1]/button[1]"
    password = "//oauth-signin/div/apple-auth/div/div[1]/div/sign-in/div/div[1]/div[1]/div/div/div[2]/div/div/input"
    sign_in = "//oauth-signin/div/apple-auth/div/div[1]/div/sign-in/div/div[1]/button[1]"
    mobile_num = "/html/body/div[3]/div[3]/div/div[2]/div[1]/section/div/div/div[2]/div/div[4]/div/div/div[1]/div[1]/div/div[2]/lightning-input/div/input"
    "/html/body/div[3]/div[3]/div/div[2]/div[1]/section/div/div/div[5]/div[1]/div/div/div[1]/div/div[2]/lightning-input/div/input"
    can_input = "/html/body/div[3]/div[3]/div/div[2]/div[1]/section/div/div/div[2]/div/div[4]/div/div/div[1]/div[2]/lightning-input/div/input"
    total_kwh = "/html/body/div[3]/div[3]/div/div[2]/div[1]/section/div/div/div[2]/div/div[4]/div/div/div[6]/div[1]/div/div/lightning-input/div[1]/input"
    bill_date = "/html/body/div[3]/div[3]/div/div[2]/div[1]/section/div/div/div[2]/div/div[4]/div/div/div[6]/div[2]/div/div/div/div/div/input"
    terms_conditions = "//div[@class='checkbox-custom']"
    submit = "//button[contains(text(), 'Submit')]"
    phone_number = "//input[@placeholder='Mobile Number *']"

    def get_apple_id(self, driver):
        return WebMisc().optional_wait_element(driver, self.appleID, "appleID")

    def get_next_btn(self, driver):
        return WebMisc().optional_wait_element(driver, self.next_btn, "next_btn")

    def get_password(self, driver):
        return WebMisc().optional_wait_element(driver, self.password, "password")

    def get_sign_in(self, driver):
        return WebMisc().optional_wait_element(driver, self.sign_in, "sign_in")

    def get_mobile_number(self, driver):
        return WebMisc().optional_wait_element(driver, self.mobile_num, "mobile_num")

    def get_can(self, driver):
        return WebMisc().optional_wait_element(driver, self.can_input, "can_input")

    def get_kwh(self, driver):
        return WebMisc().optional_wait_element(driver, self.total_kwh, "total_kwh")

    def get_bill_date(self, driver):
        return WebMisc().optional_wait_element(driver, self.bill_date, "bill_date")

    def get_terms_conditions(self, driver):
        return WebMisc().optional_wait_element(driver, self.terms_conditions, "terms_conditions")

    def get_submit(self, driver):
        return WebMisc().optional_wait_element(driver, self.submit, "submit")

    def get_phone_number(self, driver):
        return WebMisc().optional_wait_element(driver, self.phone_number, "phone_number")