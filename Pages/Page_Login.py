
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    email = "//input[@id = '113:2;a']"
    password = "//input[@id = '125:2;a']"
    log_in = "//button[@data-aura-rendered-by = '179:2;a']"


    def get_email(self, driver):
        return WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.email)))

    def get_password(self, driver):
        return driver.find_element(By.XPATH, self.password)

    def get_log_in(self, driver):
        return driver.find_element(By.XPATH, self.log_in)