"""
Login Tests - pytest Version
Demonstrates pytest fixtures and markers
"""

import pytest
import time


@pytest.mark.smoke
@pytest.mark.login
class TestLogin:
    """Login functionality tests using pytest"""
    
    def test_successful_login(self, login_page):
        """Test successful login with valid credentials"""
        
        print("\n🚀 Test: Successful Login")
        
        # Open login page (using fixture!)
        login_page.open_login_page()
        
        assert "Login Page" in login_page.get_page_heading()
        print(f"✅ On login page")
        
        # Login
        print("🔑 Logging in...")
        secure_page = login_page.login("tomsmith", "SuperSecretPassword!")
        
        # Dismiss popup
        secure_page.dismiss_password_manager_popup()
        time.sleep(2)
        
        # Verify success
        assert secure_page.is_on_secure_page()
        print("✅ On secure page")
        
        assert secure_page.is_success_message_displayed()
        print(f"✅ Success: {secure_page.get_success_message()}")
        
        assert "Secure Area" in secure_page.get_page_heading()
        print("✅ Correct heading")
        
        print("🎉 TEST PASSED!")
    
    
    def test_failed_login(self, login_page):
        """Test login with invalid credentials"""
        
        print("\n🚀 Test: Failed Login")
        
        login_page.open_login_page()
        
        print("🔑 Trying wrong password...")
        login_page.enter_username("tomsmith")
        login_page.enter_password("wrongpassword")
        login_page.click_login_button()
        
        login_page.dismiss_password_manager_popup()
        time.sleep(2)
        
        # Verify error
        assert login_page.is_error_displayed()
        error_msg = login_page.get_error_message()
        print(f"✅ Error shown: {error_msg}")
        
        assert "invalid" in error_msg.lower()
        
        print("🎉 TEST PASSED!")
    
    
    @pytest.mark.smoke
    def test_logout(self, logged_in_secure_page):
        """Test logout using fixture that's already logged in"""
        
        print("\n🚀 Test: Logout")
        
        # Already logged in via fixture!
        print("🚪 Logging out...")
        login_page = logged_in_secure_page.click_logout()
        
        login_page.dismiss_password_manager_popup()
        time.sleep(2)
        
        assert "Login Page" in login_page.get_page_heading()
        print("✅ Logged out successfully")
        
        print("🎉 TEST PASSED!")


@pytest.mark.parametrize("username,password", [
    ("", ""),
    ("wronguser", "wrongpass"),
    ("tomsmith", "badpassword"),
])
def test_invalid_credentials(login_page, username, password):
    """Data-driven test with multiple invalid credentials"""
    
    print(f"\n🔑 Testing: user='{username}', pass='{password}'")
    
    login_page.open_login_page()
    
    if username:
        login_page.enter_username(username)
    if password:
        login_page.enter_password(password)
    
    login_page.click_login_button()
    login_page.dismiss_password_manager_popup()
    time.sleep(1)
    
    assert login_page.is_error_displayed()
    print("✅ Error message shown correctly")