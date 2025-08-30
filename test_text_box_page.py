from pages.application import app

"""Заполнение формы регистрации Text Box"""


def test_text_box():
    text_box_page = app.left_panel.open_left_panel()

    (
        text_box_page.fill_full_name("Alexandra Levina")
        .fill_email("alexandralevina1@gmail.com")
        .fill_current_address("Россия, г.Санкт-Петербург, ул.Мира 10")
        .fill_permanent_address("Россия, г.Москва, ул.Маршала Жукова 1")
        .submit_button.click()
    )

    text_box_page.should_registered_user_text_box(
        "Alexandra Levina",
        "alexandralevina1@gmail.com",
        "Россия, г.Санкт-Петербург, ул.Мира 10",
        "Россия, г.Москва, ул.Маршала Жукова 1",
    )
