from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage

class GoogleSearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #defined locators with an underscore prefix to indicate they are private
        self._top_navigation_bar_locator = (By.CSS_SELECTOR, "[role='navigation'] div[data-id='trc'] [role='listitem']")
        self._search_results_locator = (By.CSS_SELECTOR, "#search .MjjYud")
        self._bottom_ads_locator = (By.ID, "bottomads")
        self._bottom_recommendation_locator = (By.ID, "bres")

    @property
    def top_navigation_bar(self):
        # Returning a list of elements found using the locator
        return self.find_elements(self._top_navigation_bar_locator)

    @property
    def search_results(self):
        # Returning a list of elements found using the locator
        return self.find_elements(self._search_results_locator)

    @property
    def bottom_ads(self):
        # Returning a single element found using the locator
        return self.find_element(self._bottom_ads_locator)

    @property
    def bottom_recommendation(self):
        # Returning a single element found using the locator
        return self.find_element(self._bottom_recommendation_locator)

    def filter_results(self, query):
        filter_options = self.top_navigation_bar
        for option in filter_options:
            if option.text == query:
                option.click()
                return
        raise NoSuchElementException(f"Element with text '{query}' not found in the top navigation bar.")

    def get_top_search_results(self, top_n):
        results = self.search_results
        return results[:top_n]
