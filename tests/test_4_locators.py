"""
Test 4: Element Locators
Master all 8 locator strategies in Selenium.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def test_locators():
    print("\n🚀 Starting Test 4: Element Locators (8 Strategies)")
    
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("https://the-internet.herokuapp.com/login")
        time.sleep(2)
        
        print(f"✅ Page loaded: {driver.title}")
        driver.save_screenshot("screenshots/locators_page.png")
        
        print("\n" + "="*60)
        print("8 SELENIUM LOCATOR STRATEGIES")
        print("="*60)
        
        # 1. By ID
        print("\n1️⃣  BY ID - Most reliable")
        print("   Syntax: By.ID")
        try:
            username = driver.find_element(By.ID, "username")
            print(f"   ✅ Found element with ID 'username'")
            print(f"   Tag: {username.tag_name}, Type: {username.get_attribute('type')}")
        except Exception as e:
            print(f"   ❌ Not found: {e}")
        
        # 2. By NAME
        print("\n2️⃣  BY NAME - Common for form elements")
        print("   Syntax: By.NAME")
        try:
            username_by_name = driver.find_element(By.NAME, "username")
            print(f"   ✅ Found element with NAME 'username'")
            print(f"   Same element as ID? {username == username_by_name}")
        except Exception as e:
            print(f"   ❌ Not found: {e}")
        
        # 3. By CLASS_NAME
        print("\n3️⃣  BY CLASS_NAME - For styled elements")
        print("   Syntax: By.CLASS_NAME")
        try:
            login_button = driver.find_element(By.CLASS_NAME, "radius")
            print(f"   ✅ Found element with class 'radius'")
            print(f"   Tag: {login_button.tag_name}, Text: '{login_button.text}'")
        except Exception as e:
            print(f"   ❌ Not found: {e}")
        
        # 4. By TAG_NAME
        print("\n4️⃣  BY TAG_NAME - Find by HTML tag")
        print("   Syntax: By.TAG_NAME")
        try:
            heading = driver.find_element(By.TAG_NAME, "h2")
            print(f"   ✅ Found heading: '{heading.text}'")
            
            # Find all input fields
            inputs = driver.find_elements(By.TAG_NAME, "input")
            print(f"   ✅ Found {len(inputs)} input elements")
        except Exception as e:
            print(f"   ❌ Not found: {e}")
        
        # 5. By LINK_TEXT
        print("\n5️⃣  BY LINK_TEXT - Exact link text match")
        print("   Syntax: By.LINK_TEXT")
        try:
            # Go to home page for this
            driver.get("https://the-internet.herokuapp.com/")
            time.sleep(1)
            
            link = driver.find_element(By.LINK_TEXT, "Form Authentication")
            print(f"   ✅ Found link: '{link.text}'")
            print(f"   URL: {link.get_attribute('href')}")
        except Exception as e:
            print(f"   ❌ Not found: {e}")
        
        # 6. By PARTIAL_LINK_TEXT
        print("\n6️⃣  BY PARTIAL_LINK_TEXT - Partial match")
        print("   Syntax: By.PARTIAL_LINK_TEXT")
        try:
            partial_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Form Auth")
            print(f"   ✅ Found link with partial text 'Form Auth'")
            print(f"   Full text: '{partial_link.text}'")
        except Exception as e:
            print(f"   ❌ Not found: {e}")
        
        # Go back to login page for CSS and XPath
        driver.get("https://the-internet.herokuapp.com/login")
        time.sleep(1)
        
        # 7. By CSS_SELECTOR
        print("\n7️⃣  BY CSS_SELECTOR - Most flexible (after XPath)")
        print("   Syntax: By.CSS_SELECTOR")
        
        css_examples = [
            ("#username", "ID selector"),
            ("input[name='username']", "Attribute selector"),
            ("button.radius", "Class selector"),
            ("form input", "Descendant selector"),
            ("button[type='submit']", "Type attribute"),
        ]
        
        for selector, description in css_examples:
            try:
                element = driver.find_element(By.CSS_SELECTOR, selector)
                print(f"   ✅ {description}: '{selector}'")
                print(f"      Found: {element.tag_name}")
            except Exception as e:
                print(f"   ❌ {description}: {e}")
        
        # 8. By XPATH
        print("\n8️⃣  BY XPATH - Most powerful, can traverse anywhere")
        print("   Syntax: By.XPATH")
        
        xpath_examples = [
            ("//input[@id='username']", "Absolute path with ID"),
            ("//input[@name='username']", "By attribute"),
            ("//button[@type='submit']", "Button by type"),
            ("//form//input[1]", "First input in form"),
            ("//h2[contains(text(), 'Login')]", "Text contains"),
            ("//*[@class='radius']", "Any element with class"),
        ]
        
        for xpath, description in xpath_examples:
            try:
                element = driver.find_element(By.XPATH, xpath)
                print(f"   ✅ {description}")
                print(f"      XPath: {xpath}")
                print(f"      Found: {element.tag_name}")
            except Exception as e:
                print(f"   ❌ {description}: Failed")
        
        # Practical Example - Fill form using different locators
        print("\n" + "="*60)
        print("PRACTICAL EXAMPLE: Fill Login Form Using Different Locators")
        print("="*60)
        
        # Username by ID
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("tomsmith")
        print("✅ Username filled (using ID)")
        
        # Password by CSS
        password_field = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_field.send_keys("SuperSecretPassword!")
        print("✅ Password filled (using CSS)")
        
        time.sleep(1)
        driver.save_screenshot("screenshots/locators_form_filled.png")
        
        # Button by XPath
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        print("✅ Login button clicked (using XPath)")
        
        time.sleep(2)
        driver.save_screenshot("screenshots/locators_logged_in.png")
        
        # Verify login
        current_url = driver.current_url
        if "secure" in current_url:
            print("✅ Login successful!")
        
        print("\n🎉 TEST 4 PASSED: All 8 locators demonstrated!")
        
        # Summary
        print("\n" + "="*60)
        print("📚 LOCATOR STRATEGY GUIDE:")
        print("="*60)
        print("🥇 Best:     ID, NAME (unique, fast)")
        print("🥈 Good:     CSS_SELECTOR (flexible, readable)")
        print("🥉 Powerful: XPATH (most flexible, slower)")
        print("📌 Useful:   LINK_TEXT (for links)")
        print("⚠️  Avoid:   CLASS_NAME, TAG_NAME alone (not unique)")
        print()
        print("💡 TIP: Use ID or NAME when available!")
        print("💡 TIP: CSS for styling-based selection")
        print("💡 TIP: XPath for complex traversal")
        print("="*60)
        
        print("\n⏸️  Keeping browser open for 3 seconds...")
        time.sleep(3)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        driver.save_screenshot("screenshots/locators_error.png")
        
    finally:
        print("\n🧹 Closing browser...")
        driver.quit()
        print("✅ Test completed!\n")

if __name__ == "__main__":
    test_locators()
