import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = "https://demoqa.com"
    browser.execute_script("window.scrollBy(0, 500)")
    browser.config.timeout = 10
    yield
    browser.quit()
