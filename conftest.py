import pytest
import os

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path=f"screenshots/{item.name}.png")


@pytest.fixture(scope="session")
def api_context(playwright):
    API_KEY = os.getenv("REQRES_API_KEY", "PUT_YOUR_API_KEY_HERE")

    context = playwright.request.new_context(
        base_url="https://reqres.in",
        extra_http_headers={
            "x-api-key": API_KEY,
            "Accept": "application/json",
            "User-Agent": "QA-Automation"
        }
    )
    yield context
    context.dispose()