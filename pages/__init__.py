"""
Page Objects Package
Import all page objects here for easy access
"""

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.secure_page import SecurePage

__all__ = ['BasePage', 'LoginPage', 'SecurePage']
