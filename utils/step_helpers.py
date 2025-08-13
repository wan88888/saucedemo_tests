"""Helper functions for test steps to reduce code duplication."""

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.constants import BASE_URL, STANDARD_USER, STANDARD_PASSWORD, CLASS_SELECTORS

def login_user(context):
    """Common login functionality."""
    context.login_page = LoginPage(context.page)
    context.login_page.go_to(BASE_URL)
    context.login_page.login(STANDARD_USER, STANDARD_PASSWORD)
    context.inventory_page = InventoryPage(context.page)
    verify_url_contains(context.page, "inventory")

def add_item_to_cart(context):
    """Add first item to cart and store item name."""
    context.inventory_page.add_first_item_to_cart()
    context.added_item_name = context.inventory_page.page.locator(CLASS_SELECTORS['inventory_item_name']).first.text_content()

def navigate_to_cart(context):
    """Navigate to cart page and initialize cart page object."""
    context.inventory_page.go_to_cart()
    context.cart_page = CartPage(context.page)
    verify_url_contains(context.page, "cart")

def verify_url_contains(page, url_fragment):
    """Verify that current URL contains the specified fragment."""
    assert url_fragment in page.url, f"Expected URL to contain '{url_fragment}', but got '{page.url}'"

def verify_cart_badge_count(page, expected_count):
    """Verify cart badge shows correct count."""
    cart_badge = page.locator(CLASS_SELECTORS['cart_badge'])
    if expected_count > 0:
        assert cart_badge.is_visible(), "Cart badge should be visible when cart has items"
        actual_count = cart_badge.text_content()
        assert actual_count == str(expected_count), f"Expected cart badge to show {expected_count}, but got {actual_count}"
    else:
        assert not cart_badge.is_visible(), "Cart badge should not be visible when cart is empty"

def verify_inventory_page_loaded(page):
    """Verify that inventory page is properly loaded."""
    verify_url_contains(page, "inventory")
    inventory_items = page.locator(CLASS_SELECTORS['inventory_item'])
    assert inventory_items.count() > 0, "Inventory page should contain inventory items"