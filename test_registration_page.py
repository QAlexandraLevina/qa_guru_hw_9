from pages.registration_page import RegistrationPage

"""Заполнение и проверка заполненной формы регистрации"""


def test_filled_form():
    """Инициализация экземпляра класса"""
    registration_page = RegistrationPage()

    """Заполнение формы"""
    registration_page.fill_first_name("Alexandra")
    registration_page.fill_last_name("Levina")
    registration_page.fill_email("alexandralevina1@gmail.com")
    registration_page.set_gender("Female")
    registration_page.fill_mobile("8912345678")
    registration_page.fill_date_of_birth("2002", "February", "17")
    registration_page.fill_subjects("Computer Science")
    registration_page.set_hobbies("Sports", "Reading", "Music")
    registration_page.upload_picture("test_file.txt")
    registration_page.fill_current_address("Россия, г.Москва, ул.Маршала Жукова 1")
    registration_page.set_state_city("Uttar Pradesh", "Lucknow")
    registration_page.submit_form()

    """Проверка заполненной формы"""
    registration_page.should_registered_user_with(
        "Alexandra Levina",
        "alexandralevina1@gmail.com",
        "Female",
        "8912345678",
        "17 February,2002",
        "Computer Science",
        "Sports, Reading, Music",
        "test_file.txt",
        "Россия, г.Москва, ул.Маршала Жукова 1",
        "Uttar Pradesh Lucknow",
    )
    registration_page.close_form()
