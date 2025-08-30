from selene import browser, have


class TextBoxPage:
    def __init__(self):
        self.full_name = browser.element("#userName")
        self.email = browser.element("#userEmail")
        self.current_address = browser.element("#currentAddress")
        self.permanent_address = browser.element("#permanentAddress")
        self.submit_button = browser.element("#submit")
        self.registered_user_text_box = browser.all(".border p")

    """Заполнение полей формы"""

    def fill_full_name(self, name):
        self.full_name.type(name)
        return self

    def fill_email(self, mail):
        self.email.type(mail)
        return self

    def fill_current_address(self, current_add):
        self.current_address.type(current_add)
        return self

    def fill_permanent_address(self, permanent_add):
        self.permanent_address.type(permanent_add)
        return self

    """Проверка заполненных полей"""

    def should_registered_user_text_box(
        self, full_name, email, current_address, permanent_address
    ):
        self.registered_user_text_box.should(
            have.exact_texts(
                f"Name:{full_name}",
                f"Email:{email}",
                f"Current Address :{current_address}",
                f"Permananet Address :{permanent_address}",
            )
        )
        return self
