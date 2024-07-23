from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage

class GoogleSearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._search_box_locator = (By.NAME, "q")
        self._search_results_locator = (By.CSS_SELECTOR, "#search .MjjYud")

    @property
    def search_box(self):
        return self.wait_for_element(self._search_box_locator)

    @property
    def search_results(self):
        return self.find_elements(self._search_results_locator)

    def search(self, query):
        search_box = self.search_box
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
