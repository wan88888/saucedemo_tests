from behave import given, when, then
from pages.cart_page import CartPage
from utils.step_helpers import login_user, add_item_to_cart, navigate_to_cart, verify_cart_badge_count, verify_inventory_page_loaded
import allure

@given("the user is logged in to SauceDemo")
def step_impl(context):
    login_user(context)

@given("the user has added an item to the cart")
def step_impl(context):
    add_item_to_cart(context)

@given("the user is on the cart page")
def step_impl(context):
    navigate_to_cart(context)

@when("the user adds an item to the cart")
def step_impl(context):
    add_item_to_cart(context)

@when("the user goes to the cart page")
def step_impl(context):
    navigate_to_cart(context)

@when("the user removes the item from cart")
def step_impl(context):
    context.cart_page.remove_first_item()

@when("the user clicks continue shopping")
def step_impl(context):
    context.cart_page.continue_shopping()

@then("the cart should contain {count:d} item")
def step_impl(context, count):
    verify_cart_badge_count(context.page, count)

@then("the cart icon should show the item count")
def step_impl(context):
    verify_cart_badge_count(context.page, 1)

@then("the cart should display the added item")
def step_impl(context):
    assert context.cart_page.get_cart_items_count() > 0
    item_names = context.cart_page.get_item_names()
    assert context.added_item_name in item_names

@then("the item details should be correct")
def step_impl(context):
    # Verify item name is displayed correctly
    item_names = context.cart_page.get_item_names()
    assert len(item_names) > 0
    assert context.added_item_name in item_names

@then("the cart should be empty")
def step_impl(context):
    assert context.cart_page.is_cart_empty()
    verify_cart_badge_count(context.page, 0)

@then("the user should be redirected to the inventory page")
def step_impl(context):
    verify_inventory_page_loaded(context.page)