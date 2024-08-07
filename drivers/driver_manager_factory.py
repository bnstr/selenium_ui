

class DriverManagerFactory:
    @staticmethod
    def get_manager(driver_type):
        if driver_type == DriverType.CHROME:
            return ChromeDriverManager()
        elif driver_type == DriverType.FIREFOX:
            return FirefoxDriverManager()
        else:
            raise ValueError(f"Driver type {driver_type} is not supported.")
