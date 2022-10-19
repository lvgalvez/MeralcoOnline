
from Utilities.WebMisc import WebMisc


class CXEDocumentPage:
    document_url = "//*/lightning-formatted-rich-text/span/a"
    document_text = "//div[contains(text(), 'Customer Document')]"

    def get_document_text(self, driver):
        return WebMisc().wait_element(driver, self.document_text, "document_text")

    def get_document_url(self, driver):
        return WebMisc().clickable_element(driver, self.document_url, "document_url")

