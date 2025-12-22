"""
Selenium Test - Login on Herokuapp (No Cloudflare!)
This site is perfect for learning Selenium!
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def test_herokuapp_login():
    print("\n🚀 Starting test: Herokuapp Login")
    
    # Setup Chrome
    print("📝 Setting up Chrome driver...")
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)
    
    try:
        # Step 1: Open the test site
        print("\n🌐 Opening Herokuapp login page...")
        driver.get("https://the-internet.herokuapp.com/login")
        time.sleep(2)
        
        print(f"✅ Page loaded! Title: {driver.title}")
        print(f"📍 URL: {driver.current_url}")
        
        driver.save_screenshot("screenshots/login_step1_page.png")
        print("📸 Screenshot: login_step1_page.png")
        
        # Step 2: Find username field
        print("\n🔍 Finding username field...")
        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        print("✅ Found username field!")
        
        # Step 3: Find password field
        print("🔍 Finding password field...")
        password_field = driver.find_element(By.ID, "password")
        print("✅ Found password field!")
        
        # Step 4: Enter credentials
        print("\n⌨️  Entering username: tomsmith")
        username_field.clear()
        username_field.send_keys("tomsmith")
        
        print("⌨️  Entering password: SuperSecretPassword!")
        password_field.clear()
        password_field.send_keys("SuperSecretPassword!")
        
        time.sleep(1)
        driver.save_screenshot("screenshots/login_step2_credentials.png")
        print("📸 Screenshot: login_step2_credentials.png")
        
        # Step 5: Click login button
        print("\n🔘 Finding and clicking login button...")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        print("✅ Clicked login button!")
        
        time.sleep(2)
        driver.save_screenshot("screenshots/login_step3_result.png")
        print("📸 Screenshot: login_step3_result.png")
        
        # Step 6: Verify successful login
        print("\n✅ Verifying login success...")
        print(f"📍 Current URL: {driver.current_url}")
        
        # Check for success message
        try:
            success_message = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
            )
            message_text = success_message.text
            print(f"✅ Success message: {message_text}")
            
            if "You logged into a secure area!" in message_text:
                print("\n🎉 TEST PASSED! Login successful! 🎉")
            else:
                print("⚠️  Unexpected message")
                
        except:
            print("❌ Could not find success message")
        
        # Step 7: Check for logout button (confirms we're logged in)
        try:
            logout_button = driver.find_element(By.CSS_SELECTOR, "a[href='/logout']")
            print("✅ Found logout button - definitely logged in!")
        except:
            print("⚠️  Logout button not found")
        
        print("\n⏸️  Keeping browser open for 5 seconds...")
        time.sleep(5)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        try:
            driver.save_screenshot("screenshots/error.png")
            print("📸 Error screenshot saved")
        except:
            pass
        
    finally:
        print("\n🧹 Closing browser...")
        driver.quit()
        print("✅ Test completed!")
        print("\n💡 Check screenshots/ folder to see the test execution!\n")

if __name__ == "__main__":
    test_herokuapp_login()
