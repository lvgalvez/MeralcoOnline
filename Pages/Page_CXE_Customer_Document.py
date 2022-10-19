
from Utilities.WebMisc import WebMisc


class CXECustomerDocumentPage:
    question_response_text = "//h1[@title='Customer Documents']"
    document_first = "//*/table/tbody/tr/th/span/a"

    def get_question_response_text(self, driver):
        return WebMisc().wait_element(driver, self.question_response_text, "question_response_text")

    def get_document_first(self, driver):
        return WebMisc().clickable_element(driver, self.document_first, "document_first")
