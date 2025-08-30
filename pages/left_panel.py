from selene import browser

from pages.text_box_page import TextBoxPage


class LeftPanelPage:
    def open_left_panel(self) -> TextBoxPage:
        browser.open("/text-box")
        return TextBoxPage()
