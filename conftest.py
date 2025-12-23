"""
pytest Configuration and Fixtures

This file is automatically discovered by pytest.
Fixtures defined here are available to all tests.
"""

import pytest
from selenium import webdriver
from utils.browser_config import get_chrome_options


# ==================== FIXTURES ====================

@pytest.fixture(scope="function")
def driver():
    """
    Provide a fresh Chrome WebDriver for each test.
    
    Scope: function (new driver for each test)
    
    Usage in test:
        def test_login(driver):
            driver.get("https://example.com")
    
    Benefits:
        - Automatic setup and teardown
        - No need to create/quit driver in tests
        - Consistent browser configuration
    """
    print("\n🔧 Setting up Chrome driver...")
    driver = webdriver.Chrome(options=get_chrome_options())
    
    yield driver  # Give driver to test
    
    # Cleanup (runs after test completes)
    print("🧹 Closing browser...")
    driver.quit()


@pytest.fixture(scope="function")
def login_page(driver):
    """
    Provide a LoginPage object ready to use.
    
    Usage in test:
        def test_something(login_page):
            login_page.open_login_page()
    """
    from pages.login_page import LoginPage
    return LoginPage(driver)


@pytest.fixture(scope="function")
def logged_in_secure_page(driver, login_page):
    """
    Provide a SecurePage object after successful login.
    
    Usage in test:
        def test_logout(logged_in_secure_page):
            # Already logged in!
            logged_in_secure_page.click_logout()
    """
    login_page.open_login_page()
    secure_page = login_page.login("tomsmith", "SuperSecretPassword!")
    secure_page.dismiss_password_manager_popup()
    return secure_page


# ==================== HOOKS ====================

def pytest_configure(config):
    """
    Called before test run starts.
    Setup reports directory.
    """
    import os
    os.makedirs("reports", exist_ok=True)
    os.makedirs("screenshots", exist_ok=True)
    print("\n" + "="*60)
    print("🚀 pytest Configuration Complete!")
    print("="*60)


def pytest_collection_finish(session):
    """
    Called after test collection is complete.
    Show how many tests were found.
    """
    print(f"\n📊 Collected {len(session.items)} tests")


# ==================== HTML REPORT CUSTOMIZATION ====================

@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    """Customize HTML report title"""
    report.title = "Selenium Mastery Project - Test Report"


def pytest_html_results_summary(prefix, summary, postfix):
    """Add custom content to HTML report summary"""
    prefix.extend([
        "<h2>Selenium Test Automation Report</h2>",
        "<p>Project: selenium-mastery-project</p>",
        "<p>Framework: Selenium WebDriver + pytest</p>"
    ])