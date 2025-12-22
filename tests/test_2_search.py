"""
Test 2: Search Functionality
Learn basic element interaction, assertions, and verification.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def test_search():
    print("\n🚀 Starting Test 2: Search Functionality")
    
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)
    
    try:
        # Navigate to page
        print("\n📍 Step 1: Navigate to Herokuapp")
        driver.get("https://the-internet.herokuapp.com/")
        time.sleep(2)
        
        print(f"✅ Page loaded: {driver.title}")
        print(f"✅ Current URL: {driver.current_url}")
        
        driver.save_screenshot("screenshots/search_step1_homepage.png")
        
        # Find all available examples
        print("\n🔍 Step 2: Finding all available test pages...")
        links = driver.find_elements(By.CSS_SELECTOR, "#content ul li a")
        print(f"✅ Found {len(links)} test pages available")
        
        # Display first 10 links
        print("\n📋 Available test pages:")
        for i, link in enumerate(links[:10], 1):
            print(f"  {i}. {link.text}")
        
        # Click on a specific link
        print("\n🔘 Step 3: Clicking on 'Add/Remove Elements'...")
        add_remove_link = driver.find_element(By.LINK_TEXT, "Add/Remove Elements")
        add_remove_link.click()
        time.sleep(2)
        
        print(f"✅ Navigated to: {driver.current_url}")
        driver.save_screenshot("screenshots/search_step2_add_remove.png")
        
        # Verify page heading
        heading = driver.find_element(By.TAG_NAME, "h3").text
        print(f"✅ Page heading: '{heading}'")
        
        # Add elements
        print("\n➕ Step 4: Adding elements...")
        add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
        
        for i in range(3):
            add_button.click()
            time.sleep(0.5)
            print(f"  ✅ Added element {i+1}")
        
        # Verify elements were added
        delete_buttons = driver.find_elements(By.CSS_SELECTOR, ".added-manually")
        print(f"✅ Total elements added: {len(delete_buttons)}")
        
        driver.save_screenshot("screenshots/search_step3_elements_added.png")
        
        # Remove one element
        print("\n➖ Step 5: Removing one element...")
        if delete_buttons:
            delete_buttons[0].click()
            time.sleep(1)
            print("✅ Removed one element")
        
        # Verify removal
        remaining_buttons = driver.find_elements(By.CSS_SELECTOR, ".added-manually")
        print(f"✅ Elements remaining: {len(remaining_buttons)}")
        
        driver.save_screenshot("screenshots/search_step4_element_removed.png")
        
        # Test assertions
        print("\n✅ Step 6: Running assertions...")
        assert len(remaining_buttons) == 2, "Should have 2 elements remaining"
        print("✅ Assertion passed: Correct number of elements")
        
        # Go back to home
        print("\n🔙 Step 7: Navigating back to home...")
        driver.get("https://the-internet.herokuapp.com/")
        time.sleep(1)
        
        # Verify we're back
        assert "The Internet" in driver.title
        print("✅ Back at homepage")
        
        print("\n🎉 TEST 2 PASSED: Search and Navigation Successful!")
        
        # Summary
        print("\n" + "="*60)
        print("📚 WHAT YOU LEARNED:")
        print("="*60)
        print("✅ Navigate to URLs")
        print("✅ Find single element: find_element()")
        print("✅ Find multiple elements: find_elements()")
        print("✅ Click elements")
        print("✅ Verify text content")
        print("✅ Use assertions")
        print("✅ Take screenshots")
        print("="*60)
        
        print("\n⏸️  Keeping browser open for 3 seconds...")
        time.sleep(3)
        
    except AssertionError as e:
        print(f"\n❌ ASSERTION FAILED: {e}")
        driver.save_screenshot("screenshots/search_assertion_error.png")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        driver.save_screenshot("screenshots/search_error.png")
        
    finally:
        print("\n🧹 Closing browser...")
        driver.quit()
        print("✅ Test completed!\n")

if __name__ == "__main__":
    test_search()
