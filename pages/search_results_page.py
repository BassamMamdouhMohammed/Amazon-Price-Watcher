from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    """Amazon Search Results Page."""

    # --- Locators ---
    PRODUCT_TITLES = (By.CSS_SELECTOR, "a.a-link-normal h2 span")
    PRODUCT_LINKS = (By.CSS_SELECTOR, "a.a-link-normal.s-line-clamp-2")
    NO_RESULTS_MSG = (By.CSS_SELECTOR, "div.a-section.a-spacing-small.a-spacing-top-small")
    FOUR_STAR_UP = (By.XPATH, "//span[@aria-label='4 Stars & Up']")



    def __init__(self, driver):
        super().__init__(driver)

    # --- Actions ---
    def get_search_results(self):
        """Retrieve a list of search result elements."""
        return self.driver.find_elements(*self.PRODUCT_LINKS)

    def has_no_results_message(self):
        """Check if the no results message is displayed."""
        return self.is_element_present(self.NO_RESULTS_MSG)
    
    def open_product_by_index(self, index):
        """Open a product detail page by its index in the search results."""
        products = self.get_search_results()
        if index < len(products):
            products[index].click()
        else:
            raise IndexError("Product index out of range")
    
    