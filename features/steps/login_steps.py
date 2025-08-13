from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.constants import BASE_URL, STANDARD_USER, STANDARD_PASSWORD

@given("the user is on the SauceDemo login page")
def step_impl(context):
    context.login_page = LoginPage(context.page)
    context.login_page.go_to(BASE_URL)

@when("they enter valid credentials")
def step_impl(context):
    context.login_page.login(STANDARD_USER, STANDARD_PASSWORD)

@then("they should be redirected to the inventory page")
def step_impl(context):
    context.inventory_page = InventoryPage(context.page)
    assert "inventory" in context.page.url, "Should be redirected to inventory page"
