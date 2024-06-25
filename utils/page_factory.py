from pages.google_search_page import GoogleSearchPage

class PageFactory:
    def __init__(self, driver):
        self.driver = driver

    def get_google_search_page(self):
        return GoogleSearchPage(self.driver)