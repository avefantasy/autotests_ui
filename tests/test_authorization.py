import pytest
from pages.login_page import LoginPage

@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("email, password", [("user.name@gmail.com", "password"),
                                            ("user.name@gmail.com", "  "),
                                            ("  ", "password")])
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):

    # Переход на страницу входа
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Заполнение email и password
    login_page.fill_login_form(email=email, password=password)

    # Нажатие кнопки Login
    login_page.click_login_button()

    # Проверка сообщения об ошибке
    login_page.check_visible_wrong_email_or_password_alert()