
from Utilities.WebMisc import WebMisc


class CXEQuestionResponsesPage:
    question_responses_text = "//h1[@title = 'Question Responses']"
    question_first = "//*/table/tbody/tr[1]/th/span/a"
    question_second = "//*/table/tbody/tr[2]/th/span/a"
    question_third = "//*/table/tbody/tr[3]/th/span/a"
    close_tab = "//button[contains(@title,'Close Question Responses')]"

    def get_question_responses_text(self, driver):
        return WebMisc().wait_element(driver, self.question_responses_text, "question_responses_text")

    def get_question_first(self, driver):
        return WebMisc().wait_element(driver, self.question_first, "question_first")

    def get_question_second(self, driver):
        return WebMisc().wait_element(driver, self.question_second, "question_second")

    def get_question_third(self, driver):
        return WebMisc().wait_element(driver, self.question_third, "question_third")

    def get_close_tab(self, driver):
        return WebMisc().clickable_element(driver, self.close_tab, "close_tab")

