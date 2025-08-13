from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def go_to(self, url):
        """Navigate to the specified URL."""
        self.page.goto(url)

    def find_element(self, selector):
        """Find an element by selector."""
        return self.page.locator(selector)

    def click(self, selector):
        """Click on an element."""
        self.find_element(selector).click()

    def fill(self, selector, text):
        """Fill an input field with text."""
        self.find_element(selector).fill(text)

    def get_text(self, selector):
        """Get the text content of an element."""
        return self.find_element(selector).text_content()