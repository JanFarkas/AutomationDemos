from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_valid_login(page):

    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.open()
    login.login("standard_user", "secret_sauce")

    assert (
        inventory.is_loaded()
    ), "User was not redirected to inventory after valid login"
