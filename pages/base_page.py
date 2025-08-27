# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Base class for all pages, provides common Selenium actions."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) 

    def find(self, locator):
        """Wait for element to be present and return it."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """Wait for element and click it."""
        self.find(locator).click()

    def send_keys(self, locator, text):
        """Wait for element and type into it."""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Get text of element."""
        return self.find(locator).text

    def is_visible(self, locator):
        """Check if element is visible."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
