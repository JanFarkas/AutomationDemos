from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

    def is_loaded(self) -> bool:
        return self.page.locator(".title").inner_text() == "Products"

    def open_menu(self):
        self.page.click("#react-burger-menu-btn")

    def logout(self):
        self.open_menu()
        self.page.click("#logout_sidebar_link")

    def add_first_item_to_cart(self):
        self.page.click(".inventory_item button")

    def get_cart_badge_count(self) -> int:
        return int(self.page.locator(".shopping_cart_badge").inner_text())
    
    def add_item_by_index(self, index: int):
        buttons = self.page.locator(".inventory_item button")
        buttons.nth(index).click()