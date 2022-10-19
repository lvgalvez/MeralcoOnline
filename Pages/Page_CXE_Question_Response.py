
from Utilities.WebMisc import WebMisc


class CXEQuestionResponsePage:
    question_response_text = "//div[contains(text(), 'Question Response')]"
    close_tab = "//button[contains(@title,'Close QR-')]"

    def get_question_responses_text(self, driver):
        return WebMisc().wait_element(driver, self.question_response_text, "question_response_text")

    def get_close_tab(self, driver):
        return WebMisc().clickable_element(driver, self.close_tab, "close_tab")

