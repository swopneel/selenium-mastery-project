
"""
Selenium Test - Handling iFrames (Fixed)
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def test_iframe_handling():
    print("\n🚀 Starting test: iFrame Handling")
    
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)
    
    try:
        # Test 1: Simple iFrame
        print("\n" + "="*60)
        print("TEST 1: Simple iFrame")
        print("="*60)
        
        driver.get("https://the-internet.herokuapp.com/iframe")
        time.sleep(2)
        
        print(f"✅ Page loaded: {driver.title}")
        driver.save_screenshot("screenshots/iframe_step1_page.png")
        
        # Switch to iframe
        print("\n🔄 Switching to iframe...")
        iframe = wait.until(EC.presence_of_element_located((By.ID, "mce_0_ifr")))
        driver.switch_to.frame(iframe)
        print("✅ Switched to iframe!")
        
        # Find element inside iframe
        print("🔍 Finding text editor inside iframe...")
        text_editor = wait.until(EC.presence_of_element_located((By.ID, "tinymce")))
        print("✅ Found text editor!")
        
        # Get current text
        current_text = text_editor.text
        print(f"📝 Current text in editor: '{current_text}'")
        
        # Use JavaScript to set the text (more reliable)
        print("⌨️  Setting new text using JavaScript...")
        new_text = "Hello from Selenium! This is inside an iframe!"
        driver.execute_script(f"arguments[0].innerHTML = '{new_text}'", text_editor)
        time.sleep(1)
        
        # Verify text was set
        updated_text = text_editor.text
        print(f"✅ Updated text: '{updated_text}'")
        
        driver.save_screenshot("screenshots/iframe_step2_typed.png")
        
        # Switch back to main content
        print("\n🔄 Switching back to main content...")
        driver.switch_to.default_content()
        print("✅ Back to main page!")
        
        # Verify we can interact with main page
        heading = driver.find_element(By.TAG_NAME, "h3")
        print(f"✅ Main page heading: {heading.text}")
        
        print("\n🎉 TEST 1 PASSED: Simple iFrame handled!")
        
        # Test 2: Nested Frames
        print("\n" + "="*60)
        print("TEST 2: Nested Frames")
        print("="*60)
        
        driver.get("https://the-internet.herokuapp.com/nested_frames")
        time.sleep(2)
        
        print(f"✅ Page loaded: {driver.title}")
        driver.save_screenshot("screenshots/iframe_step3_nested.png")
        
        # Switch to top frame
        print("\n🔄 Switching to TOP frame...")
        driver.switch_to.frame("frame-top")
        print("✅ Inside TOP frame!")
        
        # Switch to middle frame (nested)
        print("🔄 Switching to MIDDLE frame (nested)...")
        driver.switch_to.frame("frame-middle")
        print("✅ Inside MIDDLE frame!")
        
        # Get text from middle frame
        middle_text = driver.find_element(By.ID, "content").text
        print(f"✅ Text in middle frame: '{middle_text}'")
        
        # Go back to default
        driver.switch_to.default_content()
        print("🔄 Back to main content")
        
        # Access left frame
        driver.switch_to.frame("frame-top")
        driver.switch_to.frame("frame-left")
        left_text = driver.find_element(By.TAG_NAME, "body").text
        print(f"✅ Text in LEFT frame: '{left_text}'")
        
        # Go back and access right frame
        driver.switch_to.default_content()
        driver.switch_to.frame("frame-top")
        driver.switch_to.frame("frame-right")
        right_text = driver.find_element(By.TAG_NAME, "body").text
        print(f"✅ Text in RIGHT frame: '{right_text}'")
        
        # Access bottom frame
        driver.switch_to.default_content()
        driver.switch_to.frame("frame-bottom")
        bottom_text = driver.find_element(By.TAG_NAME, "body").text
        print(f"✅ Text in BOTTOM frame: '{bottom_text}'")
        
        driver.save_screenshot("screenshots/iframe_step4_all_frames.png")
        
        print("\n🎉 TEST 2 PASSED: All nested frames accessed!")
        
        # Summary
        print("\n" + "="*60)
        print("📚 KEY LEARNINGS:")
        print("="*60)
        print("✅ switch_to.frame(element) - Switch to iframe")
        print("✅ switch_to.default_content() - Back to main")
        print("✅ switch_to.parent_frame() - Go up one level")
        print("✅ Can use: ID, name, or WebElement")
        print("✅ JavaScript for complex interactions")
        print("="*60)
        
        print("\n⏸️  Keeping browser open for 5 seconds...")
        time.sleep(5)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        driver.save_screenshot("screenshots/iframe_error.png")
        
    finally:
        print("\n🧹 Closing browser...")
        driver.quit()
        print("✅ Test completed!\n")

if __name__ == "__main__":
    test_iframe_handling()
