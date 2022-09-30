
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YopmailInboxPage:
    here_link = "//a[contains(@href, 'https://uat.online.meralco.com.ph/customers/s/setpassword?id')]"

    def get_here_link(self, driver):
        WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='ifmail']")))
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.here_link))).click()
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])



