import unittest
from base_test import BaseTest  # Adjust import based on actual file structure
from selenium_ui.pages.home_page import HomePage


class SampleTest(BaseTest):
    def setUp(self):
        super().setUp()
        # Initialize HomePage for tests
        self.home_page = HomePage(self.driver)

    def test_navigation_bar_elements(self):
        # Verify that top navigation bar elements are present
        top_nav_bar_elements = self.home_page.top_navigation_bar
        self.assertGreater(len(top_nav_bar_elements), 0, "Top navigation bar elements should be present.")

    def test_search_results(self):
        # Perform a search and verify search results
        self.home_page.perform_search("test query")
        search_results = self.home_page.search_results
        self.assertGreater(len(search_results), 0, "Search results should be present.")

if __name__ == "__main__":
    unittest.main()
