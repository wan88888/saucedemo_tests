from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_items = page.locator('[data-test="inventory-item"]')
        self.checkout_button = page.locator("#checkout")
        self.continue_shopping_button = page.locator("#continue-shopping")
        self.remove_buttons = page.locator("button[id^='remove']")
        self.item_names = page.locator('.inventory_item_name')
        self.item_prices = page.locator(".inventory_item_price")
        self.cart_badge = page.locator('.shopping_cart_badge')
        
    def get_cart_items_count(self):
        """Get the number of items in the cart"""
        return self.cart_items.count()
    
    def get_item_names(self):
        """Get all item names in the cart"""
        return [name.text_content() for name in self.item_names.all()]
    
    def remove_first_item(self):
        """Remove the first item from cart"""
        self.remove_buttons.first.click()
    
    def proceed_to_checkout(self):
        """Click checkout button"""
        self.checkout_button.click()
    
    def continue_shopping(self):
        """Continue shopping"""
        self.continue_shopping_button.click()
    
    def is_cart_empty(self):
        """Check if cart is empty"""
        return self.get_cart_items_count() == 0