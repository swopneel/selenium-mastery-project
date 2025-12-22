"""
Selenium Test - Handling Multiple Windows/Tabs
Learn how to switch between browser windows and tabs.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def test_multiple_windows():
    print("\n🚀 Starting test: Multiple Windows/Tabs Handling")
    
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)
    
    try:
        # Test 1: Opening New Window
        print("\n" + "="*60)
        print("TEST 1: Opening and Switching to New Window")
        print("="*60)
        
        driver.get("https://the-internet.herokuapp.com/windows")
        time.sleep(2)
        
        print(f"✅ Main page loaded: {driver.title}")
        print(f"📍 Main window URL: {driver.current_url}")
        
        # Store main window handle
        main_window = driver.current_window_handle
        print(f"🪟 Main window handle: {main_window}")
        
        # Get all windows before clicking
        print(f"📊 Number of windows open: {len(driver.window_handles)}")
        
        driver.save_screenshot("screenshots/windows_step1_main.png")
        
        # Click to open new window
        print("\n🔘 Clicking 'Click Here' to open new window...")
        new_window_link = driver.find_element(By.LINK_TEXT, "Click Here")
        new_window_link.click()
        time.sleep(2)
        
        # Wait for new window to open
        wait.until(EC.number_of_windows_to_be(2))
        print(f"✅ New window opened!")
        print(f"📊 Number of windows now: {len(driver.window_handles)}")
        
        # Get all window handles
        all_windows = driver.window_handles
        print(f"🪟 All window handles: {all_windows}")
        
        # Switch to new window
        print("\n🔄 Switching to new window...")
        for window in all_windows:
            if window != main_window:
                driver.switch_to.window(window)
                print(f"✅ Switched to new window: {window}")
                break
        
        time.sleep(2)
        print(f"📄 New window title: {driver.title}")
        print(f"📍 New window URL: {driver.current_url}")
        
        # Get text from new window
        try:
            new_window_heading = driver.find_element(By.TAG_NAME, "h3").text
            print(f"✅ Heading in new window: '{new_window_heading}'")
        except:
            pass
        
        driver.save_screenshot("screenshots/windows_step2_new_window.png")
        
        # Close new window
        print("\n❌ Closing new window...")
        driver.close()
        print("✅ New window closed!")
        
        # Switch back to main window
        print("🔄 Switching back to main window...")
        driver.switch_to.window(main_window)
        print(f"✅ Back to main window!")
        print(f"📄 Main window title: {driver.title}")
        
        driver.save_screenshot("screenshots/windows_step3_back_to_main.png")
        
        print("🎉 TEST 1 PASSED: Window switching successful!")
        
        # Test 2: Multiple Windows
        print("\n" + "="*60)
        print("TEST 2: Handling Multiple Windows at Once")
        print("="*60)
        
        driver.get("https://the-internet.herokuapp.com/windows")
        time.sleep(1)
        
        main_window = driver.current_window_handle
        
        # Open multiple new windows
        print("\n🔘 Opening 3 new windows...")
        for i in range(3):
            driver.find_element(By.LINK_TEXT, "Click Here").click()
            time.sleep(1)
            print(f"  ✅ Opened window {i+1}")
        
        wait.until(EC.number_of_windows_to_be(4))
        print(f"✅ Total windows open: {len(driver.window_handles)}")
        
        # Switch through all windows
        print("\n🔄 Switching through all windows...")
        for i, window_handle in enumerate(driver.window_handles):
            driver.switch_to.window(window_handle)
            print(f"  🪟 Window {i+1}:")
            print(f"     Title: {driver.title}")
            print(f"     URL: {driver.current_url}")
            time.sleep(1)
        
        # Close all windows except main
        print("\n❌ Closing all windows except main...")
        for window in driver.window_handles:
            if window != main_window:
                driver.switch_to.window(window)
                driver.close()
                print(f"  ✅ Closed window")
        
        # Switch back to main
        driver.switch_to.window(main_window)
        print("✅ Only main window remains!")
        print(f"📊 Windows remaining: {len(driver.window_handles)}")
        
        driver.save_screenshot("screenshots/windows_step4_cleanup.png")
        
        print("🎉 TEST 2 PASSED: Multiple windows handled!")
        
        # Test 3: Opening New Tab (Different Method)
        print("\n" + "="*60)
        print("TEST 3: Opening New Tab with JavaScript")
        print("="*60)
        
        main_window = driver.current_window_handle
        
        # Open new tab using JavaScript
        print("\n🔘 Opening new tab with JavaScript...")
        driver.execute_script("window.open('https://the-internet.herokuapp.com/', '_blank');")
        time.sleep(2)
        
        wait.until(EC.number_of_windows_to_be(2))
        print("✅ New tab opened!")
        
        # Switch to new tab
        all_tabs = driver.window_handles
        new_tab = [tab for tab in all_tabs if tab != main_window][0]
        
        driver.switch_to.window(new_tab)
        print(f"✅ Switched to new tab")
        print(f"📄 New tab title: {driver.title}")
        
        driver.save_screenshot("screenshots/windows_step5_new_tab.png")
        
        # Close new tab
        driver.close()
        driver.switch_to.window(main_window)
        print("✅ New tab closed, back to main!")
        
        print("🎉 TEST 3 PASSED: New tab opened and closed!")
        
        # Summary
        print("\n" + "="*60)
        print("📚 KEY LEARNINGS:")
        print("="*60)
        print("✅ driver.window_handles - Get all window handles")
        print("✅ driver.current_window_handle - Get current window")
        print("✅ driver.switch_to.window(handle) - Switch windows")
        print("✅ driver.close() - Close current window")
        print("✅ driver.quit() - Close all windows")
        print("✅ window.open() JS - Open new tab")
        print("="*60)
        
        print("\n⏸️  Keeping browser open for 5 seconds...")
        time.sleep(5)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        driver.save_screenshot("screenshots/windows_error.png")
        
    finally:
        print("\n🧹 Closing browser...")
        driver.quit()
        print("✅ Test completed!\n")

if __name__ == "__main__":
    test_multiple_windows()
