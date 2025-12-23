"""
Base Page - Foundation of Page Object Model

PURPOSE:
    This is the parent class that all page objects inherit from.
    It contains common methods used across all pages.

WHY WE NEED IT:
    Instead of writing click(), type(), wait() in every page object,
    we write them ONCE here and all pages inherit them.

INTERVIEW TIP:
    "I use a BasePage class with common methods that all page objects
    inherit. This follows DRY principle and reduces code duplication."
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class BasePage:
    """
    Base class for all page objects
    
    This class provides common functionality that every page needs:
    - Finding elements
    - Clicking elements  
    - Typing text
    - Waiting for elements
    - Taking screenshots
    """
    
    def __init__(self, driver):
        """
        Initialize BasePage with WebDriver instance
        
        Args:
            driver: Selenium WebDriver instance
            
        CONCEPT: Every page object gets the same driver instance,
                 so they can all control the same browser session.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Default 10 second wait
    
    # ==================== NAVIGATION METHODS ====================
    
    def open(self, url):
        """Navigate to a URL"""
        self.driver.get(url)
    
    def get_title(self):
        """Get current page title"""
        return self.driver.title
    
    def get_current_url(self):
        """Get current URL"""
        return self.driver.current_url
    
    # ==================== ELEMENT INTERACTION METHODS ====================
    
    def find_element(self, locator):
        """Find a single element with explicit wait"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        """Find multiple elements with wait"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click(self, locator):
        """Click an element (with wait for clickability)"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def type(self, locator, text):
        """Type text into an input field"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Get text from an element"""
        element = self.find_element(locator)
        return element.text
    
    def is_displayed(self, locator):
        """Check if element is displayed on page"""
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except TimeoutException:
            return False
    
    def is_enabled(self, locator):
        """Check if element is enabled (not disabled)"""
        element = self.find_element(locator)
        return element.is_enabled()
    
    # ==================== ADVANCED WAIT METHODS ====================
    
    def wait_for_element_visible(self, locator, timeout=10):
        """Wait for element to be visible"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))
    
    def wait_for_element_clickable(self, locator, timeout=10):
        """Wait for element to be clickable"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))
    
    def wait_for_url_contains(self, text, timeout=10):
        """Wait for URL to contain specific text"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.url_contains(text))
    
    # ==================== UTILITY METHODS ====================
    
    def take_screenshot(self, filename):
        """Take a screenshot"""
        self.driver.save_screenshot(f"screenshots/{filename}")
    
    def dismiss_password_manager_popup(self):
        """
        Wait for Chrome password manager pop-up and dismiss it
        
        Waits up to 5 seconds for the pop-up to appear, then clicks OK.
        Takes screenshot before and after for documentation.
        
        Returns:
            bool: True if pop-up was found and dismissed, False otherwise
        """
        import time
        
        try:
            print("⏳ Waiting for password manager pop-up...")
            
            # Wait up to 5 seconds for the OK button to appear
            wait = WebDriverWait(self.driver, 5)
            ok_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']"))
            )
            
            print("✅ Pop-up detected!")
            
            # Take screenshot WITH pop-up visible
            self.take_screenshot("password_popup_VISIBLE.png")
            print("📸 Screenshot: Pop-up visible")
            
            # Click OK to dismiss
            ok_button.click()
            print("✅ Clicked OK on password manager pop-up")
            
            # Wait a moment for it to disappear
            time.sleep(1)
            
            # Take screenshot AFTER dismissing
            self.take_screenshot("password_popup_DISMISSED.png")
            print("📸 Screenshot: Pop-up dismissed")
            
            return True
            
        except:
            # Pop-up didn't appear within 5 seconds
            print("ℹ️  No password pop-up detected")
            return False