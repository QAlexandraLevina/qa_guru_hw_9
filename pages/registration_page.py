import os

from selene import browser, by, have


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element("#firstName")
        self.last_name = browser.element("#lastName")
        self.state = browser.element("#state input")
        self.city = browser.element("#city input")
        self.registered_user_data = browser.element(".table").all("td").even

    """Заполнение поля First Name"""

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    """Заполнение поля Last Name"""

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    """Заполнение поля Email"""

    def fill_email(self, email):
        browser.element("#userEmail").type(email)
        return self

    """Выбор радио-кнопки в поле Gender"""

    def set_gender(self, value):
        browser.element("#genterWrapper").element(by.text(value)).click()
        return self

    """Заполнение поля Mobile"""

    def fill_mobile(self, mobile):
        browser.element("#userNumber").type(mobile)
        return self

    """Заполнение поля Date of Birth"""

    def fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").type(year)
        browser.element(".react-datepicker__month-select").type(month)
        browser.element(f".react-datepicker__day--0{day}").click()
        return self

    """Заполнение поля Subjects"""

    def fill_subjects(self, value):
        browser.element("#subjectsInput").type(value).press_enter()
        return self

    """Выбор чек-бокса Hobbies"""

    def set_hobbies(self, value_1, value_2, value_3):
        browser.element("#hobbiesWrapper").element(by.text(value_1)).click()
        browser.element("#hobbiesWrapper").element(by.text(value_2)).click()
        browser.element("#hobbiesWrapper").element(by.text(value_3)).click()
        return self

    """Загрузка изображения в поле Picture"""

    def upload_picture(self, value):
        image_test_file = os.path.join(os.path.dirname(__file__), value)
        browser.element("#uploadPicture").send_keys(image_test_file)
        return self

    """Заполнение поля Current Address"""

    def fill_current_address(self, value):
        browser.element("#currentAddress").set_value(value)
        return self

    """Выбор State and City"""

    def set_state_city(self, val_stat, val_cit):
        self.state.type(val_stat).press_enter()
        self.city.type(val_cit).press_enter()
        return self

    """Нажатие кнопки Submit"""

    def submit_form(self):
        browser.element("#submit").click()
        return self

    """Проверка заполненной формы"""

    def should_registered_user_with(
        self,
        full_name,
        email,
        gender,
        mobile,
        date,
        subject,
        hobbies,
        picture,
        address,
        state_city,
    ):
        self.registered_user_data.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                mobile,
                date,
                subject,
                hobbies,
                picture,
                address,
                state_city,
            )
        )
        return self

    """Закрытие формы"""

    def close_form(self):
        browser.element("#closeLargeModal").click()
        return self
