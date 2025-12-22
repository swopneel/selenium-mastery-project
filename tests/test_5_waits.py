"""
Test 5: Waits and Synchronization
Master implicit waits, explicit waits, and handling dynamic content.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import time

def test_waits():
    print("\n🚀 Starting Test 5: Waits and Synchronization")
    
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Part 1: Implicit Wait
        print("\n" + "="*60)
        print("PART 1: Implicit Wait")
        print("="*60)
        
        print("\n📝 Setting implicit wait to 10 seconds...")
        driver.implicitly_wait(10)  # Wait up to 10 seconds for elements
        print("✅ Implicit wait set!")
        
        print("\n💡 EXPLANATION:")
        print("   Implicit wait tells Selenium to poll the DOM for a")
        print("   certain amount of time when trying to find elements.")
        print("   It applies to ALL find_element() calls.")
        
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        time.sleep(2)
        
        driver.save_screenshot("screenshots/waits_step1_implicit.png")
        
        # Part 2: Explicit Wait - Presence
        print("\n" + "="*60)
        print("PART 2: Explicit Wait - Presence of Element")
        print("="*60)
        
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
        time.sleep(2)
        
        print("✅ Page loaded")
        driver.save_screenshot("screenshots/waits_step2_before_click.png")
        
        # Click Start button
        print("\n🔘 Clicking Start button...")
        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()
        print("✅ Start clicked - content is loading...")
        
        # Wait explicitly for the element to appear
        print("\n⏳ Waiting for element to appear (explicit wait)...")
        wait = WebDriverWait(driver, 10)
        
        try:
            finish_element = wait.until(
                EC.presence_of_element_located((By.ID, "finish"))
            )
            print("✅ Element appeared!")
            print(f"✅ Text: '{finish_element.text}'")
            
        except TimeoutException:
            print("❌ Element did not appear within 10 seconds")
        
        driver.save_screenshot("screenshots/waits_step3_after_wait.png")
        
        # Part 3: Explicit Wait - Visibility
        print("\n" + "="*60)
        print("PART 3: Explicit Wait - Visibility of Element")
        print("="*60)
        
        print("\n💡 DIFFERENCE:")
        print("   presence_of_element: Element exists in DOM")
        print("   visibility_of_element: Element is visible on page")
        
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        time.sleep(2)
        
        # Start loading
        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()
        print("✅ Loading started...")
        
        # Wait for visibility (not just presence)
        print("\n⏳ Waiting for element to be VISIBLE...")
        try:
            visible_element = wait.until(
                EC.visibility_of_element_located((By.ID, "finish"))
            )
            print("✅ Element is now visible!")
            print(f"✅ Text: '{visible_element.text}'")
            
        except TimeoutException:
            print("❌ Element did not become visible")
        
        driver.save_screenshot("screenshots/waits_step4_visibility.png")
        
        # Part 4: Explicit Wait - Clickability
        print("\n" + "="*60)
        print("PART 4: Explicit Wait - Element to be Clickable")
        print("="*60)
        
        driver.get("https://the-internet.herokuapp.com/dynamic_controls")
        time.sleep(2)
        
        driver.save_screenshot("screenshots/waits_step5_controls.png")
        
        # Remove checkbox
        print("\n🔘 Clicking Remove button...")
        remove_button = driver.find_element(By.CSS_SELECTOR, "#checkbox-example button")
        remove_button.click()
        
        # Wait for it to be gone
        print("⏳ Waiting for checkbox to be removed...")
        try:
            wait.until(
                EC.invisibility_of_element_located((By.ID, "checkbox"))
            )
            print("✅ Checkbox removed!")
        except TimeoutException:
            print("❌ Checkbox still present")
        
        # Wait for Add button to be clickable
        print("\n⏳ Waiting for Add button to be clickable...")
        try:
            add_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkbox-example button"))
            )
            print("✅ Add button is clickable!")
            add_button.click()
            print("✅ Add button clicked!")
            
        except TimeoutException:
            print("❌ Add button not clickable")
        
        time.sleep(2)
        driver.save_screenshot("screenshots/waits_step6_added_back.png")
        
        # Part 5: Explicit Wait - Text to be Present
        print("\n" + "="*60)
        print("PART 5: Explicit Wait - Text to be Present")
        print("="*60)
        
        # Enable input field
        print("\n🔘 Clicking Enable button...")
        enable_button = driver.find_element(By.CSS_SELECTOR, "#input-example button")
        enable_button.click()
        
        # Wait for message to appear
        print("⏳ Waiting for success message...")
        try:
            wait.until(
                EC.text_to_be_present_in_element(
                    (By.ID, "message"),
                    "It's enabled!"
                )
            )
            message = driver.find_element(By.ID, "message").text
            print(f"✅ Message appeared: '{message}'")
            
        except TimeoutException:
            print("❌ Message did not appear")
        
        driver.save_screenshot("screenshots/waits_step7_message.png")
        
        # Part 6: Custom Wait Condition
        print("\n" + "="*60)
        print("PART 6: Custom Wait Condition")
        print("="*60)
        
        print("\n💡 You can create custom wait conditions!")
        
        def element_has_text(locator, text):
            """Custom condition: element contains specific text"""
            def _predicate(driver):
                element = driver.find_element(*locator)
                return text in element.text
            return _predicate
        
        try:
            wait.until(element_has_text((By.ID, "message"), "enabled"))
            print("✅ Custom condition met: Message contains 'enabled'")
        except TimeoutException:
            print("❌ Custom condition not met")
        
        # Summary of all wait types
        print("\n" + "="*60)
        print("📚 ALL EXPLICIT WAIT CONDITIONS:")
        print("="*60)
        
        wait_conditions = [
            "presence_of_element_located",
            "visibility_of_element_located",
            "element_to_be_clickable",
            "invisibility_of_element",
            "text_to_be_present_in_element",
            "title_contains",
            "title_is",
            "url_contains",
            "url_to_be",
            "frame_to_be_available",
            "alert_is_present",
        ]
        
        for i, condition in enumerate(wait_conditions, 1):
            print(f"  {i:2}. {condition}")
        
        print("\n🎉 TEST 5 PASSED: All wait strategies demonstrated!")
        
        # Best Practices
        print("\n" + "="*60)
        print("💡 BEST PRACTICES:")
        print("="*60)
        print("✅ Use explicit waits (more control)")
        print("✅ Set reasonable timeout values (10-15 seconds)")
        print("✅ Avoid time.sleep() (not dynamic)")
        print("✅ Use presence for checking DOM")
        print("✅ Use visibility for UI interaction")
        print("✅ Use clickable before clicking")
        print("❌ Don't mix implicit and explicit waits")
        print("="*60)
        
        print("\n⏸️  Keeping browser open for 3 seconds...")
        time.sleep(3)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        driver.save_screenshot("screenshots/waits_error.png")
        
    finally:
        print("\n🧹 Closing browser...")
        driver.quit()
        print("✅ Test completed!\n")

if __name__ == "__main__":
    test_waits()
