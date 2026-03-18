# OpenCart Automation Testing

This project automates a test scenario on [demo.opencart.com](https://demo.opencart.com/) using Selenium WebDriver with Python. It follows the Page Object Model (POM) design pattern and includes explicit waits, assertions, and logging.

## Test Scenario
- Search for "iPhone"
- Add product to cart
- Verify success message and cart total
- Proceed to checkout

## Setup
1. Clone this repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate it:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Download ChromeDriver matching your Chrome version from [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/) and place `chromedriver.exe` in the `drivers/` folder.

## Run Tests
```bash
pytest tests/ -v --html=report.html