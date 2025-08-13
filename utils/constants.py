"""Constants for the test automation framework."""

# URLs
BASE_URL = "https://www.saucedemo.com/"
INVENTORY_URL_FRAGMENT = "inventory"
CART_URL_FRAGMENT = "cart"

# Credentials
STANDARD_USER = "standard_user"
STANDARD_PASSWORD = "secret_sauce"

# Selectors
CLASS_SELECTORS = {
    'cart_badge': '.shopping_cart_badge',
    'inventory_item': '.inventory_item',
    'inventory_item_name': '.inventory_item_name',
    'cart_item': '.cart_item'
}

# Directories
REPORTS_DIR = "reports"
SCREENSHOTS_DIR = "reports/screenshots"
ALLURE_RESULTS_DIR = "reports/allure-results"