"""
Test Login using Page Object Model
This demonstrates how clean tests become with POM!
"""

import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
import time

# Import page objects
from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from utils.browser_config import get_chrome_options


def test_successful_login_with_pom():
    """Test successful login using Page Object Model"""
    
    print("\n🚀 Starting Test: Login with POM")
    
    # Setup - use configured Chrome options
    driver = webdriver.Chrome(options=get_chrome_options())
    
    try:
        # Step 1: Navigate to login page
        print("\n📍 Step 1: Opening login page...")
        login_page = LoginPage(driver)
        login_page.open_login_page()
        
        # Verify we're on login page
        assert "Login Page" in login_page.get_page_heading()
        print(f"✅ On login page: {login_page.get_page_heading()}")
        
        login_page.take_screenshot("pom_step1_login_page.png")
        
        # Step 2: Enter credentials and login
        print("\n🔑 Step 2: Logging in...")
        print("   Username: tomsmith")
        print("   Password: SuperSecretPassword!")
        
        secure_page = login_page.login("tomsmith", "SuperSecretPassword!")
        
        # IMMEDIATELY check for and dismiss password pop-up
        print("\n🔍 Checking for password manager pop-up...")
        secure_page.dismiss_password_manager_popup()
        
        time.sleep(2)
        
        # Step 3: Verify successful login
        print("\n✅ Step 3: Verifying login success...")

        assert secure_page.is_on_secure_page(), "Should be on secure page"
        print("✅ On secure page")

        assert secure_page.is_success_message_displayed(), "Success message should be displayed"
        print(f"✅ Success message: {secure_page.get_success_message()}")

        # CAPTURE SCREENSHOT IMMEDIATELY - Banner is still visible!
        secure_page.take_screenshot("pom_step2_logged_in_WITH_BANNER.png")
        print("📸 Screenshot taken WITH banner visible!")

        assert "Secure Area" in secure_page.get_page_heading()
        print(f"✅ Page heading: {secure_page.get_page_heading()}")

        assert secure_page.is_logout_button_displayed(), "Logout button should be visible"
        print("✅ Logout button is displayed")
        
        # Step 4: Logout
        print("\n🚪 Step 4: Logging out...")
        login_page = secure_page.click_logout()
        
        # Check for password pop-up after logout
        print("\n🔍 Checking for password manager pop-up after logout...")
        login_page.dismiss_password_manager_popup()
        
        time.sleep(2)
        
        # Verify we're back on login page
        assert "Login Page" in login_page.get_page_heading()
        print("✅ Logged out successfully")
        
        login_page.take_screenshot("pom_step3_logged_out.png")
        
        print("\n🎉 TEST PASSED! POM makes tests so clean!")
        
        time.sleep(3)
        
    except AssertionError as e:
        print(f"\n❌ ASSERTION FAILED: {e}")
        driver.save_screenshot("screenshots/pom_assertion_error.png")
        raise
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        driver.save_screenshot("screenshots/pom_error.png")
        raise
        
    finally:
        print("\n🧹 Closing browser...")
        driver.quit()
        print("✅ Test completed!\n")


def test_failed_login_with_pom():
    """Test failed login using Page Object Model"""
    
    print("\n🚀 Starting Test: Failed Login with POM")
    
    # Setup - use configured Chrome options
    driver = webdriver.Chrome(options=get_chrome_options())
    
    try:
        # Navigate and attempt login with wrong credentials
        print("\n📍 Opening login page...")
        login_page = LoginPage(driver)
        login_page.open_login_page()
        
        print("🔑 Attempting login with wrong password...")
        login_page.enter_username("tomsmith")
        login_page.enter_password("wrongpassword")
        login_page.click_login_button()
        
        # Check for password pop-up
        print("\n🔍 Checking for password manager pop-up...")
        login_page.dismiss_password_manager_popup()
        
        time.sleep(2)
        
        # Verify error message
        print("\n✅ Verifying error message...")
        assert login_page.is_error_displayed(), "Error message should be displayed"
        error_msg = login_page.get_error_message()
        print(f"✅ Error message: {error_msg}")
        
        assert "invalid" in error_msg.lower(), "Error should mention invalid credentials"
        
        login_page.take_screenshot("pom_failed_login.png")
        
        print("\n🎉 TEST PASSED! Error handling works!")
        
        time.sleep(3)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        driver.save_screenshot("screenshots/pom_failed_error.png")
        raise
        
    finally:
        driver.quit()


if __name__ == "__main__":
    test_successful_login_with_pom()
    print("\n" + "="*60 + "\n")
    test_failed_login_with_pom()