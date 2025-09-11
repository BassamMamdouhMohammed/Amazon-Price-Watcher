from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    """Amazon Product Detail Page."""

    # --- Locators ---
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-button")
    PRODUCT_TITLE = (By.XPATH, "//span[@id='productTitle']")
    PRICE = (By.XPATH, "(//span[@class='a-price-whole'])")
    AVAILABILITY = (By.XPATH, "//span[@class='a-size-medium a-color-success']")
    CART_COUNT = (By.ID, "nav-cart-count")
    BUY_NOW_BTN = (By.ID, "buy-now-button")

    def __init__(self, driver):
        super().__init__(driver)

    # --- Actions ---
    def add_to_cart(self):
        """Click the 'Add to Cart' button."""
        self.click(self.ADD_TO_CART_BTN)
    
    def Buy_now(self):
        """Click the 'Buy Now' button."""
        self.click(self.BUY_NOW_BTN)

    def get_product_title(self):
        """Retrieve the product title."""
        return self.get_text(self.PRODUCT_TITLE).strip()

    def get_price(self):
        """Retrieve the product price."""
        return self.get_text(self.PRICE).strip()

    def get_availability(self):
        """Retrieve the product availability status."""
        return self.get_text(self.AVAILABILITY).strip()

    def get_cart_count(self):
        """Retrieve the number of items in the cart."""
        return int(self.get_text(self.CART_COUNT).strip())