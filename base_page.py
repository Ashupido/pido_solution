# utilities/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # increased timeout

    def click(self, by_locator):
        try:
            self.wait.until(EC.element_to_be_clickable(by_locator)).click()
        except Exception as e:
            print(f"ERROR clicking element {by_locator}: {e}")
            raise

    def send_keys(self, by_locator, text):
        try:
            self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        except Exception as e:
            print(f"ERROR sending keys to element {by_locator}: {e}")
            raise

    def get_text(self, by_locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(by_locator)).text
        except Exception as e:
            print(f"ERROR getting text from element {by_locator}: {e}")
            raise

    def is_visible(self, by_locator):
        try:
            self.wait.until(EC.visibility_of_element_located(by_locator))
            return True
        except:
            return False