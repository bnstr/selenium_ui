import unittest

from selenium_ui.src import config_loader
from selenium_ui.src import test_data_manager

def SampleTest(BaseTest):

    def setUp(self):
        # Initialize page objects
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)

    def test_login_and_home_page_elements(self):
        self.login_page.login("username", "password")
        top_nav_bar_elements = self.home_page.top_navigation_bar
        self.assertGreater(len(top_nav_bar_elements), 0, "Top navigation bar elements should be present.")
        search_results = self.home_page.search_results
        self.assertGreater(len(search_results), 0, "Search results should be present.")


if __name__ == "__main__":
    unittest.main()