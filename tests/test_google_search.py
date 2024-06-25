from .base_test import BaseTest
from config.config import BASE_URL

class GoogleSearchTest(BaseTest):
    def test_google_search(self):
        # Open Google
        self.driver.get(BASE_URL)

        # Perform Search
        google_search_page = self.page_factory.get_google_search_page()
        google_search_page.search("appium")

        # Verify Results
        search_results = google_search_page.get_search_results()
        self.assertGreater(len(search_results), 0, "No search results found")