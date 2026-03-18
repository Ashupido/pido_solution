# pages/product_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.base_page import BasePage
import time

class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "button-cart")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert.alert-success")
    CART_TOTAL = (By.CSS_SELECTOR, "#cart-total")
    CART_DROPDOWN = (By.CSS_SELECTOR, "#cart button")
    CHECKOUT_BUTTON = (By.LINK_TEXT, "Checkout")

    def __init__(self, driver):
        super().__init__(driver)

    def add_to_cart(self):
        print("DEBUG: Clicking Add to Cart...")
        self.click(self.ADD_TO_CART_BUTTON)
        # Wait a moment for the cart to update
        time.sleep(2)

    def get_success_message(self):
        print("DEBUG: Waiting for success message...")
        # Use explicit wait with longer timeout
        element = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_ALERT))
        text = element.text
        print(f"DEBUG: Success message text: '{text}'")
        return text

    def get_cart_total(self):
        print("DEBUG: Waiting for cart total to update...")
        # Wait for cart total to contain something (not empty)
        def cart_total_updated(driver):
            element = driver.find_element(*self.CART_TOTAL)
            return element.text.strip() and "0 item(s)" not in element.text
        self.wait.until(cart_total_updated)
        text = self.get_text(self.CART_TOTAL)
        print(f"DEBUG: Cart total text: '{text}'")
        return text

    def go_to_checkout(self):
        print("DEBUG: Opening cart dropdown...")
        self.click(self.CART_DROPDOWN)
        time.sleep(1)
        print("DEBUG: Clicking Checkout...")
        self.click(self.CHECKOUT_BUTTON)
        time.sleep(2)