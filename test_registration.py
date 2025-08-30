from pages.registration_page import RegistrationPage
from users import UserData

"""Заполнение и проверка заполненной формы регистрации"""


def test_filled_form():
    """Инициализация экземпляров класса RegistrationPage и UserData"""
    alexandra = UserData(
        "Alexandra",
        "Levina",
        "alexandralevina1@gmail.com",
        "Female",
        "8912345678",
        ("February", "2002", "17"),
        "Computer Science",
        ("Sports", "Reading", "Music"),
        "test_file.txt",
        "Россия, г.Москва, ул.Маршала Жукова 1",
        ("Uttar Pradesh", "Lucknow"),
    )
    registration_page = RegistrationPage()
    registration_page.open_practice_form()

    """Заполнение формы"""
    registration_page.registration_user(alexandra)
    registration_page.close_button()

    """Проверка заполненной формы"""
    registration_page.should_registered_user_practice_form(alexandra)
