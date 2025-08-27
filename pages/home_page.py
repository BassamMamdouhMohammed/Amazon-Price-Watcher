# pages/home_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    """Amazon Home Page with search functionality."""

    # --- Locators ---
    SEARCH_BAR = (By.ID, "twotabsearchtextbox")
    SEARCH_BTN = (By.ID, "nav-search-submit-button")

    def __init__(self, driver):
        super().__init__(driver)

    # --- Actions ---
    def open(self, base_url="https://www.amazon.com"):
        """Open Amazon home page."""
        self.driver.get(base_url)

    def search_product(self, product_name: str):
        """Search for a product using the search bar."""
        self.send_keys(self.SEARCH_BAR, product_name)
        self.click(self.SEARCH_BTN)
