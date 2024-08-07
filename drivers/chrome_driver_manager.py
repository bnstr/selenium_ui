

class ChromeDriverManager(DriverManager):
    @classmethod
    def _init_driver(cls):
        if cls._driver is None:
            service = Service(ChromeDriverManager().install())
            cls._driver = webdriver.Chrome(service=service)
            cls._driver.delete_all_cookies()
            cls._driver.maximize_window()

