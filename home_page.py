# pages/home_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utilities.base_page import BasePage
import time

class HomePage(BasePage):
    SEARCH_INPUT = (By.NAME, "search")
    # More robust locator for search button
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn-default")

    def __init__(self, driver):
        super().__init__(driver)

    def search_product(self, product_name):
        print("DEBUG: Typing product name...")
        self.send_keys(self.SEARCH_INPUT, product_name)
        time.sleep(1)
        
        # Try clicking the button
        try:
            print("DEBUG: Attempting to click search button...")
            self.click(self.SEARCH_BUTTON)
            print("DEBUG: Search button clicked.")
        except Exception as e:
            print(f"DEBUG: Button click failed ({e}), trying Enter key...")
            # Fallback: press Enter in the search input
            self.driver.find_element(*self.SEARCH_INPUT).send_keys(Keys.RETURN)
            print("DEBUG: Enter key sent.")
        
        # Wait for search results to load
        time.sleep(2)
        
        from pages.search_results_page import SearchResultsPage
        return SearchResultsPage(self.driver)