from playwright.sync_api import Page
from utils.constants import SCREENSHOTS_DIR
import os

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def go_to(self, url):
        """Navigate to the specified URL."""
        self.page.goto(url)

    def take_screenshot(self, step_name):
        """Take a screenshot and save it with the given step name."""
        # Ensure screenshots directory exists
        os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
        screenshot_path = f"{SCREENSHOTS_DIR}/{step_name}.png"
        self.page.screenshot(path=screenshot_path)
        return screenshot_path