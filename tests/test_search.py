# tests/test_search.py
from pages.home_page import HomePage
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time


def test_search_product(browser):
    """Verify that product search works on Amazon."""
    home = HomePage(browser)
    home.open("https://www.amazon.com")
    home.click_submit()
    home.search_product("Logitech Mouse")
    home.wait_for_title("Logitech Mouse")
    # Verify that search results are displayed  
    assert EC.title_contains("Logitech Mouse")(browser)
    # Assert the page title contains the search term


def test_search_results_clickByIndex(browser):
    """Verify that product search works on Amazon."""
    home = HomePage(browser)
    home.open("https://www.amazon.com")
    home.search_product("Logitech Mouse")
    # Verify that search results are displayed  
    search = home.go_to_search_results_page()
    search.open_product_by_index(2)