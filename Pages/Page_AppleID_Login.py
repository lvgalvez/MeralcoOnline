from Utilities.WebMisc import WebMisc


class AppleLoginPage:
    appleID = "//apple-auth/div/div[1]/div/sign-in/div/div[1]/div[1]/div/div/div[1]/div/div/input"
    next_btn = "//div[1]/oauth-init/div[1]/div/oauth-signin/div/apple-auth/div/div[1]/div/sign-in/div/div[1]/button[1]"
    password = "//oauth-signin/div/apple-auth/div/div[1]/div/sign-in/div/div[1]/div[1]/div/div/div[2]/div/div/input"
    sign_in = "//oauth-signin/div/apple-auth/div/div[1]/div/sign-in/div/div[1]/button[1]"

    def get_apple_id(self, driver):
        return WebMisc().optional_wait_element(driver, self.appleID, "appleID")

    def get_next_btn(self, driver):
        return WebMisc().optional_wait_element(driver, self.next_btn, "next_btn")

    def get_password(self, driver):
        return WebMisc().optional_wait_element(driver, self.password, "password")

    def get_sign_in(self, driver):
        return WebMisc().optional_wait_element(driver, self.sign_in, "sign_in")