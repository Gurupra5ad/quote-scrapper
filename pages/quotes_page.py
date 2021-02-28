from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser


class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quote_tags = self.browser.find_element_by_css_selector(locator)
        return [
            QuoteParser(e) 
            for e in self.browser.find_elements_by_css_selector(
                QuotesPageLocators.QUOTE
                )
            ]