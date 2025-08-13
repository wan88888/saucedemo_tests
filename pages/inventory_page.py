from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.add_to_cart_button = page.locator("button[id^='add-to-cart']")
        self.cart_icon = page.locator("#shopping_cart_container")
        self.cart_badge = page.locator('.shopping_cart_badge')
        self.inventory_items = page.locator('.inventory_item')
        self.item_names = page.locator('.inventory_item_name')

    def add_first_item_to_cart(self):
        """Add the first available item to cart."""
        self.add_to_cart_button.first.click()

    def add_item_to_cart_by_index(self, index=0):
        """Add item to cart by index."""
        self.add_to_cart_button.nth(index).click()

    def go_to_cart(self):
        """Navigate to the shopping cart."""
        self.cart_icon.click()

    def get_cart_badge_count(self):
        """Get the cart badge count if visible."""
        if self.cart_badge.is_visible():
            return int(self.cart_badge.text_content())
        return 0

    def get_first_item_name(self):
        """Get the name of the first inventory item."""
        return self.item_names.first.text_content()

    def get_inventory_items_count(self):
        """Get the total number of inventory items."""
        return self.inventory_items.count()
