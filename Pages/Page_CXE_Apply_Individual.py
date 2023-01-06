from Utilities.WebMisc import WebMisc


class CXEApplyIndividual:

    email_input = "//input[@placeholder= 'Email * (username@domain.com)']"
    first_name = "//input[@placeholder ='First Name *']"
    last_name = "//input[@placeholder = 'Last Name *']"
    mobile_num = "//input[@placeholder = 'Mobile Number * (XXXXXXXXXX)']"
    terms_and_conditions = "//div/div/div[2]/div[2]/div[6]/div/div[1]/label/div"
    register_btn = "//button[text() = 'Register']"

    def get_email_attr(self, driver):
        return WebMisc().optional_clickable_element(driver, self.email_input, "email_input")

    def get_firstname_attr(self, driver):
        return WebMisc().optional_clickable_element(driver, self.first_name, "first_name")

    def get_lastname_attr(self, driver):
        return WebMisc().optional_clickable_element(driver, self.last_name, "last_name")

    def get_mobile_num(self, driver):
        return WebMisc().optional_clickable_element(driver, self.mobile_num, "mobile_num")

    def get_terms_and_conditions(self, driver):
        return WebMisc().optional_clickable_element(driver, self.terms_and_conditions, "terms_and_conditions")

    def get_register_btn(self, driver):
        return WebMisc().optional_clickable_element(driver, self.register_btn, "register_btn")
