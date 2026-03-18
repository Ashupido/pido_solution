# pages/search_results_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.base_page import BasePage
import time

class SearchResultsPage(BasePage):
    # More reliable locator for the first product link
    FIRST_PRODUCT = (By.CSS_SELECTOR, ".product-thumb h4 a")

    def __init__(self, driver):
        super().__init__(driver)

    def click_first_product(self):
        print("DEBUG: Waiting for search results to load...")
        time.sleep(3)  # Extra wait for results to appear
        
        print("DEBUG: Waiting for product links to be present...")
        # Wait specifically for product links to be present
        self.wait.until(EC.presence_of_all_elements_located(self.FIRST_PRODUCT))
        
        print("DEBUG: Attempting to click on first product link...")
        
        # Try normal click first
        try:
            self.click(self.FIRST_PRODUCT)
            print("DEBUG: Normal click successful.")
        except Exception as e:
            print(f"DEBUG: Normal click failed ({e}), trying JavaScript click...")
            # Fallback: Use JavaScript to click
            element = self.driver.find_element(*self.FIRST_PRODUCT)
            self.driver.execute_script("arguments[0].click();", element)
            print("DEBUG: JavaScript click executed.")
        
        # Wait for product page to load
        time.sleep(3)
        from pages.product_page import ProductPage
        return ProductPage(self.driver)