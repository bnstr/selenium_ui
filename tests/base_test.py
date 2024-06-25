import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.config import IMPLICIT_WAIT
from utils.page_factory import PageFactory

class BaseTest(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Specify the Chrome version here (replace XX with your version number)
        # chrome_version = "126"
        # service = Service(ChromeDriverManager(version=chrome_version).install())
        service = Service(executable_path='/Users/daniel/Downloads/chromedriver')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

        self.driver.implicitly_wait(IMPLICIT_WAIT)
        self.page_factory = PageFactory(self.driver)

    def tearDown(self):
        if self.driver:
            self.driver.quit()