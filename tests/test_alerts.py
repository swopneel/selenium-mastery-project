"""
Selenium Test - Handling JavaScript Alerts, Confirms, and Prompts
Learn how to handle all types of JavaScript popups.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def test_alerts_handling():
    print("\n🚀 Starting test: JavaScript Alerts, Confirms, and Prompts")
    
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(2)
        
        print(f"✅ Page loaded: {driver.title}")
        driver.save_screenshot("screenshots/alerts_step1_page.png")
        
        # Test 1: Simple Alert (OK only)
        print("\n" + "="*60)
        print("TEST 1: Simple Alert (JS Alert)")
        print("="*60)
        
        print("🔘 Clicking 'Click for JS Alert' button...")
        alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
        alert_button.click()
        
        print("⏳ Waiting for alert to appear...")
        alert = wait.until(EC.alert_is_present())
        print(f"✅ Alert appeared!")
        print(f"📝 Alert text: '{alert.text}'")
        
        # Accept alert BEFORE taking screenshot
        print("✅ Accepting alert (clicking OK)...")
        alert.accept()
        time.sleep(1)
        
        result = driver.find_element(By.ID, "result").text
        print(f"✅ Result: {result}")
        
        driver.save_screenshot("screenshots/alerts_step2_accepted.png")
        print("🎉 TEST 1 PASSED: Simple alert handled!")
        
        # Test 2: Confirm (OK or Cancel)
        print("\n" + "="*60)
        print("TEST 2: Confirm Alert (OK and Cancel options)")
        print("="*60)
        
        print("🔘 Clicking 'Click for JS Confirm' button...")
        confirm_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
        confirm_button.click()
        
        print("⏳ Waiting for confirm dialog...")
        confirm_alert = wait.until(EC.alert_is_present())
        print(f"✅ Confirm appeared!")
        print(f"📝 Confirm text: '{confirm_alert.text}'")
        
        print("✅ Accepting confirm (clicking OK)...")
        confirm_alert.accept()
        time.sleep(1)
        
        result = driver.find_element(By.ID, "result").text
        print(f"✅ Result after OK: {result}")
        
        # Now try dismissing (Cancel)
        print("\n🔘 Testing Cancel option...")
        confirm_button.click()
        time.sleep(0.5)
        
        confirm_alert = wait.until(EC.alert_is_present())
        print("❌ Dismissing confirm (clicking Cancel)...")
        confirm_alert.dismiss()
        time.sleep(1)
        
        result = driver.find_element(By.ID, "result").text
        print(f"✅ Result after Cancel: {result}")
        
        driver.save_screenshot("screenshots/alerts_step3_confirm.png")
        print("🎉 TEST 2 PASSED: Confirm handled (both OK and Cancel)!")
        
        # Test 3: Prompt (Input text)
        print("\n" + "="*60)
        print("TEST 3: Prompt Alert (Text Input)")
        print("="*60)
        
        print("🔘 Clicking 'Click for JS Prompt' button...")
        prompt_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
        prompt_button.click()
        
        print("⏳ Waiting for prompt dialog...")
        prompt_alert = wait.until(EC.alert_is_present())
        print(f"✅ Prompt appeared!")
        print(f"📝 Prompt text: '{prompt_alert.text}'")
        
        # Type text in prompt
        test_text = "Hello from Selenium Automation!"
        print(f"⌨️  Typing: '{test_text}'")
        prompt_alert.send_keys(test_text)
        time.sleep(0.5)
        
        print("✅ Accepting prompt...")
        prompt_alert.accept()
        time.sleep(1)
        
        result = driver.find_element(By.ID, "result").text
        print(f"✅ Result: {result}")
        
        driver.save_screenshot("screenshots/alerts_step4_prompt.png")
        print("🎉 TEST 3 PASSED: Prompt handled with text input!")
        
        # Test 4: Prompt with Cancel
        print("\n🔘 Testing prompt Cancel...")
        prompt_button.click()
        time.sleep(0.5)
        
        prompt_alert = wait.until(EC.alert_is_present())
        print("❌ Dismissing prompt (Cancel)...")
        prompt_alert.dismiss()
        time.sleep(1)
        
        result = driver.find_element(By.ID, "result").text
        print(f"✅ Result after Cancel: {result}")
        
        # Summary
        print("\n" + "="*60)
        print("📚 KEY LEARNINGS:")
        print("="*60)
        print("✅ alert.accept() - Click OK")
        print("✅ alert.dismiss() - Click Cancel")
        print("✅ alert.text - Get alert message")
        print("✅ alert.send_keys(text) - Type in prompt")
        print("✅ EC.alert_is_present() - Wait for alert")
        print("⚠️  IMPORTANT: Handle alert BEFORE screenshots!")
        print("="*60)
        
        print("\n⏸️  Keeping browser open for 3 seconds...")
        time.sleep(3)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        # Try to close any open alert
        try:
            driver.switch_to.alert.dismiss()
        except:
            pass
        driver.save_screenshot("screenshots/alerts_error.png")
        
    finally:
        print("\n🧹 Closing browser...")
        driver.quit()
        print("✅ Test completed!\n")

if __name__ == "__main__":
    test_alerts_handling()
