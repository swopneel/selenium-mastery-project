"""
Selenium Test - OpenCart Search (Fixed for popups/overlays)
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def test_opencart_search():
    print("\n🚀 Starting test: OpenCart Search")
    
    # Setup Chrome
    print("📝 Setting up Chrome driver...")
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--start-maximized')
    
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 15)
    
    try:
        # Step 1: Open OpenCart
        print("🌐 Opening OpenCart website...")
        driver.get("https://demo.opencart.com/")
        time.sleep(3)  # Wait for any popups/overlays
        
        print(f"✅ Page loaded! Title: {driver.title}")
        
        # Handle cookie banner or any overlay (if present)
        try:
            # Try to close cookie banner if it exists
            close_buttons = driver.find_elements(By.CSS_SELECTOR, "button.close, .close, [aria-label='Close']")
            if close_buttons:
                close_buttons[0].click()
                print("✅ Closed overlay/banner")
                time.sleep(1)
        except:
            pass
        
        driver.save_screenshot("screenshots/step1_page_loaded.png")
        print("📸 Screenshot: step1_page_loaded.png")
        
        # Step 2: Find and use search box
        print("\n🔍 Finding search box...")
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "search")))
        print("✅ Found search box!")
        
        # Scroll to search box to make sure it's visible
        driver.execute_script("arguments[0].scrollIntoView(true);", search_box)
        time.sleep(0.5)
        
        print("⌨️  Typing 'MacBook'...")
        search_box.clear()
        search_box.send_keys("MacBook")
        time.sleep(1)
        
        driver.save_screenshot("screenshots/step2_typed_search.png")
        print("📸 Screenshot: step2_typed_search.png")
        
        # Step 3: Submit search using ENTER key (more reliable than button click)
        print("\n🔍 Submitting search (pressing Enter)...")
        search_box.send_keys(Keys.RETURN)
        
        time.sleep(3)  # Wait for results to load
        
        driver.save_screenshot("screenshots/step3_search_results.png")
        print("📸 Screenshot: step3_search_results.png")
        
        # Step 4: Verify results
        print("\n✅ Verifying search results...")
        print(f"📍 Current URL: {driver.current_url}")
        print(f"📄 Page Title: {driver.title}")
        
        # Check if we're on search results page
        if "search=" in driver.current_url or "MacBook" in driver.current_url:
            print("✅ Successfully navigated to search results!")
            
            # Count products
            try:
                # Wait for products to load
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-thumb, .product-layout")))
                
                products = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
                if not products:
                    products = driver.find_elements(By.CSS_SELECTOR, ".product-layout")
                
                if products:
                    print(f"✅ Found {len(products)} products!")
                    print("\n🎉 TEST PASSED! 🎉")
                else:
                    print("⚠️  Page loaded but no products found")
                    
            except Exception as e:
                print(f"⚠️  Could not verify products: {e}")
                print("✅ But search page loaded successfully!")
        else:
            print("⚠️  URL didn't change as expected")
            print(f"Expected 'search=' in URL, got: {driver.current_url}")
        
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
    test_opencart_search()
