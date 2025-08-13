from playwright.sync_api import sync_playwright
import time
import os
from utils.report_utils import cleanup_old_reports, save_failure_screenshot

def before_all(context):
    """启动 Playwright 和浏览器，清理旧报告"""
    # 清理旧的测试报告和截图
    cleanup_old_reports()
    
    # 启动 Playwright 和浏览器
    context.playwright = sync_playwright().start()
    # 添加更稳定的浏览器启动配置
    context.browser = context.playwright.chromium.launch(
        headless=False,
        args=[
            '--no-sandbox',
            '--disable-dev-shm-usage',
            '--disable-web-security',
            '--disable-features=VizDisplayCompositor'
        ]
    )
    context.base_url = "https://www.saucedemo.com"
    


def before_feature(context, feature):
    """为每个功能创建新的页面"""
    context.page = context.browser.new_page()
    # 设置页面超时时间
    context.page.set_default_timeout(30000)  # 30秒
    context.page.set_default_navigation_timeout(30000)  # 30秒
    
    # 添加页面错误监听
    def handle_page_error(error):
        print(f"页面错误: {error}")
    
    context.page.on("pageerror", handle_page_error)

def after_feature(context, feature):
    """关闭页面"""
    if hasattr(context, 'page'):
        context.page.close()

def after_scenario(context, scenario):
    """Clean up after each scenario"""
    # 如果场景失败，保存截图
    if scenario.status == 'failed' and hasattr(context, 'page') and context.page:
        save_failure_screenshot(context.page, scenario.name)
    
    # Clear cart by removing all items from inventory page
    if hasattr(context, 'page') and context.page:
        try:
            context.page.goto(f"{context.base_url}/inventory.html")
            # Remove all visible items from cart
            remove_buttons = context.page.locator("button[id^='remove']")
            for i in range(remove_buttons.count()):
                button = remove_buttons.nth(i)
                if button.is_visible():
                    button.click()
        except Exception:
            # Silently ignore cleanup errors
            pass

def after_all(context):
    """关闭浏览器"""
    if hasattr(context, 'browser') and context.browser:
        context.browser.close()
    if hasattr(context, 'playwright') and context.playwright:
        context.playwright.stop()