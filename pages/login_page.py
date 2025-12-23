"""
Login Page Object
Represents the login page at https://the-internet.herokuapp.com/login
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Login Page object with locators and actions"""
    
    # URL
    URL = "https://the-internet.herokuapp.com/login"
    
    # Locators (using tuples for easy use with WebDriverWait)
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".flash.error")
    PAGE_HEADING = (By.TAG_NAME, "h2")
    
    # Page Actions
    def open_login_page(self):
        """Navigate to login page"""
        self.open(self.URL)
        return self
    
    def enter_username(self, username):
        """Enter username in the username field"""
        self.type(self.USERNAME_INPUT, username)
        return self
    
    def enter_password(self, password):
        """Enter password in the password field"""
        self.type(self.PASSWORD_INPUT, password)
        return self
    
    def click_login_button(self):
        """Click the login button"""
        self.click(self.LOGIN_BUTTON)
    
    def login(self, username, password):
        """
        Complete login action (fluent interface)
        Returns SecurePage object after successful login
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        
        # Import here to avoid circular dependency
        from pages.secure_page import SecurePage
        return SecurePage(self.driver)
    
    def get_error_message(self):
        """Get error message text"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self):
        """Check if error message is displayed"""
        return self.is_displayed(self.ERROR_MESSAGE)
    
    def get_page_heading(self):
        """Get page heading text"""
        return self.get_text(self.PAGE_HEADING)
