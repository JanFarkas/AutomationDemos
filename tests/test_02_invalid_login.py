from pages.login_page import LoginPage


def test_invalid_login(page):
    """
    BUSINESS CRITICAL:
    Invalid login must be handled gracefully with a clear error message.
    Prevents unauthorized access and informs the user what went wrong.
    """

    login = LoginPage(page)

    login.open()
    login.login("standard_user", "wrong_password")

    error = login.get_error()

    assert "Username and password do not match" in error
