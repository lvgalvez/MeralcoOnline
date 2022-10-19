from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.Config import wait_time
from Utilities.WebMisc import WebMisc


class CXECasePage:

    cases_text = "//div[@class ='entityNameTitle slds-line-height--reset']"
    close_case = "//button[contains(@title,'Close 2')]"
    question_responses = "//a[@class = 'slds-card__header-link baseCard__header-title-container' and span[contains(text(), 'Question Responses')]]"
    customer_documents = "//a[@class = 'slds-card__header-link baseCard__header-title-container' and span[contains(text(), 'Customer Document')]]"


    def get_cases_text(self, driver):
        return WebMisc().wait_element(driver, self.cases_text, "cases_text")

    def get_question_responses(self, driver):
        return WebMisc().clickable_element(driver, self.question_responses, "question_responses")

    def get_customer_documents(self, driver):
        return WebMisc().clickable_element(driver, self.customer_documents, "customer_documents")

    def get_close_case(self, driver):
        return WebMisc().clickable_element(driver, self.close_case, "close_case")
