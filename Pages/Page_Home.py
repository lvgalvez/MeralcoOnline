
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    hello_message = "//h3[@data-aura-rendered-by = '32:2;a']"


    def get_hello_message(self, driver):
        return WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.hello_message)))
