from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_logout(page):
    """
    Logout must terminate the session and prevent access to authenticated pages.
    """

    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.open()
    login.login("standard_user", "secret_sauce")

    assert inventory.is_loaded(), "Login failed, cannot test logout"

    inventory.logout()

    assert page.url == "https://www.saucedemo.com/", "User was not redirected to login page after logout"
    assert page.locator("#login-button").is_visible(), "Login button not visible after logout"
