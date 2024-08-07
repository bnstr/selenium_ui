from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage  # Adjust import based on actual file structure

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Define locators for home page elements
        self._search_field_locator = (By.CSS_SELECTOR, "input[name='q']")
        self._top_navigation_bar_locator = (By.CSS_SELECTOR, "[role='navigation'] div[data-id='trc'] [role='listitem']")
        self._search_results_locator = (By.CSS_SELECTOR, "#search .MjjYud")

    @property
    def search_field(self):
        # Return the search input field element
        return self.wait_for_element(self._search_field_locator)

    @property
    def top_navigation_bar(self):
        # Return a list of elements in the top navigation bar
        return self.find_elements(self._top_navigation_bar_locator)

    @property
    def search_results(self):
        # Return a list of search result elements
        return self.find_elements(self._search_results_locator)

    def perform_search(self, query):
        # Clear and enter the search query, then submit
        search_field = self.search_field
        search_field.clear()
        search_field.send_keys(query)
        search_field.submit()  # Assuming search is triggered by hitting Enter
