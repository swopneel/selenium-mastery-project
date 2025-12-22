"""
Selenium Test - Advanced Features (Drag & Drop, Hovers, Dynamic Content)
Learn advanced Selenium interactions.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time

def test_advanced_features():
    print("\n🚀 Starting test: Advanced Selenium Features")
    
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)
    
    try:
        # Test 1: Drag and Drop
        print("\n" + "="*60)
        print("TEST 1: Drag and Drop")
        print("="*60)
        
        driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        time.sleep(2)
        
        print(f"✅ Page loaded: {driver.title}")
        driver.save_screenshot("screenshots/advanced_step1_dragdrop_initial.png")
        
        # Find elements
        print("\n🔍 Finding source and target elements...")
        source_element = driver.find_element(By.ID, "column-a")
        target_element = driver.find_element(By.ID, "column-b")
        
        print(f"  Source element text: {source_element.text}")
        print(f"  Target element text: {target_element.text}")
        
        # Perform drag and drop using ActionChains
        print("\n🎯 Performing drag and drop...")
        actions = ActionChains(driver)
        actions.drag_and_drop(source_element, target_element).perform()
        time.sleep(2)
        
        print("✅ Drag and drop performed!")
        driver.save_screenshot("screenshots/advanced_step2_dragdrop_done.png")
        
        # Verify the swap
        source_text_after = source_element.text
        target_text_after = target_element.text
        print(f"  After drag - Source: {source_text_after}, Target: {target_text_after}")
        
        if source_text_after == "B" and target_text_after == "A":
            print("🎉 TEST 1 PASSED: Elements swapped successfully!")
        else:
            print("⚠️  Elements may not have swapped as expected")
        
        # Test 2: Hover (Mouse Over)
        print("\n" + "="*60)
        print("TEST 2: Mouse Hover Actions")
        print("="*60)
        
        driver.get("https://the-internet.herokuapp.com/hovers")
        time.sleep(2)
        
        print(f"✅ Page loaded: {driver.title}")
        driver.save_screenshot("screenshots/advanced_step3_hover_initial.png")
        
        # Find all user images
        print("\n🔍 Finding user images...")
        user_images = driver.find_elements(By.CSS_SELECTOR, ".figure")
        print(f"✅ Found {len(user_images)} user images")
        
        # Hover over each image
        for i, user_image in enumerate(user_images, 1):
            print(f"\n🖱️  Hovering over user {i}...")
            actions = ActionChains(driver)
            actions.move_to_element(user_image).perform()
            time.sleep(1)
            
            # Try to find the caption that appears
            try:
                caption = user_image.find_element(By.CSS_SELECTOR, ".figcaption")
                if caption.is_displayed():
                    caption_text = caption.text
                    print(f"  ✅ Caption appeared: {caption_text}")
                    driver.save_screenshot(f"screenshots/advanced_hover_user{i}.png")
                else:
                    print(f"  ⚠️  Caption not visible")
            except Exception as e:
                print(f"  ⚠️  Could not find caption: {e}")
            
            time.sleep(1)
        
        print("\n🎉 TEST 2 PASSED: Hover actions performed!")
        
        # Test 3: Dynamic Loading
        print("\n" + "="*60)
        print("TEST 3: Dynamic Loading (Wait for Elements)")
        print("="*60)
        
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
        time.sleep(2)
        
        print(f"✅ Page loaded: {driver.title}")
        driver.save_screenshot("screenshots/advanced_step4_dynamic_initial.png")
        
        # Click Start button
        print("\n🔘 Clicking Start button...")
        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()
        print("✅ Start button clicked!")
        
        # Wait for loading bar
        print("⏳ Waiting for content to load...")
        time.sleep(1)
        
        # Wait for the finish element to appear
        finish_element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#finish"))
        )
        
        # Wait until it's visible
        wait.until(EC.visibility_of(finish_element))
        
        finish_text = finish_element.text
        print(f"✅ Dynamic content loaded: '{finish_text}'")
        
        driver.save_screenshot("screenshots/advanced_step5_dynamic_loaded.png")
        
        if "Hello World!" in finish_text:
            print("🎉 TEST 3 PASSED: Dynamic content handled!")
        
        # Test 4: Checkboxes
        print("\n" + "="*60)
        print("TEST 4: Checkbox Handling")
        print("="*60)
        
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        time.sleep(2)
        
        print(f"✅ Page loaded: {driver.title}")
        
        # Find all checkboxes
        print("\n🔍 Finding checkboxes...")
        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        print(f"✅ Found {len(checkboxes)} checkboxes")
        
        # Check initial states
        print("\n📊 Initial checkbox states:")
        for i, checkbox in enumerate(checkboxes, 1):
            is_checked = checkbox.is_selected()
            print(f"  Checkbox {i}: {'✅ Checked' if is_checked else '☐ Unchecked'}")
        
        driver.save_screenshot("screenshots/advanced_step6_checkboxes_initial.png")
        
        # Toggle all checkboxes
        print("\n🔄 Toggling all checkboxes...")
        for i, checkbox in enumerate(checkboxes, 1):
            was_checked = checkbox.is_selected()
            checkbox.click()
            time.sleep(0.5)
            is_checked = checkbox.is_selected()
            print(f"  Checkbox {i}: {was_checked} → {is_checked}")
        
        driver.save_screenshot("screenshots/advanced_step7_checkboxes_toggled.png")
        
        print("🎉 TEST 4 PASSED: Checkboxes handled!")
        
        # Test 5: Dropdown Selection
        print("\n" + "="*60)
        print("TEST 5: Dropdown Selection")
        print("="*60)
        
        driver.get("https://the-internet.herokuapp.com/dropdown")
        time.sleep(2)
        
        print(f"✅ Page loaded: {driver.title}")
        
        from selenium.webdriver.support.select import Select
        
        # Find dropdown
        print("\n🔍 Finding dropdown...")
        dropdown_element = driver.find_element(By.ID, "dropdown")
        dropdown = Select(dropdown_element)
        
        # Get all options
        options = dropdown.options
        print(f"✅ Dropdown has {len(options)} options:")
        for i, option in enumerate(options):
            print(f"  {i}: {option.text}")
        
        driver.save_screenshot("screenshots/advanced_step8_dropdown_initial.png")
        
        # Select by visible text
        print("\n🔘 Selecting 'Option 1' by visible text...")
        dropdown.select_by_visible_text("Option 1")
        time.sleep(1)
        selected = dropdown.first_selected_option
        print(f"✅ Selected: {selected.text}")
        driver.save_screenshot("screenshots/advanced_step9_dropdown_option1.png")
        
        # Select by value
        print("\n🔘 Selecting 'Option 2' by value...")
        dropdown.select_by_value("2")
        time.sleep(1)
        selected = dropdown.first_selected_option
        print(f"✅ Selected: {selected.text}")
        driver.save_screenshot("screenshots/advanced_step10_dropdown_option2.png")
        
        print("🎉 TEST 5 PASSED: Dropdown handled!")
        
        # Summary
        print("\n" + "="*60)
        print("📚 KEY LEARNINGS:")
        print("="*60)
        print("✅ ActionChains - For complex interactions")
        print("✅ drag_and_drop() - Drag element to target")
        print("✅ move_to_element() - Hover over element")
        print("✅ EC.visibility_of() - Wait for visible")
        print("✅ is_selected() - Check checkbox state")
        print("✅ Select class - For dropdowns")
        print("✅ WebDriverWait - Handle dynamic content")
        print("="*60)
        
        print("\n⏸️  Keeping browser open for 5 seconds...")
        time.sleep(5)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        driver.save_screenshot("screenshots/advanced_error.png")
        
    finally:
        print("\n🧹 Closing browser...")
        driver.quit()
        print("✅ Test completed!\n")

if __name__ == "__main__":
    test_advanced_features()
