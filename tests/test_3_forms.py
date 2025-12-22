"""
Test 3: Form Filling
Learn how to fill forms, handle different input types, and validate data.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time

def test_forms():
    print("\n🚀 Starting Test 3: Form Filling")
    
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)
    
    try:
        # Test 1: Basic Form
        print("\n" + "="*60)
        print("PART 1: Basic Form Input")
        print("="*60)
        
        driver.get("https://the-internet.herokuapp.com/inputs")
        time.sleep(2)
        
        print(f"✅ Page loaded: {driver.title}")
        driver.save_screenshot("screenshots/forms_step1_inputs_page.png")
        
        # Find input field
        print("\n🔍 Finding input field...")
        number_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='number']")))
        print("✅ Found number input field")
        
        # Type numbers
        print("\n⌨️  Typing number: 12345")
        number_input.clear()
        number_input.send_keys("12345")
        time.sleep(1)
        
        # Get the value
        entered_value = number_input.get_attribute("value")
        print(f"✅ Value entered: {entered_value}")
        
        driver.save_screenshot("screenshots/forms_step2_number_entered.png")
        
        # Clear and enter new value
        print("\n🔄 Clearing and entering new value: 99999")
        number_input.clear()
        number_input.send_keys("99999")
        time.sleep(1)
        
        new_value = number_input.get_attribute("value")
        print(f"✅ New value: {new_value}")
        
        assert new_value == "99999", "Value should be 99999"
        print("✅ Assertion passed!")
        
        # Test 2: Checkboxes
        print("\n" + "="*60)
        print("PART 2: Checkboxes")
        print("="*60)
        
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        time.sleep(2)
        
        print(f"✅ Page loaded")
        driver.save_screenshot("screenshots/forms_step3_checkboxes.png")
        
        # Find all checkboxes
        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        print(f"✅ Found {len(checkboxes)} checkboxes")
        
        # Check initial states
        print("\n📊 Initial states:")
        for i, cb in enumerate(checkboxes, 1):
            state = "✅ Checked" if cb.is_selected() else "☐ Unchecked"
            print(f"  Checkbox {i}: {state}")
        
        # Toggle all checkboxes
        print("\n🔄 Toggling all checkboxes...")
        for i, cb in enumerate(checkboxes, 1):
            before = cb.is_selected()
            cb.click()
            time.sleep(0.3)
            after = cb.is_selected()
            print(f"  Checkbox {i}: {before} → {after}")
        
        driver.save_screenshot("screenshots/forms_step4_checkboxes_toggled.png")
        
        # Test 3: Dropdown
        print("\n" + "="*60)
        print("PART 3: Dropdown Selection")
        print("="*60)
        
        driver.get("https://the-internet.herokuapp.com/dropdown")
        time.sleep(2)
        
        print(f"✅ Page loaded")
        driver.save_screenshot("screenshots/forms_step5_dropdown.png")
        
        # Find dropdown
        dropdown_element = driver.find_element(By.ID, "dropdown")
        dropdown = Select(dropdown_element)
        
        # Get all options
        options = dropdown.options
        print(f"\n📋 Dropdown has {len(options)} options:")
        for i, opt in enumerate(options):
            print(f"  {i}: {opt.text}")
        
        # Select by visible text
        print("\n🔘 Selecting 'Option 1'...")
        dropdown.select_by_visible_text("Option 1")
        time.sleep(1)
        
        selected = dropdown.first_selected_option.text
        print(f"✅ Selected: {selected}")
        assert selected == "Option 1"
        
        driver.save_screenshot("screenshots/forms_step6_option1.png")
        
        # Select by value
        print("\n🔘 Selecting 'Option 2' by value...")
        dropdown.select_by_value("2")
        time.sleep(1)
        
        selected = dropdown.first_selected_option.text
        print(f"✅ Selected: {selected}")
        assert selected == "Option 2"
        
        driver.save_screenshot("screenshots/forms_step7_option2.png")
        
        # Test 4: Text Areas
        print("\n" + "="*60)
        print("PART 4: Key Presses (Special Keys)")
        print("="*60)
        
        driver.get("https://the-internet.herokuapp.com/key_presses")
        time.sleep(2)
        
        print(f"✅ Page loaded")
        
        from selenium.webdriver.common.keys import Keys
        
        # Find input field
        key_input = driver.find_element(By.ID, "target")
        
        # Test different keys
        test_keys = [
            ("ENTER", Keys.ENTER),
            ("TAB", Keys.TAB),
            ("ESCAPE", Keys.ESCAPE),
            ("SPACE", Keys.SPACE),
            ("ARROW_UP", Keys.ARROW_UP),
            ("ARROW_DOWN", Keys.ARROW_DOWN),
        ]
        
        print("\n⌨️  Testing special keys:")
        for key_name, key_code in test_keys:
            key_input.clear()
            key_input.send_keys(key_code)
            time.sleep(0.5)
            
            # Get result
            result = driver.find_element(By.ID, "result").text
            print(f"  {key_name}: {result}")
        
        driver.save_screenshot("screenshots/forms_step8_keys.png")
        
        print("\n🎉 TEST 3 PASSED: All form interactions successful!")
        
        # Summary
        print("\n" + "="*60)
        print("📚 WHAT YOU LEARNED:")
        print("="*60)
        print("✅ Fill text inputs")
        print("✅ Clear input fields")
        print("✅ Get input values with .get_attribute('value')")
        print("✅ Handle checkboxes with .is_selected()")
        print("✅ Use Select class for dropdowns")
        print("✅ Select by text, value, or index")
        print("✅ Send special keys (Enter, Tab, etc.)")
        print("✅ Use assertions to verify")
        print("="*60)
        
        print("\n⏸️  Keeping browser open for 3 seconds...")
        time.sleep(3)
        
    except AssertionError as e:
        print(f"\n❌ ASSERTION FAILED: {e}")
        driver.save_screenshot("screenshots/forms_assertion_error.png")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        driver.save_screenshot("screenshots/forms_error.png")
        
    finally:
        print("\n🧹 Closing browser...")
        driver.quit()
        print("✅ Test completed!\n")

if __name__ == "__main__":
    test_forms()
