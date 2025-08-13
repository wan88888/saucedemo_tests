from playwright.sync_api import sync_playwright
from utils.test_utils import cleanup_old_reports
from utils.constants import SCREENSHOTS_DIR
import os

def before_all(context):
    """Set up Playwright before all tests."""
    # Clean up old test reports and screenshots
    try:
        cleanup_old_reports()
    except Exception as e:
        print(f"Warning: Failed to cleanup old reports: {e}")
    
    print("Setting up Playwright...")
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    print("Playwright setup complete")

def before_scenario(context, scenario):
    """Set up a new browser page before each scenario."""
    print(f"Setting up scenario: {scenario.name}")
    print(f"Browser available: {hasattr(context, 'browser')}")
    if hasattr(context, 'browser'):
        context.page = context.browser.new_page()
        print("Page created successfully")
    else:
        print("ERROR: Browser not available in context")

def after_scenario(context, scenario):
    """Capture a screenshot on failure and close the page."""
    if scenario.status == "failed":
        # Ensure screenshots directory exists
        os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
        # Create safe filename by replacing spaces and special characters
        safe_name = scenario.name.replace(" ", "_").replace("/", "_")
        screenshot_path = f"{SCREENSHOTS_DIR}/{safe_name}_failed.png"
        try:
            context.page.screenshot(path=screenshot_path)
            print(f"Screenshot saved: {screenshot_path}")
        except Exception as e:
            print(f"Warning: Could not save screenshot: {e}")
    
    if hasattr(context, 'page'):
        context.page.close()


def after_all(context):
    """Close the browser and stop Playwright after all tests."""
    context.browser.close()
    context.playwright.stop()