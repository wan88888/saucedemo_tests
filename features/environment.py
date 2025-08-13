from playwright.sync_api import sync_playwright

def before_all(context):
    """启动 Playwright 和浏览器"""
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.base_url = "https://www.saucedemo.com"

def before_feature(context, feature):
    """为每个功能创建新的页面"""
    context.page = context.browser.new_page()

def after_feature(context, feature):
    """关闭页面"""
    if hasattr(context, 'page'):
        context.page.close()

def after_scenario(context, scenario):
    """Clean up after each scenario"""
    # Clear cart by going to inventory and removing all items
    if hasattr(context, 'page') and context.page:
        try:
            context.page.goto(f"{context.base_url}/inventory.html")
            # Remove all items from cart
            remove_buttons = context.page.locator("button[id^='remove']")
            count = remove_buttons.count()
            for i in range(count):
                if remove_buttons.nth(i).is_visible():
                    remove_buttons.nth(i).click()
        except:
            pass

def after_all(context):
    """关闭浏览器"""
    context.browser.close()
    context.playwright.stop()