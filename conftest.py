import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open("https://demoqa.com/automation-practice-form")
    browser.execute_script("window.scrollBy(0, 500)")
    browser.config.timeout = 10
    yield
    browser.quit()
