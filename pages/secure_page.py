"""
Secure Page Object
Represents the secure area page after successful login
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SecurePage(BasePage):
    """Secure Area Page object"""
    
    # URL
    URL = "https://the-internet.herokuapp.com/secure"
    
    # Locators
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".flash.success")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href='/logout']")
    PAGE_HEADING = (By.TAG_NAME, "h2")
    
    # Page Actions
    def get_success_message(self):
        """Get success message text"""
        return self.get_text(self.SUCCESS_MESSAGE)
    
    def is_success_message_displayed(self):
        """Check if success message is displayed"""
        return self.is_displayed(self.SUCCESS_MESSAGE)
    
    def get_page_heading(self):
        """Get page heading text"""
        return self.get_text(self.PAGE_HEADING)
    
    def is_on_secure_page(self):
        """Verify we're on the secure page"""
        return "secure" in self.get_current_url()
    
    def is_logout_button_displayed(self):
        """Check if logout button is displayed"""
        return self.is_displayed(self.LOGOUT_BUTTON)
    
    def click_logout(self):
        """
        Click logout button - handles success banner overlay
        
        Note: Banner screenshot should be taken before calling this method,
        as the banner auto-fades quickly.
        
        Process:
            1. Close success banner (if present)
            2. Capture screenshot with banner closed
            3. Click logout button
            4. Capture screenshot of login page
        
        Returns:
            LoginPage: Page object for the login page
        """
        import time
        
        # Close the success message banner if present
        try:
            close_button = self.driver.find_element(By.CSS_SELECTOR, ".flash .close")
            close_button.click()
            print("✅ Clicked X to close banner")
            time.sleep(1)  # Wait for banner to disappear
            
            # NOW capture - banner is definitely gone
            self.take_screenshot("secure_page_banner_CLOSED.png")
            print("📸 Screenshot taken AFTER closing banner")
            
        except:
            print("⚠️  Banner not found (may have auto-closed)")
            pass
        
        # Click logout using JavaScript (more reliable)
        logout_btn = self.driver.find_element(*self.LOGOUT_BUTTON)
        self.driver.execute_script("arguments[0].click();", logout_btn)
        print("✅ Clicked logout button")
        
        # Wait for navigation
        time.sleep(2)
        
        # Capture login page
        self.take_screenshot("after_logout_login_page.png")
        print("📸 Screenshot taken - back on login page")
        
        # Return LoginPage object
        from pages.login_page import LoginPage
        return LoginPage(self.driver)