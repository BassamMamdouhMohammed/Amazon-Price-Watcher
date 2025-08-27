# tests/test_search.py
from pages.home_page import HomePage
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_search_product(browser):
    """Verify that product search works on Amazon."""
    home = HomePage(browser)
    home.open("https://www.amazon.com")
    home.search_product("Logitech Mouse")
    home.wait.until(EC.title_contains("Logitech Mouse"))
    # Assert the page title contains the search term
    assert "Logitech Mouse" in browser.title
