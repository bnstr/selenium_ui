

class FirefoxDriverManager(DriverManager):
    @classmethod
    def _init_driver(cls):
        if cls._driver is None:
            service = FirefoxService(GeckoDriverManager().install())
            cls._driver = webdriver.Firefox(service=service)
            cls._driver.delete_all_cookies()
            cls._driver.maximize_window()

