import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.parametrize(
    "item_index,expected_count",
    [
        (0, 1),
        (1, 1),
        (2, 1),
    ],
)
def test_addToCart(page, item_index, expected_count):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.open()
    login.login("standard_user", "secret_sauce")
    assert inventory.is_loaded()

    for i in range(3):
        inventory.add_item_by_index(i)

    assert inventory.get_cart_badge_count() == 3
