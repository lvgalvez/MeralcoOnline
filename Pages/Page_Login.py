
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    email = "//input[@id = '113:2;a']"
    password = "//input[@id = '125:2;a']"
    log_in = "//button[@data-aura-rendered-by = '179:2;a']"
    forgot_password = "//span[@data-aura-rendered-by = '168:2;a']"
    new_password_confirmation = "//strong[@data-aura-rendered-by = '4:95;a']"


    def get_email(self, driver):
        return WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.email)))

    def get_password(self, driver):
        return driver.find_element(By.XPATH, self.password)

    def get_log_in(self, driver):
        return driver.find_element(By.XPATH, self.log_in)

    def get_forgot_password(self, driver):
        return driver.find_element(By.XPATH, self.forgot_password)

    def get_new_password_confirmation(self, driver):
        return WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.new_password_confirmation)))
