from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage

class GoogleSearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_box = (By.NAME, "q")
        self.search_results = (By.CSS_SELECTOR, "div.g")

    def search(self, query):
        search_box = self.wait_for_element(self.search_box)
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

    def get_search_results(self):
        return self.find_elements(self.search_results)