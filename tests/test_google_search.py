from .base_test import BaseTest
from config.config import BASE_URL
from pages.google_search_page import GoogleSearchPage
from pages.search_results_page import SearchResultsPage

class GoogleSearchTest(BaseTest):
    def test_google_search(self):
        # Open Google
        self.driver.get(BASE_URL)

        # Perform a search using GoogleSearchPage
        google_search_page = GoogleSearchPage(self.driver)
        google_search_page.search("selenium")

        # Create an instance of SearchResultsPage after the search results page is loaded
        search_results_page = SearchResultsPage(self.driver)

        # Get the top 5 search results
        top_results = search_results_page.get_top_search_results(5)

        # Verify that the top 5 search results exist
        self.assertGreater(len(top_results), 0, "No search results found.")
        for index, result in enumerate(top_results):
            print(f"Result {index + 1}: {result.text}")
            self.assertIsNotNone(result.text, f"Search result {index + 1} is empty.")
