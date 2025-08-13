from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.constants import BASE_URL, STANDARD_USER, STANDARD_PASSWORD

@given("the user is on the SauceDemo login page")
def step_impl(context):
    context.login_page = LoginPage(context.page)
    # 添加重试机制来处理网络问题
    max_retries = 3
    for attempt in range(max_retries):
        try:
            context.login_page.go_to(BASE_URL)
            # 等待页面完全加载
            context.page.wait_for_load_state("networkidle")
            break
        except Exception as e:
            if attempt == max_retries - 1:
                raise Exception(f"无法加载登录页面，已重试 {max_retries} 次。错误: {str(e)}")
            print(f"第 {attempt + 1} 次尝试加载页面失败，正在重试...")
            import time
            time.sleep(2)

@when("they enter valid credentials")
def step_impl(context):
    context.login_page.login(STANDARD_USER, STANDARD_PASSWORD)

@then("they should be redirected to the inventory page")
def step_impl(context):
    context.inventory_page = InventoryPage(context.page)
    assert "inventory" in context.page.url, "Should be redirected to inventory page"
