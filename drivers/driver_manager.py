

class DriverManager(ABC):
    _driver = None
    _browser_name = "chrome"  # Default browser

    #When you define a method with @abstractmethod, you are specifying that
    # subclasses are required to provide an implementation for this method.
    @abstractmethod
    @classmethod
    def _init_driver(self):
        pass

    #Class methods are often used to create factory methods that return an instance of the class.
    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            cls._init_driver()
        return cls._driver

    @classmethod
    def _init_driver(cls):
        raise NotImplementedError("Subclasses should implement this method.")

    @classmethod
    def quit(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
