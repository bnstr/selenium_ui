from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage  # Adjust import based on actual file structure

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Define locators for login page elements
        self._user_textfield_locator = (By.CSS_SELECTOR, "input[name='username']")
        self._pass_textfield_locator = (By.CSS_SELECTOR, "input[name='password']")
        self._login_button_locator = (By.CSS_SELECTOR, "button[type='submit']")

    #  the @property decorator allows you to define methods that can be accessed like attributes.
    #  This is useful for providing a clean and intuitive API, especially in page object models where you want to
    #  expose certain attributes of your page objects without requiring explicit method calls.
    @property
    def username_field(self):
        # Return the username input field element
        return self.wait_for_element(self._user_textfield_locator)

    @property
    def password_field(self):
        # Return the password input field element
        return self.wait_for_element(self._pass_textfield_locator)

    @property
    def login_button(self):
        # Return the login button element
        return self.wait_for_element(self._login_button_locator)

    def login(self, username, password):
        # Use properties to interact with elements
        self.username_field.clear()
        self.username_field.send_keys(username)

        self.password_field.clear()
        self.password_field.send_keys(password)

        self.login_button.click()
