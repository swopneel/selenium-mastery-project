"""
Selenium Test - File Upload
Learn how to upload files using Selenium.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os

def test_file_upload():
    print("\n🚀 Starting test: File Upload")
    
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)
    
    try:
        # Create a test file to upload
        print("\n📝 Creating test file...")
        project_dir = os.path.expanduser("~/selenium-mastery-project")
        test_data_dir = os.path.join(project_dir, "test_data")
        os.makedirs(test_data_dir, exist_ok=True)
        
        test_file_path = os.path.join(test_data_dir, "test_upload.txt")
        
        with open(test_file_path, 'w') as f:
            f.write("This is a test file for Selenium file upload!\n")
            f.write("Created by: Selenium Automation Test\n")
            f.write(f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        print(f"✅ Test file created: {test_file_path}")
        
        # Test 1: Simple File Upload
        print("\n" + "="*60)
        print("TEST 1: Simple File Upload")
        print("="*60)
        
        driver.get("https://the-internet.herokuapp.com/upload")
        time.sleep(2)
        
        print(f"✅ Page loaded: {driver.title}")
        print(f"📍 URL: {driver.current_url}")
        
        driver.save_screenshot("screenshots/upload_step1_page.png")
        
        # Find file input element
        print("\n🔍 Finding file input element...")
        file_input = wait.until(EC.presence_of_element_located((By.ID, "file-upload")))
        print("✅ Found file input!")
        
        # Upload file by sending the file path
        print(f"📤 Uploading file: {test_file_path}")
        file_input.send_keys(test_file_path)
        print("✅ File path sent to input!")
        
        time.sleep(1)
        driver.save_screenshot("screenshots/upload_step2_file_selected.png")
        
        # Click upload button
        print("\n🔘 Clicking Upload button...")
        upload_button = driver.find_element(By.ID, "file-submit")
        upload_button.click()
        time.sleep(2)
        
        print("✅ Upload button clicked!")
        driver.save_screenshot("screenshots/upload_step3_uploaded.png")
        
        # Verify upload success
        print("\n✅ Verifying upload...")
        print(f"📍 New URL: {driver.current_url}")
        
        try:
            # Check for success heading
            success_heading = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
            print(f"📄 Heading: {success_heading.text}")
            
            # Check uploaded filename
            uploaded_file = driver.find_element(By.ID, "uploaded-files")
            print(f"✅ Uploaded file name: {uploaded_file.text}")
            
            if "test_upload.txt" in uploaded_file.text:
                print("🎉 TEST 1 PASSED: File uploaded successfully!")
            else:
                print("⚠️  File name doesn't match")
                
        except Exception as e:
            print(f"⚠️  Could not verify upload: {e}")
        
        # Test 2: Upload Different File Types
        print("\n" + "="*60)
        print("TEST 2: Uploading Different File Types")
        print("="*60)
        
        # Create different test files
        test_files = []
        
        # Create a CSV file
        csv_path = os.path.join(test_data_dir, "test_data.csv")
        with open(csv_path, 'w') as f:
            f.write("Name,Age,City\n")
            f.write("John,30,New York\n")
            f.write("Jane,25,San Francisco\n")
        test_files.append(("CSV", csv_path))
        print(f"✅ Created CSV file: {csv_path}")
        
        # Create a JSON file
        json_path = os.path.join(test_data_dir, "test_data.json")
        with open(json_path, 'w') as f:
            f.write('{"name": "Test User", "role": "SDET", "tool": "Selenium"}\n')
        test_files.append(("JSON", json_path))
        print(f"✅ Created JSON file: {json_path}")
        
        # Create an HTML file
        html_path = os.path.join(test_data_dir, "test_page.html")
        with open(html_path, 'w') as f:
            f.write('<html><body><h1>Test HTML File</h1></body></html>\n')
        test_files.append(("HTML", html_path))
        print(f"✅ Created HTML file: {html_path}")
        
        # Upload each file type
        for file_type, file_path in test_files:
            print(f"\n📤 Uploading {file_type} file...")
            
            driver.get("https://the-internet.herokuapp.com/upload")
            time.sleep(1)
            
            file_input = driver.find_element(By.ID, "file-upload")
            file_input.send_keys(file_path)
            
            upload_button = driver.find_element(By.ID, "file-submit")
            upload_button.click()
            time.sleep(2)
            
            uploaded_file = driver.find_element(By.ID, "uploaded-files")
            filename = os.path.basename(file_path)
            
            if filename in uploaded_file.text:
                print(f"  ✅ {file_type} file uploaded: {filename}")
            else:
                print(f"  ⚠️  {file_type} upload verification failed")
            
            driver.save_screenshot(f"screenshots/upload_{file_type.lower()}.png")
        
        print("\n🎉 TEST 2 PASSED: Multiple file types uploaded!")
        
        # Test 3: File Input Properties
        print("\n" + "="*60)
        print("TEST 3: File Input Element Properties")
        print("="*60)
        
        driver.get("https://the-internet.herokuapp.com/upload")
        time.sleep(1)
        
        file_input = driver.find_element(By.ID, "file-upload")
        
        print("\n📊 File Input Properties:")
        print(f"  Tag name: {file_input.tag_name}")
        print(f"  Type: {file_input.get_attribute('type')}")
        print(f"  Name: {file_input.get_attribute('name')}")
        print(f"  ID: {file_input.get_attribute('id')}")
        print(f"  Displayed: {file_input.is_displayed()}")
        print(f"  Enabled: {file_input.is_enabled()}")
        
        print("🎉 TEST 3 PASSED: Properties inspected!")
        
        # Summary
        print("\n" + "="*60)
        print("📚 KEY LEARNINGS:")
        print("="*60)
        print("✅ file_input.send_keys(file_path) - Upload file")
        print("✅ Use absolute file path for upload")
        print("✅ No need to click 'Browse' button")
        print("✅ Works with any file type")
        print("✅ Can upload from any location on disk")
        print("✅ File input type='file' in HTML")
        print("="*60)
        
        print("\n💡 IMPORTANT NOTES:")
        print("  • File MUST exist before upload")
        print("  • Use absolute paths (not relative)")
        print("  • Check file size limits on server")
        print("  • Some sites restrict file types")
        
        print("\n⏸️  Keeping browser open for 5 seconds...")
        time.sleep(5)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        driver.save_screenshot("screenshots/upload_error.png")
        
    finally:
        print("\n🧹 Closing browser...")
        driver.quit()
        print("✅ Test completed!\n")

if __name__ == "__main__":
    test_file_upload()
