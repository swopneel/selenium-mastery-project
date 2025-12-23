"""
Browser Configuration Utilities
Provides pre-configured browser options for test automation
"""

from selenium.webdriver.chrome.options import Options
import tempfile
import os


def get_chrome_options():
    """
    Get Chrome options configured for test automation
    
    Uses a temporary user profile to completely avoid password manager prompts.
    
    Returns:
        Options: Configured Chrome options
    """
    chrome_options = Options()
    
    # Create temporary directory for Chrome profile
    temp_dir = tempfile.mkdtemp()
    
    # Use temporary profile (completely fresh, no password manager history)
    chrome_options.add_argument(f'--user-data-dir={temp_dir}')
    
    # Window settings
    chrome_options.add_argument('--start-maximized')
    
    # Disable password save bubble
    chrome_options.add_argument('--disable-save-password-bubble')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-infobars')
    
    # Disable various browser prompts via preferences
    prefs = {
        'credentials_enable_service': False,
        'profile.password_manager_enabled': False,
        'autofill.profile_enabled': False,
        'profile.default_content_setting_values.notifications': 2,
    }
    
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    return chrome_options