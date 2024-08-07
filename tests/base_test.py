# tests/test_suite.py
import unittest

from selenium_ui.src.config_loader import ConfigLoader
from selenium_ui.src.test_data_manager import TestDataManager


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize configuration loader and test data manager
        cls.config_loader = ConfigLoader()
        cls.test_data_manager = TestDataManager(os.getenv('ENV', 'development'))

        # Load configuration and test data
        cls.base_url = cls.config_loader.get('base_url')
        cls.credentials = cls.config_loader.get('credentials')
        cls.test_data = cls.test_data_manager.get_test_data('sample_data')

        # Initialize WebDriver
        cls.browser_type = DriverType.CHROME  # or DriverType.FIREFOX, DriverType.EDGE, etc.
        cls.driver_manager = DriverManagerFactory.get_manager(cls.browser_type)
        cls.driver = cls.driver_manager.get_driver()


    @classmethod
    def tearDownClass(cls):
        print("Tearing down class...")
        cls.driver_manager.quit()


