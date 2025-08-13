from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.constants import BASE_URL, STANDARD_USER, STANDARD_PASSWORD

@given("the user is logged in to SauceDemo")
def step_impl(context):
    context.login_page = LoginPage(context.page)
    context.login_page.go_to(BASE_URL)
    context.login_page.login(STANDARD_USER, STANDARD_PASSWORD)
    context.inventory_page = InventoryPage(context.page)

def _add_item_to_cart(context):
    """Helper function to add item to cart"""
    context.inventory_page.add_first_item_to_cart()
    context.added_item_name = context.page.locator('.inventory_item_name').first.text_content()

def _go_to_cart_page(context):
    """Helper function to navigate to cart page"""
    context.inventory_page.go_to_cart()
    context.cart_page = CartPage(context.page)

@given("the user has added an item to the cart")
def step_impl(context):
    _add_item_to_cart(context)

@given("the user is on the cart page")
def step_impl(context):
    _go_to_cart_page(context)

@when("the user adds an item to the cart")
def step_impl(context):
    _add_item_to_cart(context)

@when("the user goes to the cart page")
def step_impl(context):
    _go_to_cart_page(context)

@when("the user removes the item from cart")
def step_impl(context):
    context.cart_page.remove_first_item()

@when("the user clicks continue shopping")
def step_impl(context):
    context.cart_page.continue_shopping()

def _check_cart_badge(context, expected_count):
    """Helper function to check cart badge"""
    cart_badge = context.page.locator('.shopping_cart_badge')
    if expected_count > 0:
        assert cart_badge.is_visible(), f"Cart badge should be visible for {expected_count} items"
        assert cart_badge.text_content() == str(expected_count), f"Cart should show {expected_count} items"
    else:
        assert not cart_badge.is_visible(), "Cart badge should not be visible when empty"

@then("the cart should contain {count:d} item")
def step_impl(context, count):
    _check_cart_badge(context, count)

@then("the cart icon should show the item count")
def step_impl(context):
    _check_cart_badge(context, 1)

def _verify_item_in_cart(context):
    """Helper function to verify item is in cart"""
    item_names = context.cart_page.get_item_names()
    assert context.added_item_name in item_names, f"Item '{context.added_item_name}' should be in cart"

@then("the cart should display the added item")
def step_impl(context):
    assert context.cart_page.get_cart_items_count() > 0, "Cart should not be empty"
    _verify_item_in_cart(context)

@then("the item details should be correct")
def step_impl(context):
    _verify_item_in_cart(context)

@then("the cart should be empty")
def step_impl(context):
    assert context.cart_page.is_cart_empty()

@then("the user should be redirected to the inventory page")
def step_impl(context):
    assert "inventory" in context.page.url, "Should be redirected to inventory page"