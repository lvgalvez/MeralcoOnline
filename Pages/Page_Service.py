from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time


class PageService:
    click_next = "//button[@data-aura-class = 'uiButton']"
    label_serv_add = "//h4[@class = 'slds-m-bottom_large mov-text_size-32 mov-text_weight-semi-bold slds-text-align_center']"

    inp_serv_add = "//input[@class = 'slds-input mov-input-trackmyapp input']"
    clk_province = "//select[@class = 'slds-select mov-select-aftersales mov-text_color-afafaf select']"
    clk_prnc_value = "//option[@value = 'METRO MANILA']"
    clk_munciplity = "//select[@class = 'slds-select mov-select-aftersales mov-text_color-afafaf slds-select inline select']"
    clk_mciplity_val = "//option[@value = 'CALOOCAN CITY']"
    clk_ownership = "//select[@class = 'slds-select mov-select-aftersales mov-text_color-afafaf slds-select_container mov-select_container select']"
    clk_ownshp_val = "//option[@value = 'Owned']"
    clk_radio_yes = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[4]/div/div/label[1]/span"
    clk_next = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[5]/div/button"
    value_added = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/ul/li[3]/a"
    automatic_payment = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div/div[5]/div[2]/div/label[1]/div"
    attach_docu = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div/div[6]/div/div[1]/div/div/label/span/span"
    clk_next_2 = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div/div[7]/button"
    label_term_condition = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/ul/li[4]/a"
    click_term_condition = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[4]/div/div[3]/div[2]/div[1]/label/div"
    submit = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[4]/div/div[3]/div[2]/div[3]/button"
    iam_not_robot = "/html/body/div[2]/div[3]/div[1]/div/div"
    birthday = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[4]/div[3]/div/div/div/input"

    def get_birthday(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.birthday)))
    def get_iam_not_robot(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.iam_not_robot)))

    def get_term_condition(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.label_term_condition)))

    def get_click_term_condition(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.click_term_condition)))

    def get_submit(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.submit)))

    def get_clk_next_2(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_next_2)))

    def get_attach_docu(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.attach_docu)))

    def get_value_added(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.value_added)))

    def get_automatic_payment(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.automatic_payment)))


    def get_next(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_next)))

    def get_inp_serv_add(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.inp_serv_add)))


    def get_clk_radio(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_radio_yes)))

    def get_clk_province(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_province)))

    def get_province_value(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_prnc_value)))

    def get_municipality(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_munciplity)))

    def get_clk_mciplity_val(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_mciplity_val)))

    def get_clk_ownership(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_ownership)))

    def get_clk_ownership_value(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.clk_ownshp_val)))

    def get_click_next(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.click_next)))

    def get_label_serv_add(self, driver):
        return WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, self.label_serv_add)))